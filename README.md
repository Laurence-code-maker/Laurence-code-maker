---

DOCUMENTATION DU PROJET:Analyse et prévision des prix bas et élevés de l'Ethereum en USD par la modélisation ARIMA/SARIMA
SOURCE DES CODES : Python
DATE: 02/04/2024
---

# Table des matières


* `Description du Projet`
* `Prérequis et Guide d'Installation`
* `Utilisation de Outil`
* `Fonctionalités Détaillées des Algorithmes de Prédiction de l'Ethereum USD`
* `Fonctionnement des scripts `
* `Ouverture du Projet`

# Description du projet


Notre projet en Techniques de Programmation vise à analyser et prédire les fluctuations des prix de l'Ethereum en USD (ETH-USD), une cryptomonnaie majeure sur les marchés financiers. À l'aide de techniques d'automatisation pour la collecte de données, ainsi que de la modélisation ARIMA/SARIMA, nous avons relevé le défi de concevoir un outil automatisé. Cet outil effectue préalablement la collecte et la visualisation des données, la décomposition de la série temporelle, et la récupération des prix nécessaires à la prévision. Par la suite, il génère un modèle automatique capable de sélectionner le modèle approprié, en tenant compte ou non des saisons (ARIMA ou SARIMA), selon les variations observées dans les données. Pour parfaire ce travail, l'outil convertit automatiquement les résultats au format PDF, qu'il envoie à des prospects potentiels toutes les 24 heures. L'objectif principal est de fournir des informations précieuses et rentables aux investisseurs en bourse ainsi qu'aux analystes financiers.
>**Note**: Nous avons opté pour les prix bas et élevés de l'Ethereum pour effectuer nos prédictions ; cependant, bien d'autres alternatives restent également pertinentes.

## Prérequis et Guide d'Installation

Cette section expose les procédures nécessaires pour installer et configurer le projet sur votre machine locale.
### Prérequis

Avant d'entamer le processus d'installation, veuillez vous assurer de disposer des outils et des logiciels suivants:
* Python 
* Git
>**Note:** 
Nous avons utilisé le langage Python avec l'éditeur Visual Studio Code dans le cadre de ce projet.

### Clonage du Dépôt
Afin d'obtenir une copie du projet, clonez le dépôt GitHub sur votre machine locale en copiant le code suivant.

```python
git clone <URL_du_dépôt>
```
Remplacez <URL_du_dépôt> par l'URL de la page de dépôt que vous avez precedément copié

### Installation des Dépendances

Avant de procéder à la prédiction, veuillez installer toutes les bibliothèques listées dans le fichier requirements.txt dans un environnement virtuel. Pour votre projet, vous pouvez utiliser la commande suivante dans le terminal :

```python
pip install -r requirements.txt
```

# Utilisation de Outil

Pour utiliser l'outil de prédiction, il vous suffit d'exécuter le fichier principal (MAIN.py) qui procède automatiquement à la collecte, à la visualisation, à l'extraction des prix bas et élevés, à la création du modèle automatique, à la prédiction des prix et à l'envoi des prédictions par e-mail au format PDF
>**Note:** 
Veuillez changer le mail du receveur afin d'être  sûr de recevoir le mail!

# Fonctionalités Détaillées des Algorithmes de Prédiction de l'Ethereum USD

## Récupération des Données Brutes
Ce bloc comprend le code nécessaire pour récupérer les données historiques de l'Ethereum en USD depuis Yahoo Finance. Il utilise la bibliothèque yfinance pour extraire les données souhaitées dans un format approprié pour une analyse ultérieure.
>**Note:** 
Les données de yfinance sont actualisées tous les jours ; cependant, le modèle de prédiction que nous proposons est un modèle dynamique qui prend en compte les tendances, les cycles, les saisons et d'autres structures temporelles présentes dans les données.

#### Implémentation

