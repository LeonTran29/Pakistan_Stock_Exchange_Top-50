import os
def check_missing_values(df):
    """
    Check for missing values in the DataFrame.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to check.
    
    Returns:
    pd.DataFrame: A DataFrame with the count of missing values for each column.
    """
    missing_value_2 = df.is_null().sum().reset_index()
    missing_value_2.columns = ['Column', 'Missing Values']
    if missing_value_2['Missing Values'].sum() == 0:
        print("No missing values found in the DataFrame.")
    else:
        print("Missing values found in the following columns:")
        print(missing_value_2[missing_value_2['Missing Values'] > 0])
        missing_value_1 = df.groupby('Id').agg(lambda x: x.isnull().sum()).reset_index()
        return missing_value_1

def check_information(df):
    """
    Check the information of the DataFrame.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to check.
    
    Returns:
    None
    """
    print("----------------------------------------------------------------")
    print("DataFrame Information:")
    df.info()
    print("----------------------------------------------------------------")
    print("\nDataFrame Description:")
    print(df.describe())
    print("----------------------------------------------------------------")
    print("\nDataFrame Head:")
    print(df.head(5))
    print("----------------------------------------------------------------")
    print("\nDataFrame Tail:")
    print(df.tail(5))
    print("----------------------------------------------------------------")
    print("\nDataFrame Shape:", df.shape)
    print("\nDataFrame Columns:", df.columns.tolist())
    print("\nDataFrame Dtypes:", df.dtypes)
    
def check_duplicates(df):
    """
    Check for duplicate rows in the DataFrame.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to check.
    
    Returns:
    int: The number of duplicate rows.
    """
    duplicates = df.duplicated(keep=False).sum()
    if duplicates > 0:
        print(f"Duplicate rows found: {duplicates}")
    else:
        print("No duplicate rows found.")
    return duplicates

def display_duplicates(df):
    """
    Display the duplicate rows in the DataFrame.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to check.
    
    Returns:
    pd.DataFrame: A DataFrame containing the duplicate rows.
    """
    # This will group by all columns and count occurrences
    duplicate_counts = df.groupby(df.columns.tolist(), as_index = False).size()
    # Filter to show only duplicates (count > 1)
    duplicates = duplicate_counts[duplicate_counts['size'] > 1]
    print("Count of duplicate rows:")
    print(duplicates)
    
    # To specifically display the duplicate rows
    # minuteSleep['Date'] =  pd.to_datetime(minuteSleep['Date'], format='%m/%d/%Y')
    # minuteSleep['Time'] = pd.to_datetime(minuteSleep['Time'], format='%H:%M:%S')
    # Then:
    # row_to_check = df[
    # (df['column1'] == 'value1') &
    # (df['column2'] == 'value2') & 
    # (df['column3'] == 'value3')
    # ]