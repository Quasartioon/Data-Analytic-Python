# Análise de Dados de Feminicídio em Minas Gerais
Este projeto utiliza dados de feminicídios em Minas Gerais para analisar padrões, compreender a violência de gênero e apoiar a criação de políticas públicas mais eficazes.  
## Objetivo
Investigar a ocorrência de feminicídios por meio de dados estruturados, identificando padrões sociais, regionais e comportamentais que contribuam para a prevenção da violência contra a mulher.  
## Importância do Projeto
* Compreensão do problema: o feminicídio é uma forma extrema de violência de gênero, frequentemente ligada a fatores como machismo e violência doméstica.
* Base para decisões públicas: a análise de dados permite orientar políticas públicas mais eficazes e direcionadas.
* Uso de dados atualizados: informações recentes garantem análises mais precisas e alinhadas com a realidade.

## Estrutura dos Dados

Os dados analisados incluem variáveis como:  

* Idade da vítima;
* Localização do crime;
* Relação com o agressor;
* Método utilizado;
* Histórico de denúncias.  

Essas informações permitem identificar padrões geográficos e sociais.  

## Abordagem Regional
Minas Gerais apresenta grande diversidade social e econômica.  
Por isso, o projeto considera uma análise regionalizada, permitindo:

* Identificar áreas com maior incidência
* Entender diferenças entre regiões
* Criar soluções específicas (não genéricas)

## Impacto e Aplicações
* Fortalecimento de redes de proteção à mulher
* Apoio a pesquisas acadêmicas
* Incentivo à transparência e acesso à informação
* Colaboração entre instituições (governo, ONGs, saúde, segurança)
* Desenvolvimento de campanhas de conscientização

## Monitoramento e Evolução

A análise contínua dos dados permite:

* Avaliar políticas públicas existentes
* Identificar melhorias necessárias
* Adaptar estratégias conforme mudanças sociais

## Conclusão

O uso de dados sobre feminicídios em Minas Gerais contribui para uma compreensão mais profunda do problema e para o desenvolvimento de soluções mais eficazes, promovendo segurança e igualdade de gênero. 

# Documentação do Código  
O projeto foi desenvolvido em Python utilizando bibliotecas voltadas para análise de dados e visualização.
## Tecnologias Utilizadas
* pandas → manipulação e análise de dados
* numpy → operações numéricas
* matplotlib → geração de gráficos

## Leitura e Tratamento dos Dados
O script realiza a leitura de um arquivo `<.csv>` contendo os dados de feminicídio: 
``` python 
feminicidio_df = pd.read_csv('feminicidio_2023.csv', sep=';')
```
Principais etapas de tratamento:

* Limpeza da coluna de datas (data_fato)
* Conversão para formato datetime
* Extração do mês para análises temporais
* Identificação de possíveis erros de conversão  
