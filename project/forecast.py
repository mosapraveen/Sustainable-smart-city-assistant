import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

def forecast_and_detect(filepath):
    df = pd.read_csv(filepath)
    
    df = df.set_index('Year')
    model = ARIMA(df['Usage'], order=(1,1,1))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=3)
    
    plt.figure(figsize=(6,4))
    df['Usage'].plot(label='History')
    forecast.plot(label='Forecast', color='green')
    plt.legend()
    plt.title('Forecast for Energy Usage')
    plt.xlabel('Year')
    plt.ylabel('Usage')
    plt.savefig('forecast_plot.png')
    
    forecast_df = pd.DataFrame({'Year': [2025, 2026, 2027], 'Forecasted Usage': forecast})
    return forecast_df
