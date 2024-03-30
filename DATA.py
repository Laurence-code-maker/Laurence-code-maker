from datetime import date, timedelta
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import warnings
import plotly.graph_objects as go
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

def get_eth_data():
    # Configuration des paramètres d'affichage
    warnings.filterwarnings("ignore")
    plt.style.use('fivethirtyeight')
    matplotlib.rcParams['axes.labelsize'] = 14
    matplotlib.rcParams['xtick.labelsize'] = 12
    matplotlib.rcParams['ytick.labelsize'] = 12
    matplotlib.rcParams['text.color'] = 'k'

    # Définition des dates de début et de fin pour la récupération des données
    today = date.today()
    end_date = today.strftime("%Y-%m-%d")
    start_date = (date.today() - timedelta(days=120)).strftime("%Y-%m-%d")

    # Téléchargement des données historiques sur l'ETH-USD depuis Yahoo Finance
    data = yf.download('ETH-USD', start=start_date, end=end_date, progress=False)

    # Réorganisation des données pour ne conserver que les colonnes pertinentes
    data = data.reset_index()[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]

    # Affichage des premières lignes des données réorganisées
    print("\nLes premières lignes des données réorganisées :")
    print(data.head())

    return data

def visualize_eth_data(data):
    # Visualisation des données
    # Création de la figure contenant le graphique en chandelier (Candlestick)
    figure = go.Figure(data=[go.Candlestick(x=data["Date"],
                                            open=data["Open"],
                                            high=data["High"],
                                            low=data["Low"],
                                            close=data["Close"])])
    
    # Mise à jour de la mise en page de la figure
    figure.update_layout(title="Ethereum USD (ETH-USD) Price Analysis",
                         xaxis_rangeslider_visible=False)

    # Affichage de la figure
    figure.show()

    # Analyse de la distribution des prix hauts (High)
    plt.figure(figsize=(10, 6))
    sns.histplot(data["High"], kde=True, color='blue')
    plt.title("Distribution des prix High d'Ethereum (ETH-USD)")
    plt.xlabel("Prix High")
    plt.ylabel("Densité")
    plt.show()

    # Analyse de la distribution des prix bas (Low)
    plt.figure(figsize=(10, 6))
    sns.histplot(data["Low"], kde=True, color='red')
    plt.title("Distribution des prix Low d'Ethereum (ETH-USD)")
    plt.xlabel("Prix Low")
    plt.ylabel("Densité")
    plt.show()

    # Analyse de la volatilité des prix hauts (High)
    plt.figure(figsize=(10, 6))
    plt.plot(data["Date"], data["High"], color='green', label="Prix High")
    plt.title("Volatilité des prix hauts d'Ethereum (ETH-USD)")
    plt.xlabel("Date")
    plt.ylabel("Prix High")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.show()

    # Analyse de la volatilité des prix bas (Low)
    plt.figure(figsize=(10, 6))
    plt.plot(data["Date"], data["Low"], color='orange', label="Prix Low")
    plt.title("Volatilité des prix bas d'Ethereum (ETH-USD)")
    plt.xlabel("Date")
    plt.ylabel("Prix Low")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.show()

def decompose_eth_data(data):
    # Décomposition de la série temporelle
    df = data.set_index('Date')
    # Décomposer la série temporelle pour les prix High
    decomposition_high = seasonal_decompose(data["High"], model='additive', period=7)
    trend_high = decomposition_high.trend
    seasonal_high = decomposition_high.seasonal
    residual_high = decomposition_high.resid
    
    # Décomposer la série temporelle pour les prix Low
    decomposition_low = seasonal_decompose(data["Low"], model='additive', period=7)
    trend_low = decomposition_low.trend
    seasonal_low = decomposition_low.seasonal
    residual_low = decomposition_low.resid

    # Affichage des composantes de la décomposition
    # Visualisation des composantes de la série temporelle pour les prix High
    plt.figure(figsize=(15, 10))
    plt.subplot(421)
    plt.plot(data.index, trend_high, label='Trend', color='green')
    plt.legend(loc='upper left')
    plt.title('Trend (High)')
    plt.subplot(423)
    plt.plot(data.index, seasonal_high, label='Seasonality', color='red')
    plt.legend(loc='upper left')
    plt.title('Seasonality (High)')
    plt.subplot(425)
    plt.plot(data.index, residual_high, label='Residuals', color='purple')
    plt.legend(loc='upper left')
    plt.title('Residuals (High)')
    plt.tight_layout()
    
    # Visualisation des composantes de la série temporelle pour les prix Low
    plt.figure(figsize=(15, 10))
    plt.subplot(422)
    plt.plot(data.index, trend_low, label='Trend', color='green')
    plt.legend(loc='upper left')
    plt.title('Trend (Low)')
    plt.subplot(424)
    plt.plot(data.index, seasonal_low, label='Seasonality', color='red')
    plt.legend(loc='upper left')
    plt.title('Seasonality (Low)')
    plt.subplot(426)
    plt.plot(data.index, residual_low, label='Residuals', color='purple')
    plt.legend(loc='upper left')
    plt.title('Residuals (Low)')
    plt.tight_layout()
    
    plt.show()

def main():
    # Récupération des données
    data = get_eth_data()
    
    # Visualisation des données
    visualize_eth_data(data)
    
    # Décomposition de la série temporelle
    decompose_eth_data(data)

# Exécution de la fonction principale
if __name__ == "__main__":
    main()





