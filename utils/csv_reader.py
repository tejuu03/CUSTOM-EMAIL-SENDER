import pandas as pd

def read_csv(file):
    return pd.read_csv(file).to_dict(orient='records')
