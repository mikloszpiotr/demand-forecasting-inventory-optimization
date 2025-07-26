import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

def train_model(df, feature_cols, target_col="quantity_sold"):
    X = df[feature_cols]
    y = df[target_col]
    X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False, test_size=0.2)
    model = xgb.XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=6)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    return model, preds, y_test, mae
