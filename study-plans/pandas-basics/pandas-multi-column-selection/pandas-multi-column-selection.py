import pandas as pd

def select_columns(data, columns):
    """
    Returns: dict mapping selected column names to value lists
    """
    df = pd.DataFrame(data)
    return df.loc[:, columns].to_dict("list")