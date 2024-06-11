import pandas as pd

# Load the data
rock_samples = pd.read_csv('sample-return/data/rocksamples.csv')

# Convert the weight to kilograms
rock_samples['Weight (g)'] = rock_samples['Weight (g)'] * 0.001

rock_samples.rename(columns={'Weight (g)': 'Weight (kg)'}, inplace=True)


missions = pd.DataFrame()
missions['Mission'] = rock_samples['Mission'].unique()


sample_total_weight = rock_samples.groupby('Mission')['Weight (kg)'].sum()