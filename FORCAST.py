from AUTOMATIC_MODEL import create_automatic_models
from ETH_PRICES import prepare_eth_data_for_forecasting
import matplotlib.pyplot as plt

# Création des modèles automatiques
model_auto_high, model_auto_low = create_automatic_models()

# Préparation des données pour les prévisions
crypto_prices_high, crypto_prices_low = prepare_eth_data_for_forecasting()


def faire_predictions(model_auto_high, model_auto_low, crypto_prices_high, crypto_prices_low):
    import matplotlib.pyplot as plt
    import pandas as pd
    predictions_sarima_high, conf_int_high = model_auto_high.predict_in_sample(return_conf_int=True)
    predictions_sarima_low, conf_int_low = model_auto_low.predict_in_sample(return_conf_int=True)
    all_predictions_sarima_high = pd.concat([pd.Series(predictions_sarima_high, index=crypto_prices_high.index)], axis=0)
    all_predictions_sarima_low = pd.concat([pd.Series(predictions_sarima_low, index=crypto_prices_low.index)], axis=0)
    forecast_sarima_high = model_auto_high.predict(start=len(crypto_prices_high), end=len(crypto_prices_high) + 10)
    forecast_sarima_low = model_auto_low.predict(start=len(crypto_prices_low), end=len(crypto_prices_low) + 10)
    index_future_dates = pd.date_range(start=crypto_prices_high.index[-1], periods=11, freq='D')[1:]
    forecast_sarima_high_df = pd.DataFrame(forecast_sarima_high, index=index_future_dates, columns=['Predictions (High)'])
    forecast_sarima_low_df = pd.DataFrame(forecast_sarima_low, index=index_future_dates, columns=['Predictions (Low)'])

    plt.figure(figsize=(12, 6))
    plt.plot(crypto_prices_high, label='Prix observés (High)', color='blue')
    plt.plot(all_predictions_sarima_high, label='Prédictions (High)', color='red')
    plt.plot(forecast_sarima_high_df, label='Prédictions pour les 10 prochains jours (High)', color='green', linestyle='--')
    
    plt.title('Prédictions du modèle ARIMA pour les prix High')
    plt.legend()
    plt.show()
    
    plt.figure(figsize=(12, 6))
    plt.plot(crypto_prices_low, label='Prix observés (Low)', color='blue')
    plt.plot(all_predictions_sarima_low, label='Prédictions (Low)', color='red')
    plt.plot(forecast_sarima_low_df, label='Prédictions pour les 10 prochains jours (Low)', color='green', linestyle='--')
    
    plt.title('Prédictions du modèle ARIMA pour les prix Low')
    plt.legend()
    plt.show()
    
    print(forecast_sarima_high_df.head())
    print(forecast_sarima_low_df.head())
    return all_predictions_sarima_high, forecast_sarima_high_df, all_predictions_sarima_low, forecast_sarima_low_df
faire_predictions(model_auto_high, model_auto_low, crypto_prices_high, crypto_prices_low)
