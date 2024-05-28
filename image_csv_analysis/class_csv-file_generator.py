import pandas as pd

df = pd.read_csv("./image_csv/train_data.csv")

class_df = df[["class", "class_names"]]

class_df_unique = class_df.drop_duplicates()
class_df_sorted = class_df_unique.sort_values(by="class")

class_df_sorted.to_csv("class_names.csv", index=False)