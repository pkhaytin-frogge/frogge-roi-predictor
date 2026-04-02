import pandas as pd
import os
from catboost import CatBoostRegressor
from sklearn.model_selection import train_test_split

# ПУТИ К ФАЙЛАМ
DATA_PATH = 'data/raw_data.csv'
MODEL_SAVE_PATH = 'models/frogge_model.cbm'

# Проверка наличия папок
os.makedirs('models', exist_ok=True)

if not os.path.exists(DATA_PATH):
    print(f"Ошибка: Положи исходный файл в {DATA_PATH}")
else:
    df = pd.read_csv(DATA_PATH)
    
    # Расчет целевой переменной
    df['ROI'] = (df['product_sales'] / df['estimated_reach']) * 100
    
    # Очистка данных
    X = df.drop(columns=['campaign_id', 'start_date', 'end_date', 'ROI'])
    y = df['ROI']
    
    cat_features = ['platform', 'influencer_category', 'campaign_type']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("Обучение новой модели Frogge...")
    model = CatBoostRegressor(iterations=1000, learning_rate=0.05, depth=6, verbose=200)
    model.fit(X_train, y_train, cat_features=cat_features, eval_set=(X_test, y_test))

    # Сохранение в нужную папку
    model.save_model(MODEL_SAVE_PATH)
    print(f"Готово! Модель сохранена в {MODEL_SAVE_PATH}")