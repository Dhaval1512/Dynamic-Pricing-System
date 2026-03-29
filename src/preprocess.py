import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def preprocess(df):
    # Drop target
    X = df.drop("demand", axis=1)
    y = df["demand"]

    # No missing values → skip for now

    # No categorical → skip encoding

    return X, y