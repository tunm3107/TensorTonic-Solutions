import pandas as pd

def reset_index_demo(data, index_col):
    """
    Returns: list [columns_before_reset, columns_after_reset]
    """
    df = pd.DataFrame(data)

    indexed_df = df.set_index(index_col)
    df = indexed_df.reset_index(names=index_col)

    return [indexed_df.columns.tolist(), df.columns.tolist()]