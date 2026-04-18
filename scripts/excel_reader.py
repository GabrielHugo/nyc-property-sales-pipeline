import pandas as pd
import numpy as np

class Extract:
    def __init__(self, file):

        self.file = file

    def read_csv(self):
        df = pd.read_csv(self.file)

        return df
