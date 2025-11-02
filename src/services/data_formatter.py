import pandas as pd

def format_dataframe(
        df : pd.DataFrame
    ) -> dict:
    """
    Formats a DataFrame for JSON serialization by converting data types.

    Args:
        df (pd.DataFrame): Input DataFrame.
    Returns:
        (dict): Formatted DataFrame as a dictionary.
    """
    for col in df.columns:
        if df[col].dtype in ['float64', 'int64', 'bool']:
            df[col] = df[col].astype(df[col].dtype)
        else:
            df[col] = df[col].astype(str)

    return df.to_dict()