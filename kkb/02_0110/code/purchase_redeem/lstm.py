# coding:utf-8

import os
import sys
import math
import warnings
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')
BASE_DIR = os.path.abspath(os.path.join(__file__, os.pardir))

############## 1. load data set
def load_data() -> pd.DataFrame:
    """
    return df:
    [
        total_purchase_amt,  # purchase
        total_redeem_amt,    # redeem
        yBalance,            # feature 1
        mfd_daily_yield,     # feature 2
        mfd_7daily_yield,    # feature 3
        Interest_O_N,        # feature 4
        Interest_1_W,        # feature 5
        Interest_1_Y,        # feature 6
    ]
    """
    # TODO: need to download large *.csv files
    df_user_profile = pd.read_csv(os.path.join(BASE_DIR, 'user_profile_table.csv'))
    df_user_balance = pd.read_csv(os.path.join(BASE_DIR, 'user_balance_table.csv'))
    df_mfd_bank_shibor = pd.read_csv(os.path.join(BASE_DIR, 'mfd_bank_shibor.csv'))
    df_mfd_day_share_interest = pd.read_csv(os.path.join(BASE_DIR, 'mfd_day_share_interest.csv'))

    # drop user related info, calc sum of purchase & redeem over all users
    df_balance = df_user_balance[['report_date', 'total_purchase_amt', 'total_redeem_amt', 'yBalance']]
    df_balance.index = pd.to_datetime(df_balance['report_date'], format='%Y%m%d')
    del df_balance['report_date']
    df_balance = df_balance.resample('D').sum()

    # join df_mfd_bank_shibor & df_mfd_day_share_interest
    df_mfd = df_mfd_bank_shibor.set_index('mfd_date').join(df_mfd_day_share_interest.set_index('mfd_date'))
    df_mfd.index = pd.to_datetime(df_mfd.index, format='%Y%m%d')
    df_mfd = df_mfd[['mfd_daily_yield', 'mfd_7daily_yield', 'Interest_O_N', 'Interest_1_W', 'Interest_1_Y']]

    # join df_balance & df_mfd
    df = df_balance.join(df_mfd)
    df = df.fillna(method='ffill')
    return df

############## 2. create train & test dataset
def create_train_test_data(df: pd.DataFrame, column='total_purchase_amt', use_other_features=True):
    # using data in last 30 days to predict data in the future 30 days
    n_in = 30
    n_out = 30

    if use_other_features:
        columns = [column] + list(df.columns[2:])
    else:
        columns = [column]
    df = df[columns]

    # normalization
    scaler = MinMaxScaler(feature_range=(0, 1))
    np_data = scaler.fit_transform(df)

    # create train_x, train_y, test_x
    train_x = []
    train_y = []
    for k in range(np_data.shape[0] - n_in - n_out):
        x = np_data[k:k+n_in, :].reshape((1, -1))
        y = np_data[k+n_in: k+n_in+n_out, 0].reshape((-1,))
        train_x.append(x)
        train_y.append(y)
    train_x = np.array(train_x)
    train_y = np.array(train_y)

    test_x = np_data[-n_in:, :].reshape((1, 1, -1))

    # create inverse transform function
    def inverse_trans_func(scaled_pred):
        scaled_pred = scaled_pred.reshape((-1,))
        """ dummy_data:
        y1, 0, ..., 0
        y2, 0, ..., 0
        y3, 0, ..., 0
        y4, 0, ..., 0
        """
        dummy_data = np.zeros((len(scaled_pred), len(columns)))
        dummy_data[:, 0] = scaled_pred
        return scaler.inverse_transform(dummy_data)[:, 0]
    return train_x, train_y, test_x, inverse_trans_func

############## 3. create LSTM model
def train_lstm(train_x, train_y):
    model = Sequential()
    model.add(LSTM(100, input_shape=(1, train_x.shape[-1]), return_sequences=True))
    model.add(LSTM(50, return_sequences=False))
    model.add(Dense(32))
    model.add(Dense(30))
    model.compile(optimizer='adam', loss='mse')
    result = model.fit(
        train_x,
        train_y,
        # epochs=4,
        epochs=200,
        batch_size=16,
        verbose=2,
    )
    return model

############## 4. predict
def run(df, use_other_features=True):
    df_out = pd.DataFrame()
    df_out['date'] = ['201409%02d' % k for k in range(1, 31)]
    # purchase
    train_x, train_y, test_x, inverse_trans_func = create_train_test_data(
        df, 'total_purchase_amt', use_other_features=use_other_features)
    model = train_lstm(train_x, train_y)
    scaled_pred = model.predict(test_x)
    pred = inverse_trans_func(scaled_pred)
    df_out['purchase'] = pred

    # redeem
    train_x, train_y, test_x, inverse_trans_func = create_train_test_data(
        df, 'total_redeem_amt', use_other_features=use_other_features)
    model = train_lstm(train_x, train_y)
    scaled_pred = model.predict(test_x)
    pred = inverse_trans_func(scaled_pred)
    df_out['redeem'] = pred
    
    # output
    df_out.to_csv('use_features_%s.csv' % use_other_features, header=False, index=False)


def main():
    np.random.seed(0)
    df = load_data()
    run(df, use_other_features=True)   # score 76.1022
    run(df, use_other_features=False)  # score 102.8396
    

if __name__ == '__main__':
    main()
