

from PDF import create_predictions_pdf
from fpdf import FPDF
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email_with_attachment(sender_email, password, receiver_email, subject, body):

    # Création de l'objet MIMEMultipart
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Corps du message
    message.attach(MIMEText(body, "plain"))

    # Pièce jointe : fichier PDF
    filename = "predictions.pdf"
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encodage de la pièce jointe en base64
    encoders.encode_base64(part)

    # Ajout de l'en-tête de la pièce jointe
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    # Ajout de la pièce jointe au message
    message.attach(part)
    # Envoi du courriel
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email des prévisions envoyé avec succès !")

# Exécution
if __name__ == "__main__":
    sender_email = 'cryptoforecast2@gmail.com'
    password = ''
    receiver_email = ''
    subject = 'Prévisions des prix'
    body = """
    Bonjour,

    Veuillez trouver ci-joint les prévisions des prix de l’Ethereum USD sur les 10 prochains jours.

    Cordialement,
    Lath
    """
send_email_with_attachment(sender_email, password, receiver_email, subject, body)



import schedule
import time

def execute_functions():
    from ETH_PRICES import prepare_eth_data_for_forecasting
    from AUTOMATIC_MODEL import create_automatic_models
    from FORCAST import  faire_predictions
    from DATA import get_eth_data

    # Récupération des données
    data = get_eth_data()
    
    # Préparation des données pour les prévisions
    crypto_prices_high, crypto_prices_low = prepare_eth_data_for_forecasting()
    
    # Création des modèles automatiques
    model_auto_high, model_auto_low = create_automatic_models()
    
    # Faire les prédictions
    all_predictions_sarima_high, forecast_sarima_high_df, all_predictions_sarima_low, forecast_sarima_low_df = faire_predictions(model_auto_high, model_auto_low, crypto_prices_high, crypto_prices_low)
    
    # Création du PDF avec les prédictions
    create_predictions_pdf(crypto_prices_high, all_predictions_sarima_high, forecast_sarima_high_df, crypto_prices_low, all_predictions_sarima_low, forecast_sarima_low_df, pdf_filename)
    pdf_filename = "predictions.pdf"
    # Envoi de l'email avec le fichier PDF en pièce jointe
    sender_email = 'cryptoforecast2@gmail.com'
    password = 'v to e e y s d d h v s u a x l'
    receiver_email = 'essohlath95@gmail.com'
    subject = 'Prévisions des prix'
    body = """
    Bonjour,

    Veuillez trouver ci-joint les prévisions des prix de l’Ethereum USD sur les 10 prochains jours.

    Cordialement,
    Lath
    """
    send_email_with_attachment(sender_email, password, receiver_email, subject, body, pdf_filename)

# Planifier l'exécution des fonctions chaque 24 heures
schedule.every().day.at("00:00").do(execute_functions)

# Boucle principale pour exécuter la planification
while True:
    schedule.run_pending()
    time.sleep(1)
