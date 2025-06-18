import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
df = pd.read_csv('distancia_colisao.csv')

# Mostrar informações básicas
print("Resumo Estatístico:")
print(df.describe())

print("\nDistribuição de Risco de Colisão:")
print(df['risco_colisao'].value_counts())

# Histograma da distância
plt.figure(figsize=(10, 5))
sns.histplot(df['distancia_cm'], bins=30, kde=True, color='skyblue')
plt.axvline(100, color='red', linestyle='--', label='Limite de colisão (100 cm)')
plt.title('Distribuição das Distâncias (cm)')
plt.xlabel('Distância (cm)')
plt.ylabel('Frequência')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico de barras - Quantidade de risco vs não risco
plt.figure(figsize=(6, 4))
sns.countplot(x='risco_colisao', data=df, palette='Set2')
plt.xticks([0, 1], ['Sem risco', 'Com risco'])
plt.title('Distribuição de Risco de Colisão')
plt.xlabel('Risco de Colisão')
plt.ylabel('Contagem')
plt.tight_layout()
plt.show()

# Boxplot para ver outliers nas distâncias
plt.figure(figsize=(8, 4))
sns.boxplot(x='risco_colisao', y='distancia_cm', data=df, palette='coolwarm')
plt.xticks([0, 1], ['Sem risco', 'Com risco'])
plt.title('Boxplot das Distâncias por Classe de Risco')
plt.xlabel('Risco de Colisão')
plt.ylabel('Distância (cm)')
plt.tight_layout()
plt.show()
