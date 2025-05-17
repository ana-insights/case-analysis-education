import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# Lendo a Base de Dados
Base_Dados = pd.read_csv('StudentsPerformance+(1).csv')

# Dimensão
Base_Dados.shape

# Estrutura
Base_Dados.head()

# Campos nulos
Nulos = Base_Dados.isnull()

plt.title('Analise de campos nulos')
plt.figure(figsize=(16, 5))
sns.heatmap(Nulos, cbar=False)
plt.show()
print(Nulos.sum())

# Campos Unicos
print(Base_Dados.nunique())

# Dados duplicados
print(Base_Dados.duplicated().sum())

# Estatistica
print(Base_Dados.describe())

# info
print(Base_Dados.info())

print(Base_Dados['gender'].value_counts(normalize=True)*100)
print(Base_Dados['race/ethnicity'].value_counts(normalize=True)*100)
print(Base_Dados['parental level of education'].value_counts(
    normalize=True)*100)
print(Base_Dados['test preparation course'].value_counts(normalize=True)*100)
print(Base_Dados['lunch'].value_counts(normalize=True)*100)

# Analise nota de matematica por genero
sns.boxplot(data=Base_Dados, x='math score', y='gender')
plt.show()

# Analise nota de leitura por genero
sns.boxplot(data=Base_Dados, x='reading score', y='gender')
plt.show()

# Analise nota de Redação por genero
sns.boxplot(data=Base_Dados, x='writing score', y='gender')
plt.show()


print(Base_Dados.groupby(by=['gender']).describe()['math score'].reset_index())


# Analise do teste de matemática

sns.boxplot(data=Base_Dados, x='math score', y='parental level of education')
plt.title('Influência do nível educacional dos pais no desempenho em matemática.')
plt.show()
print(Base_Dados.groupby(by=['parental level of education']).describe()[
      'math score'].reset_index())

sns.boxplot(data=Base_Dados, x='math score', y='test preparation course')
plt.title('Influência da preparação antes do teste no desempenho em matemática.')
plt.show()
print(Base_Dados.groupby(by=['test preparation course']).describe()[
      'math score'].reset_index())

sns.scatterplot(data=Base_Dados, x='math score', y='writing score')
plt.show()