* Importation des bibliothèques nécessaires, y compris numpy, pandas et yfinance.
```python
from datetime import date 
from datetime timedelta 
import numpy as np  
import pandas as pd  
import yfinance as yf  
```
* Configuration des paramètres d'affichage pour une meilleure visualisation des données.

```python
import matplotlib  
import warnings  
warnings.filterwarnings("ignore")  
plt.style.use('fivethirtyeight')  
matplotlib.rcParams['axes.labelsize'] = 
matplotlib.rcParams['xtick.labelsize'] = 
matplotlib.rcParams['ytick.labelsize'] = 
matplotlib.rcParams['text.color'] = 'k' 

```

* Définition des dates de début et de fin pour la récupération des données.

```python 
today = date.today()
    end_date = today.strftime("%Y-%m-%d")
    start_date = (date.today() - timedelta(days=120)).strftime("%Y-%m-%d")

```
* Téléchargement des données historiques sur l'ETH-USD depuis Yahoo Finance.

```python
    data = yf.download('ETH-USD', start=start_date, end=end_date, progress=False)
```
* Réorganisation des données pour ne conserver que les colonnes pertinentes
```python
    data = data.reset_index()[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
```
* Affichage des premières lignes des données réorganisées
```python
    print("\nLes premières lignes des données réorganisées :")
    print(data.head())
```
>**Note:** 
Assurez-vous d'avoir installé les bibliothèques nécessaires avant d'exécuter ce bloc de code. Vous pouvez spécifier la période de récupération des données en ajustant les paramètres de date selon vos besoins..

## Récupération des Données Brutes
Ce bloc met en œuvre des techniques de visualisation pour explorer et comprendre les données récupérées. Il génère des graphiques en chandeliers, des histogrammes et des graphiques de volatilité pour les prix élevés (High) et bas (Low) de l'Ethereum en USD.
#### Implémentation
>**Note:** 
Veuillez importer au prealable les des bibliothèques de visualisation, notamment matplotlib, seaborn et Plotly.
```python
import seaborn as sns  données
import matplotlib.pyplot as plt  
import matplotlib
import plotly.graph_objects as go
```
#### Seaborn (sns): 
Pour des visualisations statistiques avancées, basées sur Matplotlib. Utilisées pour des graphiques plus esthétiques et complexes avec moins de code.

#### Matplotlib (plt): 
Module de base pour la visualisation de données en Python, offrant un contrôle complet pour créer des graphiques statiques, animés et interactifs.

#### Plotly (go): 
Outil pour des visualisations interactives et de haute qualité qui peuvent être utilisées dans des applications web.

* Création de graphiques en chandelier pour représenter les prix d'ouverture, de clôture, les plus hauts et les plus bas

```python
figure = go.Figure(data=[go.Candlestick(x=data["Date"],
                                        open=data["Open"],
                                        high=data["High"],
                                        low=data["Low"],
                                        close=data["Close"])])


figure.update_layout(title="Ethereum USD (ETH-USD) Price Analysis",
                     xaxis_rangeslider_visible=False)


figure.show()
```
#### go.Figure(): 
Crée une nouvelle figure pour le graphique.

#### data=[go.Candlestick(...)]: 
Définit les données du graphique sous forme d'un graphique en chandelier.

Les paramètres x, open, high, low, close sont passés à go.Candlestick, où : x représente la date; open est le prix à l'ouverture; high est le prix le plus haut atteint; low est le prix le plus bas atteint; close est le prix à la clôture.

Ces données sont extraites d'un dataframe data préalablement défini, qui doit contenir ces colonnes spécifiques.

* Génération d'histogrammes pour analyser la distribution des prix hauts (High) et bas (Low)

