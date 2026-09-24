import pandas as pd
import yfinance as yf

# Télécharge l'historique de l'action Apple (AAPL) sur les 5 derniers jours
print("Téléchargement des données boursières...")
apple = yf.Ticker("AAPL")
historique = apple.history(period="5d")

# Affiche le tableau des cours grâce à pandas
print(historique)