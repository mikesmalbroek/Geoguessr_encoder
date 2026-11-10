import pandas as pd

sample = pd.read_csv("datasets/train.csv", nrows=5)

print(sample.columns.tolist())
print(sample.to_string())