from ETH_PRICES import prepare_eth_data_for_forecasting
from pmdarima import auto_arima
def create_automatic_models():
    # Préparation des données ETH-USD
    crypto_prices_high, crypto_prices_low = prepare_eth_data_for_forecasting()
    
    # Créer le modèle SARIMA automatique pour les prix hauts (High)
    print("\nCréation du modèle SARIMA automatique pour les prix hauts (High)...")
    model_auto_high = auto_arima(crypto_prices_high, seasonal=True, m=12, trace=True)
    print("\nRésumé du modèle SARIMA pour les prix hauts (High):\n", model_auto_high.summary())

    # Créer le modèle SARIMA automatique pour les prix bas (Low)
    print("\nCréation du modèle SARIMA automatique pour les prix bas (Low)...")
    model_auto_low = auto_arima(crypto_prices_low, seasonal=True, m=12, trace=True)
    print("\nRésumé du modèle SARIMA pour les prix bas (Low):\n", model_auto_low.summary())
    
    return model_auto_high, model_auto_low

# Si vous souhaitez exécuter cette fonction lors de l'exécution du fichier .py
if __name__ == "__main__":
    create_automatic_models()