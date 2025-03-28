import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

feminicidio_df = pd.read_csv('feminicidio_2023.csv', sep=';') # Lê o csv/planilha de feminicidio em Minas Gerais

# Ajustando os dados
feminicidio_df['data_fato'] = feminicidio_df['data_fato'].str.strip()
feminicidio_df['data_fato'] = pd.to_datetime(feminicidio_df['data_fato'], dayfirst=True, errors='coerce')
feminicidio_df['mes'] = feminicidio_df['data_fato'].dt.month

# Erros ao converter datas
erros = feminicidio_df[feminicidio_df['data_fato'].isnull()]


print("---------- Quantidade de vítimas por mês ----------\n") 
# Quantidade de casos por mês
casos_mes = feminicidio_df['mes'].value_counts().sort_index().reset_index()
casos_mes.columns = ['mes', 'quantidade']
print(casos_mes)

plt.figure(figsize=(10, 5))
plt.bar(casos_mes['mes'], casos_mes['quantidade'], color='skyblue')
plt.title('Quantidade de Casos por Mês - 2023 (MG)')
plt.xlabel('Mês')
plt.ylabel('Quantidade de Casos')
plt.xticks(np.arange(1, 13, 1))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

print("\n---------- Média de vítimas por mês ---------- \n") 

# Número médio de vítimas por mês, aredondando pro valor inteiro mais próximo e sem números após a vírgula
media_vitimas = feminicidio_df.groupby('mes')['qtde_vitimas'].mean().round().astype(int).reset_index(name='media vitimas por mês')
print(media_vitimas)


media_vitimas = feminicidio_df.groupby('mes')['qtde_vitimas'].apply(lambda x: int(np.round(np.mean(x)))).reset_index(name='media vitimas por mês')

plt.figure(figsize=(10, 5))
plt.plot(media_vitimas['mes'], media_vitimas['media vitimas por mês'], marker='o', color='orange', label='Média de Vítimas')
plt.title('Média de Vítimas por Mês - 2023 (MG)')
plt.xlabel('Mês')
plt.ylabel('Média de Vítimas')
plt.xticks(np.arange(1, 13, 1))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.show()

print("\n---------- Casos por município ----------\n") 

# Quantidade de casos por município
casos_municipio = feminicidio_df['municipio_fato'].value_counts().reset_index()
casos_municipio.columns = ['municipio_fato', 'quantidade']
print(casos_municipio)

top_municipios = casos_municipio.head(10)
plt.figure(figsize=(8, 8))
plt.pie(top_municipios['quantidade'], labels=top_municipios['municipio_fato'], autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
plt.title('Top 10 Municípios com Mais Casos - 2023 (MG)')
plt.show()

print("\n---------- Quantidade de consumados e tentados ----------\n") 

# Distribuição de casos por tipo de ocorrência (tentado vs consumado)
casos_tipo = feminicidio_df['tentado_consumado'].value_counts().reset_index()
casos_tipo.columns = ['tentado_consumado', 'quantidade']
print(casos_tipo)

plt.figure(figsize=(8, 5))
plt.bar(casos_tipo['tentado_consumado'], casos_por_tipo['quantidade'], color=['red', 'green'])
plt.title('Casos Tentados vs Consumados - 2023 (MG)')
plt.ylabel('Quantidade de Casos')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

print("\n---------- Distribuição por RISP (Região Integrada de Segurança Pública) ----------\n") # Divisória de análise para análise

# Distribuição por RISP (Região Integrada de Segurança Pública)
casos_risp = feminicidio_df['risp'].value_counts().reset_index()
casos_risp.columns = ['risp', 'quantidade']
print(casos_risp)

plt.figure(figsize=(10, 7))
plt.barh(casos_por_risp['risp'], casos_por_risp['quantidade'], color='purple')
plt.title('Casos por RISP - 2023 (MG)')
plt.xlabel('Quantidade de Casos')
plt.ylabel('RISP')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()

print("\n---------- Distribuição por RMBH (Região Metropolitana de Belo Horizonte) ----------\n") # Divisória de análise para análise

# Distribuição por RMBH (Região Metropolitana de Belo Horizonte)
casos_rmbh = feminicidio_df['rmbh'].value_counts().reset_index()
casos_rmbh.columns = ['rmbh', 'quantidade']
print(casos_rmbh)

plt.figure(figsize=(8, 5))
plt.bar(casos_rmbh['rmbh'], casos_rmbh['quantidade'], color='cyan')
plt.title('Casos por RMBH - 2023 (MG)')
plt.ylabel('Quantidade de Casos')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

print("\n---------- Relação entre Casos Tentados e Consumados por RISP ----------\n") # Divisória de análise para análise

relacao_risp = feminicidio_df.groupby(['risp', 'tentado_consumado']).size().unstack(fill_value=0)
print(relacao_risp)

relacao_risp.plot(kind='bar', stacked=True, figsize=(12, 6), color=['red', 'green'])
plt.title('Casos Tentados vs Consumados por RISP - 2023 (MG)')
plt.xlabel('RISP')
plt.ylabel('Quantidade de Casos')
plt.legend(title='Tipo de Ocorrência')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

print("\n---------- Média de Vítimas por RMBH ----------\n") # Divisória de análise para análise
media_vitimas_rmbh = feminicidio_df.groupby('rmbh')['qtde_vitimas'].mean().round().astype(int).reset_index()
media_vitimas_rmbh.columns = ['RMBH', 'Media_Vitimas']

print(media_vitimas_rmbh)

plt.figure(figsize=(10, 6))
plt.bar(media_vitimas_rmbh['RMBH'], media_vitimas_rmbh['Media_Vitimas'], color='purple')
plt.title('Média de Vítimas por RMBH - 2023 (MG)')
plt.xlabel('RMBH')
plt.ylabel('Média de Vítimas')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

print("\n---------- Distribuição de Casos por Estação do Ano ----------\n") # Divisória de análise para análise

def estacao_do_ano(data):
    mes = data.month
    if mes in [12, 1, 2]:
        return 'Verão'
    elif mes in [3, 4, 5]:
        return 'Outono'
    elif mes in [6, 7, 8]:
        return 'Inverno'
    else:
        return 'Primavera'

feminicidio_df['estacao'] = feminicidio_df['data_fato'].apply(estacao_do_ano)
casos_estacao = feminicidio_df.groupby('estacao')['qtde_vitimas'].sum().reset_index()
print(casos_estacao)

plt.figure(figsize=(8, 8))
plt.pie(casos_estacao['qtde_vitimas'], labels=casos_estacao['estacao'], autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Distribuição de Casos por Estação - 2023 (MG)')
plt.show()