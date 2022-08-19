from sys import exit

try:
    import pandas as pd

    print("Module pandas loaded successfully.")
except:
    print("Install: 'pip install pandas' ")
    exit(0)

# Modules prepared, let's go :)

source_data = "https://raw.githubusercontent.com/abixadamj/helion-python/main/Rozdzial_5/data.csv"
print(f"Source data: {source_data}")

# Creating DataFrame
try:
    df = pd.read_csv(source_data)
    print("Source data has been downloaded")
except:
    print("Warning! Downloading failure")
    exit(0)

print("----[ Information about source data]----")
print(df)
print("-----------------------------------------")

new_df = df[["obce", "polskie", "month"]]
plot = new_df.plot(
    kind="line",
    x="month",
    xlabel="Year - month",
    ylabel="Number of ships handled",
    title="Reloading in the port of Gdynia"
)

plot.get_figure().savefig("../files/graph.png")
