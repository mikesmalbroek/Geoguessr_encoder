from collections import Counter
import pandas as pd

counts = Counter()

# Lees het grote bestand in stukken, zodat het geheugen beperkt blijft.
for chunk in pd.read_csv(
    "datasets/train.csv",
    usecols=["country"],
    dtype={"country": "string"},
    chunksize=100_000,
):
    counts.update(chunk["country"].dropna())

print("Aantal beelden per land:")
for country, count in counts.most_common():
    print(f"{country}: {count:,}")

print(f"\nTotaal met landlabel: {sum(counts.values()):,}")