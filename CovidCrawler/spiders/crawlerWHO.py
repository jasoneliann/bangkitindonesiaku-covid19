import scrapy
# System
import os
from xlsxwriter.workbook import Workbook

# import python script
import sys
absolute_path = os.path.abspath(__file__)
script_dir = os.path.dirname(absolute_path) + "/../../Script/"
sys.path.append(script_dir)

import who_data_converter



class CrawlerWHOSpider(scrapy.Spider):
    name = 'crawlerWHO'

    start_urls = [
        "https://covid19.who.int/WHO-COVID-19-global-data.csv"
    ]

    def parse(self, response):
        # print("Directory Path: " + )

        # This is the used one
        result_directory = "Data/PerkembanganKasus/"
                
        name = "WHO-COVID-19-global-data"

        target_path = result_directory + name + ".csv"

        # Write File
        data_file = open(target_path, "w")
        data_file.write(response.text)
        data_file.close()

        # Run script to extract file
        who_data_converter.extract_global_WHO_csv_to_each_country(target_path, "Data/PerkembanganKasus/WHO/")
