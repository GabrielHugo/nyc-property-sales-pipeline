import pandas as pd
import numpy as np

class ExtractTransform:
    def __init__(self, file):

        self.file = file
        self.df = None

    def read_csv(self):
        self.df = pd.read_csv(self.file)

        return self.df

    def transform(self):

        df_transform = self.read_csv()

        df_transform = df_transform.drop("Unnamed: 0", axis=1)
        df_transform = df_transform.drop("EASE-MENT", axis=1)

        df_transform = df_transform.reset_index()

        df_transform = df_transform.replace(r"^\s*$", value=np.nan, regex=True)
        df_transform[["LAND SQUARE FEET", "GROSS SQUARE FEET", "SALE PRICE"]] = df_transform[["LAND SQUARE FEET", "GROSS SQUARE FEET", "SALE PRICE"]].replace(r"^\s*-\s*$", np.nan, regex=True)

        return df_transform.head(200)