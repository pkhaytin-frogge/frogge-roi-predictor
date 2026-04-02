import pandas as pd
import os
from catboost import CatBoostRegressor
from datetime import datetime

# ПУТИ
MODEL_PATH = 'models/frogge_model.cbm'
HISTORY_PATH = 'data/frogge_history.csv'

if not os.path.exists(MODEL_PATH):
    print("Ошибка: Сначала запусти train_model.py, чтобы создать модель.")
    exit()

model = CatBoostRegressor()
model.load_model(MODEL_PATH)

def run_campaign_simulation(platform, category, reach, budget, avg_check, campaign_name="Test"):
    input_data = pd.DataFrame({
        'platform': [platform],
        'influencer_category': [category],
        'campaign_type': ['Product Launch'],
        'engagements': [int(reach * 0.05)],
        'estimated_reach': [reach],
        'product_sales': [0], 
        'campaign_duration_days': [14]
    })
    
    # Порядок колонок должен быть как при обучении
    column_order = ['platform', 'influencer_category', 'campaign_type', 
                    'engagements', 'estimated_reach', 'product_sales', 'campaign_duration_days']
    input_data = input_data[column_order]
    
    pred_efficiency = model.predict(input_data)[0]
    sales_count = (pred_efficiency / 100) * reach
    revenue = sales_count * avg_check
    money_roi = (revenue / budget) * 100

    result = {
        'date': datetime.now().strftime("%Y-%m-%d %H:%M"),
        'campaign_name': campaign_name,
        'platform': platform,
        'category': category,
        'reach': reach,
        'budget': budget,
        'avg_check': avg_check,
        'predicted_sales': round(sales_count, 0),
        'revenue': round(revenue, 2),
        'roi_percent': round(money_roi, 2)
    }

    # Сохранение в CSV в папку data/
    os.makedirs('data', exist_ok=True)
    new_row = pd.DataFrame([result])
    file_exists = os.path.isfile(HISTORY_PATH)
    new_row.to_csv(HISTORY_PATH, mode='a', index=False, header=not file_exists, encoding='utf-8-sig')
    
    print(f"Прогноз для {campaign_name} готов и записан в историю.")

# Пример запуска
run_campaign_simulation('YouTube', 'Tech', 150000, 700, 60, "Warsaw_Tech_Promo")