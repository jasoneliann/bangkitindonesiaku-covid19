#!/usr/bin/env python
import pandas as pd
import csv
import datetime

def generate_dict_rename_column(columns): 
    
    """
    Generate the dict for renaming columns.
    
    Parameters
    ----------
    columns: Array of string of the columns.
    
    
    Returns
    -------
    Dictionary of the rename columns
    """
    
    result_dict = {}

    for column in columns: 
        result_dict[column] = column.lower()

    return result_dict

def write_to_disk(dataframe, filename, path): 
    """
    Write dataframe to the disk.
    
    Parameters
    ----------
    dataframe: Pandas DataFrame that will be saved.
    filename: String The file name of the csv. Without the format.
    path: The directory path of the result.
    """
    dataframe.to_csv(path + filename + ".csv", index=False)


def convert_series_to_dataframe(country_series): 
    """
    Save the Pandas series into Pandas than save.
    
    Parameters
    ----------
    country_series: Array of Pandas Series
    
    Returns
    -------
    Pandas DataFrame of the country
    
    """
    
    country_dataframe = pd.DataFrame(data=country_series)
    return country_dataframe
    
def convert_string_date_yyyy_mm_dd_to_dd_mm_yyyy(string_date_time): 
    """
    Convert string yyyy-mm-dd to string date dd-mm-yyyy
    
    Parameters
    ----------
    string_date_time: String that is related to date. "yyyy-mm-dd"
    
    Returns
    -------
    string dd-mm-yyyy
    """
    
    the_date_time = datetime.datetime.strptime(string_date_time, "%Y-%m-%d")
    
    new_date_time = datetime.datetime.fromtimestamp(the_date_time.timestamp())
    result = new_date_time.strftime("%d-%m-%Y")
    return result
    
def extract_global_WHO_csv_to_each_country(csv_path, target_path): 
    """
    Extract global WHO data to each country csv. Make the smaller csv.
    
    Parameters
    ----------
    csv_path: The global WHO csv directory file
    target_path: The output directory of the extracted value.
    """
    
    # Read CSV
    df = pd.read_csv(csv_path).rename(str.lower, axis='columns')
    
        
    
    list_country_code = [df.iloc[0]["country_code"]]
    country_series = []
    
    # Loop each row
    for (index, col) in df.iterrows(): 
        current_country = col["country_code"]

        # Make temporary Data
        if (current_country not in list_country_code): 

            country_dataframe = convert_series_to_dataframe(country_series)

            country_name = country_series[0]["country"].replace("'", "")
            write_to_disk(country_dataframe, country_name, target_path)

            # New iteration
            list_country_code.append(current_country)
            country_series = []
        
        # Change date-time format
        col["date_reported"] = convert_string_date_yyyy_mm_dd_to_dd_mm_yyyy(col["date_reported"])

        country_series.append(col)
    
if __name__ == "__main__": 
    extract_global_WHO_csv_to_each_country("../Data/PerkembanganKasus/WHO-COVID-19-global-data.csv", "../Data/PerkembanganKasus/WHO/")
