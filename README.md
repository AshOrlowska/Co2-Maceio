# 🌍 - Co2-Maceio - Projeto Simples Meteorologia + Dados
Este projeto tem como objetivo **analisar a emissão de dióxido de carbono (CO₂)** na cidade de **Maceió - Alagoas - Brasil** ao longo de 15 anos, do dia **20/01/2010** até **20/09/2025**.  

A iniciativa combina **ciência de dados + meteorologia**, utilizando a biblioteca **Pandas** para manipulação dos dados e **Matplotlib** para visualização.  
Com isso, é possível **verificar se as emissões aumentaram ou diminuíram** nesse período.

---

## 📥 Como Obter os Dados Reais

EDGAR (Emissions Database for Global Atmospheric Research)
Baixe os gridmaps anuais de CO₂:
<div> 
  🔗  <a href="https://edgar.jrc.ec.europa.eu/dataset_ghg60" target="_blank"><img   height = "150" width = "150" src="https://edgar.jrc.ec.europa.eu/images/logo/positive/logo-ec--en.svg" target="_blank"></a>

  CAMS (Copernicus Atmosphere Monitoring Service)
  Dados de reanálise de gases de efeito estufa:
  🔗  <a href="https://ads.atmosphere.copernicus.eu/cdsapp#!/dataset/cams-global-ghg-reanalysis-egg4 " target="_blank"><img  src="https://ads.atmosphere.copernicus.eu/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcopernicus.3cdaca12.png&w=96&q=75" target="_blank"></a>
</div>

<br>

## 📊 Funcionalidades

- Leitura e organização de dados de emissões (EDGAR ou simulados).
- Estimativa de emissões futuras (quando não há dados disponíveis).
- Análise estatística de tendência (regressão linear + p-valor).
- Geração de gráficos de séries temporais.
- Conclusão automática: **aumentou ou diminuiu**?
<br>

## Gráfico: Emissões de CO2 - Maceió - 2010 - 2025 (Gráficos Fictícios)
<div>
  <img align = "left" alt = "Ash-Co2" height = "800", width="1000" border= "6px;" src = "https://github.com/AshOrlowska/Co2-Maceio/blob/Master/Emiss%C3%B5es%20de%20CO2%20-%20Macei%C3%B3%20-%202010%20-%202025.png?raw=true">
</div>
ㅤ

<br>

## 🚀 Tecnologias Utilizadas

- [Python 3.9+](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [SciPy](https://scipy.org/)
- [xarray](https://docs.xarray.dev/) (opcional, para NetCDF)
- [cdsapi](https://pypi.org/project/cdsapi/) (opcional, para baixar dados CAMS)

---

## 📂 Estrutura do Repositório

```bash
├── data/                  # Coloque aqui os arquivos EDGAR / CAMS baixados
├── co2_maceio_analysis.py # Script principal
├── simple_analysis.py     # Versão simplificada (~20 linhas)
└── README.md              # Documentação do projeto

⚙️ Como Executar

1 - Clone este repositório:

git clone https://github.com/seu-usuario/co2-maceio.git
cd co2-maceio


2 - Crie um ambiente virtual (opcional, mas recomendado):

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3 - Instale as dependências:

pip install -r requirements.txt

4 - Execute a versão completa:

python co2_maceio_analysis.py


Ou a versão simples:

python simple_analysis.py

5 - 📥 Como Obter os Dados Reais

EDGAR (Emissions Database for Global Atmospheric Research)
Baixe os gridmaps anuais de CO₂ em resolução 0.1°:
🔗  https://edgar.jrc.ec.europa.eu/dataset_ghg60

CAMS (Copernicus Atmosphere Monitoring Service)
Dados de reanálise de gases de efeito estufa:
🔗 https://ads.atmosphere.copernicus.eu/cdsapp#!/dataset/cams-global-ghg-reanalysis-egg4

Coloque os arquivos na pasta data/ antes de rodar o script.

6 - 📈 Exemplos de Resultados

- Gráfico das emissões anuais de CO₂ em Maceió.
- Linha de tendência indicando aumento ou diminuição.
- Estatísticas descritivas (média 2010–2014 vs média 2020–2024).
- P-valor indicando significância da tendência.

🧑‍💻 Autor
Ash A. Orłowska
