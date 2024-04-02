
import time

# Import des fonctions depuis les fichiers Python
from DATA import get_eth_data
from DATA import visualize_eth_data
from DATA import decompose_eth_data
from ETH_PRICES import prepare_eth_data_for_forecasting

update_frequency = 86400  
def fonction():
    while True:
        print("Récupération des données...")
        # Récupération des données Ethereum
        data = get_eth_data()
        visualize_eth_data(data)
        decompose_eth_data(data)
        crypto_prices_high, crypto_prices_low = prepare_eth_data_for_forecasting()

        print("Création des modèles de prévision...")
        # Création des modèles de prévision automatiques
        from AUTOMATIC_MODEL import create_automatic_models
        model_auto_high, model_auto_low = create_automatic_models()
    
        
        print("Prévision des prix...")
        # Prédiction des prix
        from FORCAST import faire_predictions
        all_predictions_sarima_high, forecast_sarima_high_df, all_predictions_sarima_low, forecast_sarima_low_df = faire_predictions(model_auto_high, model_auto_low, crypto_prices_high, crypto_prices_low)
        
        
        print("Création du PDF de prévisions...")
        # Création du PDF de prévisions
        from PDF import create_predictions_pdf
        create_predictions_pdf(crypto_prices_high, all_predictions_sarima_high, forecast_sarima_high_df, crypto_prices_low, all_predictions_sarima_low, forecast_sarima_low_df)

        print("Envoi de l'email avec les prévisions...")
        # Envoi de l'email avec les prévisions en pièce jointe
        from EMAIL import send_email_with_attachment
        send_email_with_attachment(sender_email, password, receiver_email, subject, body)
        
        # Attendre 24 heures avant la prochaine mise à jour
        print("Attente de 24 heures avant la prochaine mise à jour...")
        time.sleep(update_frequency)  # 24 heures en secondes

# Configuration pour l'email
sender_email = 'cryptoforecast2@gmail.com'
password = 'v to e e y s d d h v s u a x l'  # Assurez-vous de ne pas partager votre mot de passe en clair dans un fichier Python
receiver_email = 'essohlath95@gmail.com'
subject = 'Prévisions des prix'
body = """
Bonjour,

Veuillez trouver ci-joint les prévisions des prix de l’Ethereum USD sur les 10 prochains jours.

Cordialement,
Lath
"""

if __name__ == "__main__":
    fonction()
