import pandas as pd
df = pd.read_csv("Numpy/RealEstate-USA.csv", delimiter=",")
print(df.to_string())
print(df)

print(df.describe())

print(df.info)

print(df[6:8])

print(df.dtypes)

print(df.tail(3))

print(df.head(2))

print(df.shape)

city = df["city"]
print(city)

status = df["status"]
print(status)

city_status = df[["city", "status"]]
print(city_status)

third_row = df.loc[2]
print(third_row)

row_7_to_13 = df.loc[7:14]
print(row_7_to_13)

row_7_to_13 = df.iloc[7:14]
print(row_7_to_13)
