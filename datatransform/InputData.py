import pandas as pd

# reading in values from web hosted csv
df = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv")

# prints unmodified data frame
print(df)

# saves csv with no modifications
df.to_csv(r'data.csv')

# strips data frame down to the necessary date field
#df = df.drop(["state", "fips", "cases", "deaths"], axis=1)

# removes all duplicate data values and then prints modified date frame
df = pd.DataFrame(data = df['date'].unique())
print(df)

# saves csv with only unique dates from the imported csv
df.to_csv(r'dates.csv')
