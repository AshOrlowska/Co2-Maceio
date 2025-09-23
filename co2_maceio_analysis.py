#Projeto Meteorologia + Dados
#Autor: Ash A. Orłowska

import pandas as pd, numpy as np, matplotlib.pyplot as plt
from scipy.stats import linregress

# Período de 2010 a 2025
anos = np.arange(2010, 2026)

# Gerando dados fictícios de emissões (toneladas)
np.random.seed(42)
emissoes = 500 + (anos-2010)*15 + np.random.normal(0,30,len(anos))

# Criando DataFrame
df = pd.DataFrame({"Ano": anos, "CO2_ton": emissoes}).set_index("Ano")

# Ajuste de tendência
slope, intercept, r, p, se = linregress(df.index, df["CO2_ton"])
tendencia = intercept + slope*df.index

# Plot
plt.plot(df.index, df["CO2_ton"], 'o-', label="Dados CO₂")
plt.plot(df.index, tendencia, 'r--', label=f"Tendência ({slope:.1f} ton/ano)")
plt.title("Emissões de CO₂ - Maceió (2010–2025)")
plt.xlabel("Ano"); plt.ylabel("CO₂ (ton)")
plt.legend(); plt.grid(); plt.show()

# Conclusão
print("AUMENTOU" if slope>0 else "DIMINUIU", f"(p={p:.4f})")
