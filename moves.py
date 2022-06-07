import pandas as pd

df = pd.read_csv("D:\codes_python\sds project\games_with_null_values.csv")

moves = df["moves"]

moves.to_csv("moves.csv")