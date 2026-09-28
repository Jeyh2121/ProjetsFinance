import yfinance as yf

# Définissons l'entreprise (ex: LVMH avec le ticker MC.PA)
ticker = "MC.PA"
entreprise = yf.Ticker(ticker)

# Récupérer le Tableau des Flux de Trésorerie (Cash Flow Statement)
cash_flow = entreprise.cashflow

# Extraire les valeurs clés de l'année la plus récente (colonne 0)
# Note : Dans yfinance, le CapEx est souvent affiché en valeur négative (car c'est une sortie d'argent)
ocf = cash_flow.loc['Operating Cash Flow'].iloc[0]
capex = cash_flow.loc['Capital Expenditure'].iloc[0] 

# Calcul du FCF (On additionne car le CapEx est déjà négatif)
fcf = ocf + capex

print(f"--- ANALYSE DU FREE CASH FLOW : {ticker} ---")
print(f"Flux de Trésorerie Opérationnel (Cash rentrant) : {ocf:,.0f} €")
print(f"Dépenses d'Investissement (CapEx, Cash sortant) : {capex:,.0f} €")
print("-" * 40)
print(f"Free Cash Flow (Cash Libre) : {fcf:,.0f} €")

if fcf > 0:
    print("\nDiagnostic : Excellente nouvelle, l'entreprise génère du cash libre !")
else:
    print("\nDiagnostic : L'entreprise brûle du cash. Il faut analyser si c'est pour une croissance agressive ou si c'est un signal d'alarme.")