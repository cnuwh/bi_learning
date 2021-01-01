import os
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

INPUT_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), 'raw.csv'))

# load dataset
df = pd.read_csv(
    INPUT_FILE,
    index_col=0,
    parse_dates={'date': ['year', 'month', 'day', 'hour']},
    date_parser=lambda *args: datetime.datetime.strptime(' '.join(args), '%Y %m %d %H'),
)
df.drop('No', axis=1, inplace=True)
df = df[24:]
df['pm2.5'].fillna(0, inplace=True)
print(df.head())

# process categorical column cbwd, using LabelEncoder
le = preprocessing.LabelEncoder()
le.fit(df['cbwd'].values)
df['cbwd'] = le.transform(df['cbwd'])
print(df.head())

# visualize features
fig, axs = plt.subplots(8, 1)
x = list(range(df.shape[0]))
for k, col in enumerate(df.columns):
    axs[k].plot(x, df[col])
plt.savefig('features.png')

# normalize data to [0, 1]
min_max_scaler = preprocessing.MinMaxScaler()
np_scaled = min_max_scaler.fit_transform(df)
df = pd.DataFrame(np_scaled, columns=df.columns)
print(df.head())

# series to supervised, output [x0, x1, ... xN, y]
df = pd.concat([df, df['pm2.5'].shift(-1)], axis=1)
df.columns = ['x%s' % k for k in range(df.shape[1] - 1)] + ['y']
df.dropna(inplace=True)
print(df.head())

# split train & test dataset
train_size = int(df.shape[0] * 0.8)
train = df.values[:train_size, :]
test = df.values[train_size:, :]
train_x, train_y = train[:, :-1], train[:, -1]
test_x, test_y = test[:, :-1], test[:, -1]
print(train_x.shape, train_y.shape, test_x.shape, test_y.shape)

# reshape dataset to fit LSTM, [sample count, time step, feature count]
train_x = train_x.reshape([train_x.shape[0], 1, train_x.shape[1]])
test_x = test_x.reshape([test_x.shape[0], 1, test_x.shape[1]])

# train data using LSTM
model = Sequential()
model.add(LSTM(50, input_shape=(train_x.shape[1], train_x.shape[2])))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')
result = model.fit(
    train_x,
    train_y,
    epochs=10,
    batch_size=64,
    validation_data=(test_x, test_y),
    verbose=2,
    shuffle=False,
)
plt.figure('loss')
plt.plot(result.history['loss'], label='train', c='r')
plt.plot(result.history['val_loss'], label='test', c='g')
plt.legend(loc='best')
plt.savefig('loss.png')
print(model.summary())

# predict
train_pred = model.predict(train_x)
test_pred = model.predict(test_x)

# plot predicted result
plt.figure('pred_result')
plt.plot(df.values[:, -1], label='real', c='b')
plt.plot(train_pred, label='train_pred', c='g')
plt.plot([None] * train_size + list(test_pred), label='test_pred', c='r')
plt.legend(loc='best')
plt.savefig('pred_result.png')

# plot diff
train_diff = train_pred - df.values[:train_size, -1].reshape([-1, 1])
test_diff = test_pred - df.values[train_size:, -1].reshape([-1, 1])
plt.figure('pred_diff')
plt.plot(train_diff, label='train_diff', c='g')
plt.plot([None] * train_size + list(test_diff), label='test_diff', c='r')
plt.legend(loc='best')
plt.savefig('pred_diff.png')