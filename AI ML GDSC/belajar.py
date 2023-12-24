#import library yang diperlukan
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import numpy as np
from scipy import stats
sales = pd.Series([200000, 150000, 100000, 50000, 0, -50000])
ads_spend = pd.Series([8000, 12000, 16000, 20000, 24000, 28000])
sales