from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_excel("C:/Users/Rob/Documents/Projetos/Python/banco_de_dados/Vendas.xlsx", sheet_name='base_vendas')

df['ano_venda'] = pd.to_datetime(df['dt_venda']).dt.year

vendas_por_ano = df.groupby('ano_venda').size().reset_index(name='quantidade_vendas')

print(vendas_por_ano)

plt.figure(figsize=(10, 6))
sns.set_theme(style="darkgrid")

sns.barplot(data=vendas_por_ano, x='ano_venda', y='quantidade_vendas', palette='Blues')

plt.title('Quantidade de Vendas por Ano')
plt.xlabel('Ano')
plt.ylabel('Quantidade de Vendas')
plt.xticks(rotation=45)

plt.show()