```python
plt.figure(figsize=(10, 6))
sns.histplot(data["High"], kde=True, color='blue')
plt.title("Distribution des prix High d'Ethereum (ETH-USD)")
plt.xlabel("Prix High")
plt.ylabel("Densité")
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data["Low"], kde=True, color='red')
plt.title("Distribution des prix Low d'Ethereum (ETH-USD)")
plt.xlabel("Prix Low")
plt.ylabel("Densité")
plt.show()
```
#### plt.figure(figsize=(10, 6)):
 Définit la taille du graphique.

#### sns.histplot(...): 
Crée un histogramme des prix "High" avec une courbe de densité.

#### plt.title(...): 
Ajoute un titre au graphique.

#### plt.xlabel(...), plt.ylabel(...): 
Nomment les axes X (Prix High) et Y (Densité).

#### plt.show(): 
Affiche le graphique.

* Tracé de la volatilité des prix hauts (High) et bas (Low) au fil du temps

```python
plt.figure(figsize=(10, 6))
plt.plot(data["Date"], data["High"], color='green', label="Prix High")
plt.title("Volatilité des prix hauts d'Ethereum (ETH-USD)")
plt.xlabel("Date")
plt.ylabel("Prix High")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(data["Date"], data["Low"], color='orange', label="Prix Low")
plt.title("Volatilité des prix bas d'Ethereum (ETH-USD)")
plt.xlabel("Date")
plt.ylabel("Prix Low")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()
```

#### plt.plot(data["Date"], data["High"], color='green', label="Prix High"): 
Trace un graphique de ligne des prix "High" par rapport à la date, avec des points verts et une légende "Prix High"

#### plt.xlabel("Date"), plt.ylabel("Prix High"): 
Nomment les axes X (Date) et Y (Prix High)

#### plt.xticks(rotation=45): 
Rotation de 45 degrés pour les étiquettes de l'axe des x (dates) pour une meilleure lisibilité

#### plt.legend(): 
Affiche la légende sur le graphique

#### plt.grid(True): 
Affiche une grille sur le graphique

* Décomposition des séries temporelles pour les prix High et Low

```python
from statsmodels.tsa.seasonal import seasonal_decompose

decomposition_high = seasonal_decompose(data["High"], model='additive', period=7)
trend_high = decomposition_high.trend
seasonal_high = decomposition_high.seasonal
residual_high = decomposition_high.resid

decomposition_low = seasonal_decompose(data["Low"], model='additive', period=7)
trend_low = decomposition_low.trend
seasonal_low = decomposition_low.seasonal
residual_low = decomposition_low.resid
```
#### from statsmodels.tsa.seasonal import seasonal_decompose: 
Importe la fonction seasonal_decompose du module seasonal de statsmodels.tsa.

Décomposition de la série temporelle pour les prix High: 
#### decomposition_high = seasonal_decompose(data["High"], model='additive', period=7): 
Décompose la série temporelle des prix "High" en tendance, saisonnalité et résidus, en utilisant un modèle additif avec une période de 7 jours.

#### trend_high = decomposition_high.trend: 
Obtient la tendance de la décomposition.

#### seasonal_high = decomposition_high.seasonal: 
Obtient la composante saisonnière de la décomposition.

#### residual_high = decomposition_high.resid: 
Obtient les résidus de la décomposition.

* Visualisation des composantes des séries temporelles pour les prix High et Low

```python

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
```

#### plt.subplot(421), plt.subplot(423), plt.subplot(425): 
Crée des sous-graphiques (subplot) dans une grille 4x2. Les nombres dans la fonction subplot spécifient le nombre de lignes, le nombre de colonnes et l'index de chaque subplot.

#### plt.plot(data.index, trend_high, label='Trend', color='green'), plt.plot(data.index, seasonal_high, label='Seasonality', color='red'), plt.plot(data.index, residual_high, label='Residuals', color='purple'): 
Trace les tendances, la saisonnalité et les résidus respectivement.

#### plt.legend(loc='upper left'): 
Ajoute une légende dans le coin supérieur gauche de chaque subplot.

