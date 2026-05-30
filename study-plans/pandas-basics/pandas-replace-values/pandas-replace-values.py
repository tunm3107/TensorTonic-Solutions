import pandas as pd

def replace_values(data, column, old_val, new_val):
    """
    Returns: dict with 'data' (dict) and 'count' (int)
    """
    df = pd.DataFrame(data)

    new_df = df.replace({column: {old_val: new_val}})
    return {
        "data": new_df.to_dict("list"),
        "count": df[column].loc[df[column] == old_val].shape[0]
    }