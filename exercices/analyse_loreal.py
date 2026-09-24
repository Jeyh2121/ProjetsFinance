import pandas as pd
import yfinance as yf

# Définissons une entreprise (ex: L'Oréal sur Euronext Paris avec le ticker OR.PA, ou Apple AAPL)
symbole = "OR.PA"
entreprise = yf.Ticker(symbole)

print(f"--- EXTRACTION DES ÉTATS FINANCIERS : {symbole} ---")

# 1. Récupérer le Compte de Résultat annuel (Financials)
compte_resultat = entreprise.financials
print("\n[1] Aperçu du Compte de Résultat (Chiffre d'affaires, Résultat net) :")
# On affiche les lignes clés si elles sont présentes
postes_cles = ['Total Revenue', 'Net Income', 'Operating Income']
# Filtre pour n'afficher que les lignes qui existent dans le tableau
disponibles = [p for p in postes_cles if p in compte_resultat.index]
print(compte_resultat.loc[disponibles].head())

# 2. Récupérer le Bilan (Balance Sheet)
bilan = entreprise.balance_sheet
print("\n[2] Aperçu du Bilan (Actifs / Passifs) :")
print(bilan.head(3))

# Optionnel : Exporter tout cela proprement dans un fichier Excel multi-onglets
nom_excel = f"etats_financiers_{symbole}.xlsx"
with pd.ExcelWriter(nom_excel, engine='openpyxl') as writer:
    compte_resultat.to_excel(writer, sheet_name="Compte de Resultat")
    bilan.to_excel(writer, sheet_name="Bilan")

print(f"\n[Succès] Les états financiers complsets ont été exportés dans '{nom_excel}' !")