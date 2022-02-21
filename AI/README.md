## Tree

```
. fineapple/AI
├── preprocess
│   ├── generation
│   │   ├── power_generator.py
│   │   └── run.py              # 발전량 전처리 실행파일
│   ├── consumption
│   │   ├── weather_asos.py
│   │   ├── user_consumption.py
│   │   └── run.py              # 소비량 전처리 실행파일
├── model
│   ├── generation
│   │   ├── predict_ann.py
│   │   └──  ann_model_50k.pt   # ANN
│   ├── consumption
│   │   └── predict_xgboost.py
├── data
│   ├── private                 # 사용자의 개인정보: 소비량
│   │   └── PowerConsumption
│   ├── generation              # 입력한 주소의 발전량
│   │   └── PowerGeneration
│   └── ASOS                    # 입력한 주소의 기상정보
├── consumption-main.py         # 소비량 예측 main file
└── power-generation-main.py    # 발전량 예측 main file
```

## Model Structure

![AI-model-structure](https://user-images.githubusercontent.com/60145951/154900244-dc2caaa5-22ff-4d84-a87c-38e106353c1a.png)
