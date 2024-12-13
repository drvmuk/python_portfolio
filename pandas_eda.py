import pandas as pd

df_tips = pd.read_csv("resources\\tips.csv")

# print head and tail
print(df_tips.head(2))
print(df_tips.tail(2))

# print column names
print(df_tips.columns)

# print aggregates --> min, max
df_aggregate = df_tips.aggregate({"total_bill":['min','max'],
                                  "tip":['min','max']})
print(df_aggregate)

