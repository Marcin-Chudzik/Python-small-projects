import pandas as pd

source_data = "../files/dane_opady_temperatura.ods"
print(f"Source data: {source_data}")

df = pd.read_excel(source_data, engine="odf")

print("----[ Information about source data]----")
print(df)
print("-----------------------------------------")

# Adding a column
df["Autor"] = "Marcin Chudzik"
print("----[ Information about data]----")
print(df)
print("-----------------------------------------")

# Libre Office Calc
df.to_excel("../files/dane_opady_temperatura_nowy.ods", engine="odf")
# MS-Excel
df.to_excel("../files/dane_opady_temperatura_nowy.xlsx", engine="openpyxl")
