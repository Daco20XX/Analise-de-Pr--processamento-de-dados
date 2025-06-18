
# 📊 Pré-Análise de Dados: Classificação de Risco de Colisão

Este repositório contém a etapa de análise exploratória de dados (EDA), extração de características e redução de dimensionalidade com PCA, com base em simulações de sensores de distância. Esta análise servirá como base para treinamentos futuros de modelos preditivos em outro repositório.

---

## 🔍 Objetivo

Investigar o comportamento das leituras de sensores, entender padrões de risco de colisão e preparar os dados com características relevantes para serem utilizados posteriormente em modelos de classificação.

---

## 📌 Funcionalidades

- Geração e visualização de estatísticas descritivas;
- Gráficos de distribuição e separação de classes;
- Análise temporal com janelas deslizantes;
- Extração de estatísticas por janela (média, desvio, etc.);
- Redução de dimensionalidade via PCA.

---

## 🛠 Tecnologias Utilizadas

- **Python 3.x**  
- **NumPy**  
- **Pandas**  
- **Matplotlib**  
- **Seaborn**  
- **Scikit-learn**

---

## ▶️ Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/Daco20XX/Analise-de-Pr--processamento-de-dados.git
cd Analise-de-Pr--processamento-de-dados
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o script de análise:
```bash
python analise_eda.py
```

---

## 📁 Estrutura do Projeto

```
📦 Analise-de-Pr--processamento-de-dados
├── 📜 analise_eda.py
├── 📁 dados
│   └── simulated_data.csv
├── 📁 imgs
│   └── (imagens geradas pela análise)
└── 📄 README.md
```

---

## 📊 Relatório Técnico

### 1. Gráficos de EDA

#### Histograma da Distância

Mostra a distribuição das distâncias medidas pelos sensores, com destaque para o **limite de colisão (100 cm)**.

![Histograma](imgs/histograma_distancia.png)

#### Estatísticas Descritivas

Resumo estatístico dos dados coletados, revelando que 101 amostras indicam risco de colisão (distância < 100 cm).

![Estatísticas](imgs/resumo_estatistico.png)

#### Distribuição por Classe

Gráfico de barras mostrando a proporção de situações com e sem risco.

![Distribuição](imgs/distribuicao_risco.png)

#### Boxplot das Distâncias por Classe

A distância média das situações “com risco” é visivelmente menor e mais concentrada.

![Boxplot](imgs/boxplot_distancias.png)

---

### 2. Aplicação do PCA

A Análise de Componentes Principais (PCA) foi utilizada para reduzir a dimensionalidade e facilitar a visualização da separação entre classes.

![PCA](imgs/pca_projecao.png)

Apesar de a separação linear ser sutil, é possível observar aglomerados com e sem risco.

---

### 3. Extração de Características

Com o objetivo de representar melhor o contexto de risco em janelas de tempo, as seguintes features foram extraídas a cada 10 leituras:

| Feature             | Descrição                                      |
|--------------------|-----------------------------------------------|
| `media_distancia`  | Média das distâncias na janela                |
| `desvio_distancia` | Variação (desvio padrão) das distâncias       |
| `min_distancia`    | Valor mínimo observado                        |
| `max_distancia`    | Valor máximo observado                        |
| `soma_risco`       | Quantidade de medidas com risco (< 100 cm)    |

Essas características foram escolhidas por resumirem o comportamento da distância ao longo do tempo.

#### Exemplos gráficos:

- Média da distância por janela:

  ![Média](imgs/media_janela.png)

- Desvio padrão da distância:

  ![Desvio](imgs/desvio_janela.png)

- Exemplo da tabela com as features extraídas:

  ![Tabela Features](imgs/features_extraidas.png)

---

## 📎 Observações Finais

Este repositório trata exclusivamente da pré-análise de dados. Os modelos de classificação (MLP e MLP-RAM) serão desenvolvidos e avaliados em outro repositório, utilizando os dados e features preparados aqui.
