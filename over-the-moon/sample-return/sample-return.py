import pandas as pd

# Load the data
rock_samples = pd.read_csv('C:/Users/miguel/Desktop/Codes/24.1_trilha_for_code/over-the-moon/sample-return/data/rocksamples.csv')

# Convert the weight to kilograms
rock_samples['Weight (g)'] = rock_samples['Weight (g)'] * 0.001

rock_samples.rename(columns={'Weight (g)': 'Weight (kg)'}, inplace=True)


missions = pd.DataFrame()                                 # missions e um novo dataframe
missions['Mission'] = rock_samples['Mission'].unique()    # cria uma coluna chamada 'Mission' no novo dataframe missions e
                                                          # atribui a ela os valores unicos da coluna 'Mission' do dataframe rock_samples

sample_total_weight = rock_samples.groupby('Mission')['Weight (kg)'].sum() # soma todos os valores de peso de cada missao, e agrupa eles por missao, em um novo dataframe chamado sample_total_weight
# print(sample_total_weight)


# tendo em vista que o dataframe missions tem apenas uma coluna 'Mission', e o dataframe sample_total_weight tem duas colunas e uma delas e a coluna 'Mission', podemos fazer um merge entre os dois dataframes, juntando-os pela coluna 'Mission' e adicionando uma nova coluna ao dataframe missions, com a soma dos pesos de cada missao

missions = pd.merge(missions, sample_total_weight, on='Mission') # merge dataframes
# print(missions)

# fez o merge corretamente, porem a coluna ainda nao possui um nome
missions.rename(columns={'Weight (kg)': 'Sample weight (kg)'}, inplace=True) # renomeia a coluna

# print(missions)

missions['Weight diff'] = missions['Sample weight (kg)'].diff()

# print(missions)

missions['Weight diff'] = missions['Weight diff'].fillna(value=0) # preenche os valores NaN com 0

print(missions)