import os
import pandas as pd
import yfinance as yf

# Define o período de tempo para baixar os dados
start_date = "2022-05-01"
end_date = "2022-05-08"

# Baixa os dados da ação AAPL do Yahoo Finance
ticker = yf.Ticker("AAPL")
df = ticker.history(start=start_date, end=end_date, interval="1wk")

# Salva os dados em um arquivo xls
filename = "AAPL_prices.xls"
df.to_excel(filename)

# Exibe o diretório atual
print(os.getcwd())

# Exibe o conteúdo do diretório
print(os.listdir())
