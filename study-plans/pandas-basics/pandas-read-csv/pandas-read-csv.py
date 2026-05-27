import pandas as pd

def create_dataframe(data):
    """
    Returns: dict with 'data', 'shape', 'columns'
    """
    df = pd.DataFrame(data)

    return {"data": {key: data[key] for key in df.columns}, 
            "shape": [df.shape[0], df.shape[1]], 
            "columns": list(df.columns)}