#### plt.title('Trend (High)'), plt.title('Seasonality (High)'), plt.title('Residuals (High)'): 
Ajoute un titre à chaque subplot.

#### plt.tight_layout(): 
Ajuste automatiquement la disposition des subplots pour éviter les chevauchements.
>**Note:** 
Exécutez ce bloc de code pour visualiser les données historiques de l'Ethereum USD sous forme de graphiques interactifs et d'histogrammes. Vous pouvez ajuster les paramètres de visualisation selon vos préférences.

## Récupération des prix pour les prévisions
Ce bloc prépare les données récupérées pour la modélisation ARIMA/SARIMA. Il extrait les séries temporelles des prix hauts (High) et bas (Low) de l'Ethereum USD pour une analyse de prévision ultérieure.

### Implémentation

* Extraction des séries temporelles des prix hauts (High) et bas (Low) de l'Ethereum USD.
* Conversion des données en séries temporelles pour la modélisation ARIMA/SARIMA.

```python
crypto_prices_high = data.set_index('Date')['High']
crypto_prices_low = data.set_index('Date')['Low']

print(crypto_prices_high.head())
print(crypto_prices_low.head())
```

#### crypto_prices_high = data.set_index('Date')['High'] : 
Crée une série temporelle des prix "High" de la crypto-monnaie en utilisant la colonne 'Date' comme index du DataFrame data, puis en sélectionnant la colonne 'High'.

#### crypto_prices_low = data.set_index('Date')['Low'] : 
Crée une série temporelle des prix "Low" de la crypto-monnaie de manière similaire, en utilisant la colonne 'Date' comme index du DataFrame data, puis en sélectionnant la colonne 'Low'.

#### print(crypto_prices_high.head()) : 
Affiche les cinq premières lignes de la série temporelle des prix "High".

#### print(crypto_prices_low.head()) : 
Affiche les cinq premières lignes de la série temporelle des prix "Low".
>**Note:** 
Exécutez ce bloc de code pour préparer les données nécessaires à la modélisation ARIMA/SARIMA des prix hauts (High) et bas (Low) de l'Ethereum USD.

## Création automatique des modèles SARIMA ou ARIMA

### Description
Ce bloc automatise la création des modèles SARIMA pour les prix hauts (High) et bas (Low) de l'Ethereum USD en utilisant la bibliothèque pmdarima. Il sélectionne les paramètres optimaux du modèle pour générer des prévisions précises.
### Implémentation
* Utilisation de la bibliothèque pmdarima pour créer automatiquement les modèles SARIMA.

```python
from pmdarima import auto_arima
```
* Ajustement des modèles aux données historiques pour générer des prévisions
```python
print("\nCréation du modèle SARIMA automatique pour les prix hauts (High)...")
model_auto_high = auto_arima(crypto_prices_high, seasonal=True, m=12, trace=True)
print("\nRésumé du modèle SARIMA pour les prix hauts (High):\n", model_auto_high.summary())

print("\nCréation du modèle SARIMA automatique pour les prix bas (Low)...")
model_auto_low = auto_arima(crypto_prices_low, seasonal=True, m=12, trace=True)
print("\nRésumé du modèle SARIMA pour les prix bas (Low):\n", model_auto_low.summary())
```

#### model_auto_high = auto_arima(crypto_prices_high, seasonal=True, m=12, trace=True) : 
Crée un modèle SARIMA automatique pour les prix "High" de la crypto-monnaie en utilisant la fonction auto_arima. Les paramètres spécifiés sont :

#### crypto_prices_high : 
La série temporelle des prix "High".

#### seasonal=True : 
Active la composante saisonnière du modèle.

#### m=12 : 
Spécifie la période saisonnière, ici 12 (mensuelle).

#### trace=True : 
Affiche les informations de traçage pendant l'ajustement du modèle.

