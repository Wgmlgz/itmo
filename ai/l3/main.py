import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# 1. Загрузка и анализ данных
data = pd.read_csv("./california_housing_train.csv")

# Визуализация статистики
statistics = data.describe().transpose()
print(statistics)

# Визуализация распределений данных
plt.figure(figsize=(16, 12))
for i, column in enumerate(data.select_dtypes(include=['float64', 'int64']).columns):
    plt.subplot(3, 3, i + 1)
    sns.histplot(data[column], kde=True, color='skyblue')
    plt.title(f"Histogram for {column}")
plt.tight_layout()
plt.show()

# 2. Предварительная обработка данных
data.fillna(data.median(), inplace=True)  # Заполнение отсутствующих значений
scaler = MinMaxScaler()  # Нормализация данных
scaled_features = scaler.fit_transform(data.select_dtypes(include=['float64', 'int64']))
scaled_data = pd.DataFrame(scaled_features, columns=data.select_dtypes(include=['float64', 'int64']).columns)

# 3. Разделение на обучающий и тестовый наборы
train_data, test_data = train_test_split(scaled_data, test_size=0.2, random_state=42)

# 4. Реализация линейной регрессии
def linear_regression(X, y):
    X = np.c_[np.ones(X.shape[0]), X]  # Добавление столбца единиц
    coeff = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)  # Вычисление коэффициентов
    return coeff

def predict(X, coeff):
    X = np.c_[np.ones(X.shape[0]), X]  # Добавление столбца единиц
    return X.dot(coeff)

def r_squared(y_true, y_pred):
    ss_total = np.sum((y_true - np.mean(y_true))**2)
    ss_residual = np.sum((y_true - y_pred)**2)
    return 1 - (ss_residual / ss_total)

# 5. Построение моделей
X = train_data.drop('median_house_value', axis=1)
y = train_data['median_house_value']

# Модель 1: все признаки
coeff_1 = linear_regression(X, y)
predictions_1 = predict(test_data.drop('median_house_value', axis=1), coeff_1)
r2_1 = r_squared(test_data['median_house_value'], predictions_1)

# Модель 2: географические признаки
X_geo = train_data[['longitude', 'latitude']]
coeff_2 = linear_regression(X_geo, y)
predictions_2 = predict(test_data[['longitude', 'latitude']], coeff_2)
r2_2 = r_squared(test_data['median_house_value'], predictions_2)

# Модель 3: социальные признаки
X_social = train_data[['median_income', 'housing_median_age']]
coeff_3 = linear_regression(X_social, y)
predictions_3 = predict(test_data[['median_income', 'housing_median_age']], coeff_3)
r2_3 = r_squared(test_data['median_house_value'], predictions_3)

# Введение синтетического признака: отношение количества комнат к количеству спален
train_data['rooms_per_bedroom'] = train_data['total_rooms'] / train_data['total_bedrooms']
test_data['rooms_per_bedroom'] = test_data['total_rooms'] / test_data['total_bedrooms']

# Модель 4: социальные признаки + синтетический признак
X_synthetic = train_data[['median_income', 'housing_median_age', 'rooms_per_bedroom']]
coeff_4 = linear_regression(X_synthetic, y)
predictions_4 = predict(test_data[['median_income', 'housing_median_age', 'rooms_per_bedroom']], coeff_4)
r2_4 = r_squared(test_data['median_house_value'], predictions_4)

plt.figure(figsize=(16, 12))
for i, column in enumerate(scaled_data.columns):
    plt.subplot(3, 3, i + 1)
    sns.histplot(x=scaled_data[column], kde='true', color='lightgreen')
    plt.title(f"Histogram for {column} (Scaled)")

plt.tight_layout()
plt.show()

# 6. Вывод результатов
print(f"Модель 1 (все признаки) R^2: {r2_1:.3f}")
print(f"Модель 2 (географические признаки) R^2: {r2_2:.3f}")
print(f"Модель 3 (социальные признаки) R^2: {r2_3:.3f}")
print(f"Модель 4 (социальные признаки + синтетический признак) R^2: {r2_4:.3f}")