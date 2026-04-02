# Frogge ROI Predictor 🐸

Инструмент на базе Machine Learning (CatBoost) для прогнозирования эффективности рекламных кампаний у инфлюенсеров.

## 📦 Архитектура проекта

```text
frogge_predict_ml/
├── data/                  # Локальные данные (игнорируется Git)
│   ├── raw_data.csv       # Локальное хранилище данных и истории прогнозов на данных Kaggle. Пример https://www.kaggle.com/datasets/tfisthis/influencer-marketing-roi-dataset
│   └── frogge_history.csv # История всех сделанных прогнозов
├── models/                # Обученные модели (игнорируется Git)
│   └── frogge_model.cbm   # Веса модели CatBoost
├── train_model.py         # Скрипт для обучения модели на исторических данных
├── predict_roi.py         # Инструмент для проведения симуляций и расчета ожидаемого ROI в деньгах
├── .gitignore             # Правила исключения файлов
└── requirements.txt       # Список необходимых библиотек
```

### 🚀 Как запустить
1. Установите зависимости: `pip install -r requirements.txt`
2. Положите данные в `data/raw_data.csv`
3. Обучите модель: `python train_model.py`
4. Сделайте прогноз: `python predict_roi.py`
