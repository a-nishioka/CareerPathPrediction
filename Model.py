from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor # ランダムフォレスト のライブラリ

class Model:
    def __init__(self):
        return

    def __del__(self):
        return

    def supervised_learn(self, datafram, target_col, exclude_cols):
        feature_cols = []
        for col in datafram.columns:
            if col not in exclude_cols:
                feature_cols.append(col)
        print(datafram[feature_cols])
        X = datafram[feature_cols]
        y = datafram[target_col]
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=1234)
        print('X_train Features Shape: ', X_train.shape)
        print('y_train Target Shape: ', y_train.shape)
        print('X_test Features Shape: ', X_test.shape)
        print('y_test Target Shape: ', y_test.shape)

        rf = RandomForestRegressor(random_state=1234)
        rf.fit(X_train, y_train)
        y_pred = rf.predict(X_test)
        rf_mse = mean_squared_error(y_test, y_pred)
        print('='*20)
        print('RandomForestClassifier')
        print(f'accuracy of train set: {rf.score(X_train, y_train)}')
        print(f'accuracy of test set: {rf.score(X_test, y_test)}')
