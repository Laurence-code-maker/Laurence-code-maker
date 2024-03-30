
from DATA import get_eth_data
import statsmodels.api as sm

def prepare_eth_data_for_forecasting():
    # Utilisation de la fonction get_eth_data pour obtenir les données
    data = get_eth_data()
    
    # Sélectionner les colonnes 'Date', 'High' et 'Low'
    crypto_prices = data[["Date", "High", "Low"]].set_index('Date')

    return crypto_prices['High'], crypto_prices['Low']

# Utilisation de la fonction pour préparer les données
crypto_prices_high, crypto_prices_low = prepare_eth_data_for_forecasting()

# Affichage des premières valeurs pour vérification
print("Prix High :")
print(crypto_prices_high.head())
print("\nPrix Low :")
print(crypto_prices_low.head())
