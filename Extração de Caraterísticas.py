import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv('distancia_colisao.csv')

# Simular um índice de tempo
df['tempo'] = range(len(df))

# Definir janela (ex: 10 medições por vez)
janela = 10

# Aplicar extração de características com janela deslizante
df_feat = df.rolling(window=janela).agg({
    'distancia_cm': ['mean', 'std', 'min', 'max'],
    'risco_colisao': 'sum'
})

# Renomear colunas
df_feat.columns = ['media_distancia', 'desvio_distancia', 'min_distancia', 'max_distancia', 'soma_risco']
df_feat = df_feat.dropna().reset_index(drop=True)

# Exibir as 5 primeiras linhas das features extraídas
print(df_feat.head())

# Criação do arquivo CSV
df_feat.to_csv('features_sensor.csv', index=False)

# Plot da média das distâncias por janela
plt.figure(figsize=(12, 5))
plt.plot(df_feat['media_distancia'], label='Média da Distância', color='blue')
plt.title('Média da Distância em Janelas de 10 Leituras')
plt.xlabel('Janela')
plt.ylabel('Distância Média (cm)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Plot do desvio padrão das distâncias
plt.figure(figsize=(12, 5))
plt.plot(df_feat['desvio_distancia'], label='Desvio Padrão da Distância', color='orange')
plt.title('Variação das Distâncias em Janelas de 10 Leituras')
plt.xlabel('Janela')
plt.ylabel('Desvio Padrão (cm)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
