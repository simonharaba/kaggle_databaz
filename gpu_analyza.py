import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Načítanie CSV súboru
df = pd.read_csv('gpu_specs_v6.csv')

# Základné info
print(df.head())
print(df.info())
print("Výrobcovia:", df["manufacturer"].unique())

# Výber stĺpcov
important = df[["manufacturer", "memSize", "memBusWidth", "gpuClock", "memClock"]]

# Histogramy
sns.histplot(data=important, x="memSize", kde=True)
plt.title("Veľkosť pamäte (GB)")
plt.show()

sns.histplot(data=important, x="gpuClock", kde=True)
plt.title("Frekvencia jadra (MHz)")
plt.show()

# Scatterploty
sns.scatterplot(data=important, x="memSize", y="memBusWidth", hue="manufacturer")
plt.title("Pamäť vs Šírka zbernice")
plt.show()

sns.scatterplot(data=important, x="gpuClock", y="memClock", hue="manufacturer")
plt.title("GPU frekvencia vs Pamäťová frekvencia")
plt.show()

# Výkonné GPU
avg_mem = important["memSize"].mean()
avg_gpu = important["gpuClock"].mean()
high_perf = important[(important["memSize"] > avg_mem) & (important["gpuClock"] > avg_gpu)]

print(f"Priemerná pamäť: {avg_mem:.2f} GB")
print(f"Priemerná frekvencia GPU: {avg_gpu:.2f} MHz")
print(f"Počet výkonných GPU: {high_perf.shape[0]}")
print(high_perf.head())
