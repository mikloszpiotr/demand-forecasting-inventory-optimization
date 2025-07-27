
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Example true and predicted demand values
y_true = np.array([100, 150, 200, 130, 170])
y_pred = np.array([110, 145, 190, 135, 160])

mae = mean_absolute_error(y_true, y_pred)
rmse = mean_squared_error(y_true, y_pred, squared=False)
r2 = r2_score(y_true, y_pred)

print(f"MAE: {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R² Score: {r2:.2f}")
