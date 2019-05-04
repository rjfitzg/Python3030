'''
Homework 10, Exercise 1
Riley Fitzgibbons
5/4/19
Uses the provided csv datasheet to plot some statistics about it. 
I used seaborn as it is an easier wrapper to use for matplotlib.
The instructions were extremely vague so I did my best to estimate what was wanted.
'''
import seaborn as sb # seaborn used matplotlib as a backend

# Load all data, I modified the file to be easier to load.
df_all = pd.read_csv('weath_mod.csv')

# Mean temp by day over all 12 months
for i in range(1,12+1):
    x = df_all[df_all['Month'] == i]
    sb.lineplot(x['Day'], df_all['Temperature daily mean [2 m above gnd]'])

# Total Precipitation by day over all 12 months
for i in range(1,12+1):
    x = df_all[df_all['Month'] == i]
    sb.lineplot(x['Day'], df_all['Total Precipitation (high resolution) daily sum [sfc]'])

# Snowfall by day over all 12 months
for i in range(1,12+1):
    x = df_all[df_all['Month'] == i]
    sb.lineplot(x['Day'], df_all['Snowfall Amount (high resolution) daily sum [sfc]'])

# Max temp by day over all 12 months
for i in range(1,12+1):
    x = df_all[df_all['Month'] == i]
    sb.lineplot(x['Day'], df_all['Temperature daily max [2 m above gnd]'])

# Min temp by day over all 12 months
for i in range(1,12+1):
    x = df_all[df_all['Month'] == i]
    sb.lineplot(x['Day'], df_all['Temperature daily min [2 m above gnd]'])
