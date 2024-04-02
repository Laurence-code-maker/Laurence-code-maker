from FORCAST import faire_predictions
from fpdf import FPDF
import matplotlib.pyplot as plt
import pandas as pd

from fpdf import FPDF

def create_predictions_pdf(crypto_prices_high, all_predictions_sarima_high, forecast_sarima_high_df, crypto_prices_low, all_predictions_sarima_low, forecast_sarima_low_df):
    # Création d'un objet FPDF
    pdf = FPDF()
    
    # Ajout d'une page au PDF
    pdf.add_page()
    pdf.set_font("Arial", size=16)
    
    # Ajout du titre
    pdf.cell(200, 10, txt="Prévisions des prix High et Low pour les 10 prochains jours (ETH-USD)", ln=True, align='C')
    pdf.ln(10)   
    
    # Sauvegarde des graphiques dans des fichiers temporaires
    plt.figure(figsize=(12, 6))
    plt.plot(crypto_prices_high, label='Prix observés (High)', color='blue')
    plt.plot(all_predictions_sarima_high, label='Prédictions (High)', color='red')
    plt.plot(forecast_sarima_high_df, label='Prédictions pour les 10 prochains jours (High)', color='green', linestyle='--')
    plt.title('Prédictions du modèle ARIMA pour les prix High')
    plt.legend()
    plt.savefig('predictions_high.png')  # Sauvegarder le graphique des prédictions High
    plt.close()
    
    plt.figure(figsize=(12, 6))
    plt.plot(crypto_prices_low, label='Prix observés (Low)', color='blue')
    plt.plot(all_predictions_sarima_low, label='Prédictions (Low)', color='red')
    plt.plot(forecast_sarima_low_df, label='Prédictions pour les 10 prochains jours (Low)', color='green', linestyle='--')
    plt.title('Prédictions du modèle ARIMA pour les prix Low')
    plt.legend()
    plt.savefig('predictions_low.png')  # Sauvegarder le graphique des prédictions Low
    plt.close()
    
    # Ajout des images au PDF
    pdf.image('predictions_high.png', x=10, y=pdf.get_y(), w=180)
    pdf.ln(100)
    pdf.image('predictions_low.png', x=10, y=pdf.get_y(), w=180)
    pdf.ln(100)
    
    # Ajout des valeurs numériques au PDF
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Valeurs numériques des prédictions pour les prix [Low ; High] :", ln=True, align='L')
    pdf.ln(5)
    
    for date, high_price, low_price in zip(forecast_sarima_high_df.index, forecast_sarima_high_df['Predictions (High)'], forecast_sarima_low_df['Predictions (Low)']):
        pdf.cell(200, 10, txt=f"{date.strftime('%Y-%m-%d')} : [{low_price}; {high_price}]", ln=True)
        
    # Enregistrement du PDF
    pdf.output("predictions.pdf")
 
   