**print("\nRésumé du modèle SARIMA pour les prix hauts (High):\n",

#### model_auto_high.summary()) : 
Affiche un résumé du modèle SARIMA ajusté pour les prix "High" de la crypto-monnaie. Ce résumé comprend des informations importantes telles que les paramètres du modèle, les statistiques de performance et les diagnostics.
>**Note:** 
Exécutez ce bloc de code pour créer automatiquement les modèles SARIMA pour les prix hauts (High) et bas (Low) de l'Ethereum USD.

## Prédictions sur toute la période (d'analyse) et les 10 Prochains Jours
### Description
Ce bloc génère des prévisions pour les prix hauts (High) et bas (Low) de l'Ethereum USD sur toute la période observée et pour les 10 prochains jours en utilisant les modèles ARIMA/SARIMA précédemment créés.
### Implémentation

* Génération des prévisions pour les prix hauts (High) et bas (Low) de l'Ethereum USD.

```python
    predictions_sarima_high, conf_int_high = model_auto_high.predict_in_sample(return_conf_int=True)
    predictions_sarima_low, conf_int_low = model_auto_low.predict_in_sample(return_conf_int=True)

    all_predictions_sarima_high = pd.concat([pd.Series(predictions_sarima_high, index=crypto_prices_high.index)], axis=0)
    all_predictions_sarima_low = pd.concat([pd.Series(predictions_sarima_low, index=crypto_prices_low.index)], axis=0)

    forecast_sarima_high = model_auto_high.predict(start=len(crypto_prices_high), end=len(crypto_prices_high) + 10)
    forecast_sarima_low = model_auto_low.predict(start=len(crypto_prices_low), end=len(crypto_prices_low) + 10)

    index_future_dates = pd.date_range(start=crypto_prices_high.index[-1], periods=11, freq='D')[1:]

    forecast_sarima_high_df = pd.DataFrame(forecast_sarima_high, index=index_future_dates, columns=['Predictions (High)'])
    forecast_sarima_low_df = pd.DataFrame(forecast_sarima_low, index=index_future_dates, columns=['Predictions (Low)'])
```

#### predictions_sarima_high, conf_int_high = model_auto_high.predict_in_sample(return_conf_int=True) : 
Obtient les prédictions dans l'échantillon pour les prix "High" en utilisant le modèle SARIMA automatique ajusté, ainsi que les intervalles de confiance associés.

#### predictions_sarima_low, conf_int_low = model_auto_low.predict_in_sample(return_conf_int=True) : 
Obtient les prédictions dans l'échantillon pour les prix "Low" de manière similaire.

#### all_predictions_sarima_high = pd.concat([pd.Series(predictions_sarima_high, index=crypto_prices_high.index)], axis=0) : 
Combine les prédictions SARIMA pour les prix "High" avec leur index de temps correspondant.

#### all_predictions_sarima_low = pd.concat([pd.Series(predictions_sarima_low, index=crypto_prices_low.index)], axis=0) : 
Combine les prédictions SARIMA pour les prix "Low" de manière similaire.

#### forecast_sarima_high = model_auto_high.predict(start=len(crypto_prices_high), end=len(crypto_prices_high) + 10) : 
Effectue une prévision future des prix "High" en utilisant le modèle SARIMA automatique, pour les 10 périodes suivantes après la fin des données historiques.

#### forecast_sarima_low = model_auto_low.predict(start=len(crypto_prices_low), end=len(crypto_prices_low) + 10) : 
Effectue une prévision future similaire pour les prix "Low".

#### index_future_dates = pd.date_range(start=crypto_prices_high.index[-1], periods=11, freq='D')[1:] : 
Crée un index de dates pour les prévisions futures, commençant par la date suivant la dernière date dans les données historiques.

#### forecast_sarima_high_df = pd.DataFrame(forecast_sarima_high, index=index_future_dates, columns=['Predictions (High)']) : 
Crée un DataFrame contenant les prédictions futures pour les prix "High" avec leurs dates correspondantes.

#### forecast_sarima_low_df = pd.DataFrame(forecast_sarima_low, index=index_future_dates, columns=['Predictions (Low)']) : 
Crée un DataFrame similaire pour les prédictions futures des prix "Low".

* Visualisation des prévisions à l'aide de graphiques et de données numériques.

```python
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
```
>**Note:** 
Exécutez ce bloc de code pour générer des prévisions précises des prix hauts (High) et bas (Low) de l'Ethereum USD sur les 10 prochains jours.

## Création du PDF Comportant les Résultats Graphiques et Numériques des Prédictions (Intervalle

### Description
Ce bloc crée un fichier PDF contenant des graphiques des prévisions pour les prix hauts (High) et bas (Low) de l'Ethereum USD sur les 10 prochains jours, accompagnés de données numériques correspondantes.

### Implémentation
*Utilisation de la bibliothèque FPDF pour créer le fichier PDF.

```python
from fpdf import FPDF
import matplotlib.pyplot as plt
```
* Ajout des graphiques des prévisions et des données numériques au fichier PDF.

```python

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=16)

    pdf.cell(200, 10, txt="Prévisions des prix High et Low pour les 10 prochains jours (ETH-USD)", ln=True, align='C')
    pdf.ln(10)

    plt.figure(figsize=(12, 6))
    plt.plot(crypto_prices_high, label='Prix observés (High)', color='blue')
    plt.plot(all_predictions_sarima_high, label='Prédictions (High)', color='red')
    plt.plot(forecast_sarima_high_df, label='Prédictions pour les 10 
    prochains jours (High)', color='green', linestyle='--')
    plt.title('Prédictions du modèle ARIMA pour les prix High')
    plt.legend()
    plt.savefig('predictions_high.png')  
    plt.close()
    
    plt.figure(figsize=(12, 6))
    plt.plot(crypto_prices_low, label='Prix observés (Low)', color='blue')
    plt.plot(all_predictions_sarima_low, label='Prédictions (Low)', color='red')
    plt.plot(forecast_sarima_low_df, label='Prédictions pour les 10 prochains jours (Low)', color='green', linestyle='--')
    plt.title('Prédictions du modèle ARIMA pour les prix Low')
    plt.legend()
    plt.savefig('predictions_low.png')  
    plt.close()
    
    pdf.image('predictions_high.png', x=10, y=pdf.get_y(), w=180)
    pdf.ln(100)
    pdf.image('predictions_low.png', x=10, y=pdf.get_y(), w=180)
    pdf.ln(100)
    
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Valeurs numériques des prédictions pour les prix [Low ; High] :", ln=True, align='L')
    pdf.ln(5)
    
    for date, high_price, low_price in zip(forecast_sarima_high_df.index, forecast_sarima_high_df['Predictions (High)'], forecast_sarima_low_df['Predictions (Low)']):
        pdf.cell(200, 10, txt=f"{date.strftime('%Y-%m-%d')} : [{low_price}; {high_price}]", ln=True)
        
    pdf.output("predictions.pdf")
```

#### pdf.cell(200, 10, txt="Prévisions des prix High et Low pour les 10 prochains jours (ETH-USD)", ln=True, align='C') : 
Ajoute un titre centré au PDF indiquant les prévisions des prix High et Low pour les 10 prochains jours.

#### pdf.ln(10) : 
Ajoute un saut de ligne de 10 unités après le titre. Ajout des images au PDF :

#### pdf.image('predictions_high.png', x=10, y=pdf.get_y(), w=180) : 
Ajoute l'image représentant les prévisions des prix High au PDF, avec une largeur de 180 unités.

#### pdf.ln(100) : 
Ajoute un saut de ligne de 100 unités après l'image des prévisions High.

#### pdf.image('predictions_low.png', x=10, y=pdf.get_y(), w=180) : 
Ajoute l'image représentant les prévisions des prix Low au PDF, avec une largeur de 180 unités.

#### pdf.ln(100) : 
Ajoute un saut de ligne de 100 unités après l'image des prévisions Low.

#### pdf.set_font("Arial", size=12) : 
Définit la police et la taille de la police pour le texte des valeurs numériques.

#### pdf.cell(200, 10, txt="Valeurs numériques des prédictions pour les prix [Low ; High] :", ln=True, align='L') : 
Ajoute une ligne de texte indiquant le début des valeurs numériques des prédictions. pdf.ln(5) : Ajoute un saut de ligne de 5 unités après le texte.

#### Boucle for : for date, high_price, low_price in zip(forecast_sarima_high_df.index, forecast_sarima_high_df['Predictions (High)'], forecast_sarima_low_df['Predictions (Low)']): : 
Parcourt simultanément les index et les valeurs des prédictions High et Low.

#### pdf.cell(200, 10, txt=f"{date.strftime('%Y-%m-%d')} : [{low_price}; {high_price}]", ln=True) : 
Ajoute une ligne de texte au PDF pour chaque date avec les prédictions High et Low correspondantes.

>**Note:** 
Exécutez ce bloc de code pour créer un fichier PDF contenant des graphiques et des données numériques des prévisions des prix hauts (High) et bas (Low) de l'Ethereum USD sur les 10 prochains jours.

## Envoie des Prédiction au format PDF par Mail

###Description

permet d'envoyer un email avec une pièce jointe contenant les prévisions des prix de l’Ethereum USD sur les 10 prochains jours. Les prévisions sont générées et stockées dans un fichier PDF ci-dessus.
```python
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
```
### Implémentation

* Création de l'objet MIMEMultipart: Cela crée un objet pour représenter un message MIME multipart, qui est utilisé pour les emails avec pièces jointes.

* Définition des en-têtes du message: Les champs comme "From", "To" et "Subject" sont définis.

* Corps du message: Le corps de l'email est attaché au message.

* Pièce jointe : fichier PDF : Le fichier PDF contenant les prévisions est ouvert en mode lecture binaire et attaché au message.

* Encodage de la pièce jointe : La pièce jointe est encodée en base64 pour être ajoutée au message.

* Ajout de l'en-tête de la pièce jointe : L'en-tête Content-Disposition est ajouté pour spécifier le nom de la pièce jointe.

* Envoi du courriel : Une connexion SSL est établie avec le serveur SMTP de Gmail, puis le message est envoyé avec les informations d'identification du compte expéditeur.

```python
sender_email = 'cryptoforecast2@gmail.com'
password = 'v to e e y s d d h v s u a x l'
receiver_email = 'essohlath95@gmail.com'
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Prévisions des prix"

body = """
Bonjour,

Veuillez trouver ci-joint les prévisions des prix de l’Ethereum USD sur les 10 prochains jours.

Cordialement,
Lath
"""
message.attach(MIMEText(body, "plain"))

filename = "predictions.pdf"
with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)

part.add_header(
    "Content-Disposition",
    "attachment; filename=predictions.pdf",
)
message.attach(part)

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Email des prévisions envoyé avec succès !")
```
>**Note:** 
Exécutez ce bloc de code pour envoyer automatiquement le fichier PDF des prévisions par e-mail à une adresse spécifiée.

## Boucle finale 
Ce bloc de code est conçu pour automatiser l'exécution périodique de toutes les tâches precedentes. Il utilise la bibliothèque time pour planifier l'exécution du code toutes les 24 heures.
```python
import time
update_frequency = 86400  
while True:
    try:
    time.sleep(update_frequency)
```

#### import time: 
Cette ligne importe le module time, qui fournit diverses fonctionnalités liées au temps, y compris la fonction sleep() utilisée plus loin dans le code.

#### update_frequency = 86400: 
Cette ligne définit une variable update_frequency à 86400, ce qui correspond à 24 heures en secondes. Cela indique la fréquence à laquelle le programme sera mis à jour.

#### while True:: 
Cette ligne crée une boucle infinie, ce qui signifie que le code à l'intérieur de cette boucle sera exécuté de manière répétée indéfiniment, à moins qu'il ne rencontre une instruction de sortie (comme un break ou une exception non gérée).

#### try:: 
Cette ligne commence un bloc d'essai, qui est utilisé pour gérer les exceptions potentielles qui pourraient se produire lors de l'exécution du code à l'intérieur de la boucle while.

#### time.sleep(update_frequency): 
Cette ligne met le programme en pause pendant la durée spécifiée par update_frequency. Dans ce cas, il met le programme en pause pendant 24 heures (86400 secondes). Cela garantit que le programme attendra la durée spécifiée avant de continuer à s'exécuter.

Assurez-vous d'insérer tout le code, y compris les importations, à l'intérieur de la boucle try-except et d'indenter correctement chaque ligne de code à l'intérieur de la boucle while. Cela garantira que le programme fonctionne comme prévu en mettant à jour les prévisions toutes les 24 heures et en gérant les erreurs de manière appropriée.

# Fonctionnement des scripts 

* ##### Fichier (DATA.py): Récupération et visualisation des données.


* ##### Fichier (ETH_PRICES.py): Extraction des prix low et hight pour les prédictions.

* ##### Fichier (AUTOMATIC_MODEL.py): Création du modèle SARIMA/ARIMA automatique

* ##### Fichier (FORCAST.py): Prévision sur les dix prochains jours

* ##### Fichier (PDF.py): Création du PDF 

* ##### Fichier (EMAIL.py): Envoie du mail aux futurs prospects 

* ##### Fichier (MAIN.py): Script final du projet englobant toutes les fonctions prédefinies.


# Ouverture du Projet
Notre projet a pour objectif l'automatisation des prévisions de prix de l'Ethereum USD en utilisant des modèles ARIMA/SARIMA. En combinant des techniques d'analyse de séries temporelles, de visualisation de données et de génération de rapports automatisés, nous avons créé un outil robuste destiné aux investisseurs et aux analystes financiers.

Ce README fournit une documentation complète sur chaque aspect du projet, depuis la récupération des données brutes jusqu'à l'envoi des prévisions par e-mail. Des explications détaillées sur le code et des exemples d'utilisation ont été inclus pour faciliter la compréhension et l'utilisation de l'outil.

Les résultats obtenus ont démontré l'efficacité des modèles ARIMA/SARIMA dans la prédiction des prix de l'Ethereum USD. Les graphiques interactifs, les histogrammes et les séries temporelles décomposées ont permis une analyse approfondie des données historiques. De plus, les prévisions précises pour les 10 prochains jours ont fourni des informations cruciales pour la prise de décision.

En générant un fichier PDF contenant à la fois des visualisations graphiques et des données numériques des prévisions, nous avons offert aux utilisateurs un moyen pratique de consulter et d'analyser les résultats de manière professionnelle.

Ce projet a démontré l'importance de la programmation technique dans le domaine de la finance et des investissements, en permettant l'automatisation des tâches répétitives et la prise de décisions éclairées basées sur des analyses approfondies des données. Néanmoins, nous avons rencontré plusieurs difficultés dans la conception de notre outil. Nous étions à la base partis sur un modèle GARCH qui a pour objectif de modéliser et de prévoir la volatilité des séries temporelles financières. Toutefois, nous avons obtenu des prédictions qui ne reflétaient pas la réalité selon nous. En raison de la présence de saisonnalités, nous avons donc décidé de faire les prédictions avec un modèle SARIMA, qui est un modèle plus général utilisé pour la modélisation et la prévision des valeurs des séries temporelles avec prise en compte de la saisonnalité quand il y en a.

