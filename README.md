# Frogge ROI Predictor 🐸

Инструмент на базе Machine Learning (CatBoost) для прогнозирования эффективности рекламных кампаний у инфлюенсеров.

## Архитектура проекта
frogge_predict_ml/
├── data/                   # Папка для всех данных
│   ├── raw_data.csv        # Локальное хранилище данных и истории прогнозов. Пример https://www.kaggle.com/datasets/tfisthis/influencer-marketing-roi-dataset
│   └── frogge_history.csv  # Результаты симуляций
├── models/                 # Папка для "мозгов"
│   └── frogge_model.cbm    # Сохраненная обученная модель
├── train_model.py          # Скрипт для обучения модели на исторических данных
├── predict_roi.py          # Инструмент для проведения симуляций и расчета ожидаемого ROI в деньгах
└── requirements.txt        # Список библиотек

## Как запустить
1. Установите зависимости: `pip install -r requirements.txt`
2. Положите данные в `data/raw_data.csv`
3. Обучите модель: `python train_model.py`
4. Сделайте прогноз: `python predict_roi.py`
