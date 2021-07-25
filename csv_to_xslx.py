#!/usr/bin/env python

import csv
import datetime
# System
import glob
import os
from xlsxwriter.workbook import Workbook

def csv_to_xlsx():
    path_directory = "./Result"

    workbook = Workbook("Indonesia-Covid" + ".xlsx")

    for csvfile in glob.glob( os.path.join(path_directory, "*.csv") ):
        province_string = csvfile[ len(path_directory) + 1 : -4 ]
        
        worksheet = workbook.add_worksheet(province_string)
        
        cell_date_format = workbook.add_format({'num_format': 'dd mmmm yyyy'})
        cell_numeric_format = workbook.add_format({'num_format': '#,##0'})
        cell_header_format = workbook.add_format({ 'bold': True, 'locked': True, 'bg_color': 'green', 'shrink': True})

        with open(csvfile, "rt", encoding="utf8") as f:
            reader = csv.reader(f)

            for r, row in enumerate(reader):
                for c, col in enumerate(row): 
                    value = col
                    # Header
                    if r == 0: 
                        worksheet.write_string(r, c, value, cell_header_format)
                    # Tanggal
                    elif c == 0 and r != 0:             
                        timestamp = int(value)
                        date_time = datetime.datetime.fromtimestamp(timestamp / 1e3)
                        worksheet.write_datetime(r, c, date_time, cell_date_format)
                    
                    else: 
                        new_value = int(value)
                        worksheet.write_number(r, c, new_value, cell_numeric_format)
    
    workbook.worksheets_objs.sort(key=lambda x: x.name)
    workbook.close()

csv_to_xlsx()