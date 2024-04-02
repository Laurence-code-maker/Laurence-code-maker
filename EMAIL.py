
from PDF import create_predictions_pdf
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
    password = 'v to e e y s d d h v s u a x l'
    receiver_email = '*******@gmail.com'
    subject = 'Prévisions des prix'
    body = """
    Bonjour,

    Veuillez trouver ci-joint les prévisions des prix de l’Ethereum USD sur les 10 prochains jours.

    Cordialement,
    """
    send_email_with_attachment(sender_email, password, receiver_email, subject, body)
