import scrapy
import json
import csv
import datetime
# System
import glob
import os
from xlsxwriter.workbook import Workbook

class CrawlerSpider(scrapy.Spider):
    name = 'crawler'
    # allowed_domains = ['covid19.go.id']

    start_urls = [
        'https://data.covid19.go.id/public/api/prov_detail_JAWA_BARAT.json',
        'https://data.covid19.go.id/public/api/prov_detail_DKI_JAKARTA.json',
        'https://data.covid19.go.id/public/api/prov_detail_JAWA_TIMUR.json',
        'https://data.covid19.go.id/public/api/prov_detail_JAWA_TENGAH.json',
        'https://data.covid19.go.id/public/api/prov_detail_SULAWESI_SELATAN.json',
        'https://data.covid19.go.id/public/api/prov_detail_BANTEN.json',
        'https://data.covid19.go.id/public/api/prov_detail_NUSA_TENGGARA_BARAT.json',
        'https://data.covid19.go.id/public/api/prov_detail_BALI.json',
        'https://data.covid19.go.id/public/api/prov_detail_PAPUA.json',
        'https://data.covid19.go.id/public/api/prov_detail_KALIMANTAN_SELATAN.json',
        'https://data.covid19.go.id/public/api/prov_detail_SUMATERA_BARAT.json',
        'https://data.covid19.go.id/public/api/prov_detail_SUMATERA_SELATAN.json',
        'https://data.covid19.go.id/public/api/prov_detail_KALIMANTAN_TENGAH.json',
        'https://data.covid19.go.id/public/api/prov_detail_KALIMANTAN_TIMUR.json',
        'https://data.covid19.go.id/public/api/prov_detail_SUMATERA_UTARA.json',
        'https://data.covid19.go.id/public/api/prov_detail_DAERAH_ISTIMEWA_YOGYAKARTA.json',
        'https://data.covid19.go.id/public/api/prov_detail_KALIMANTAN_UTARA.json',
        'https://data.covid19.go.id/public/api/prov_detail_KEPULAUAN_RIAU.json',
        'https://data.covid19.go.id/public/api/prov_detail_KALIMANTAN_BARAT.json',
        'https://data.covid19.go.id/public/api/prov_detail_SULAWESI_TENGGARA.json',
        'https://data.covid19.go.id/public/api/prov_detail_LAMPUNG.json',
        'https://data.covid19.go.id/public/api/prov_detail_SULAWESI_UTARA.json',
        'https://data.covid19.go.id/public/api/prov_detail_SULAWESI_TENGAH.json',
        'https://data.covid19.go.id/public/api/prov_detail_RIAU.json',
        'https://data.covid19.go.id/public/api/prov_detail_PAPUA_BARAT.json',
        'https://data.covid19.go.id/public/api/prov_detail_SULAWESI_BARAT.json',
        'https://data.covid19.go.id/public/api/prov_detail_JAMBI.json',
        'https://data.covid19.go.id/public/api/prov_detail_MALUKU_UTARA.json',
        'https://data.covid19.go.id/public/api/prov_detail_MALUKU.json',
        'https://data.covid19.go.id/public/api/prov_detail_GORONTALO.json',
        'https://data.covid19.go.id/public/api/prov_detail_KEPULAUAN_BANGKA_BELITUNG.json',
        'https://data.covid19.go.id/public/api/prov_detail_ACEH.json',
        'https://data.covid19.go.id/public/api/prov_detail_BENGKULU.json',
        'https://data.covid19.go.id/public/api/prov_detail_NUSA_TENGGARA_TIMUR.json'
    ]

    def parse(self, response):
        result_directory = "Result/"
        url = response.url

        keyword = 'prov_detail_'

        stringIndex = url.find(keyword)
        startIndex = stringIndex + len(keyword)

        stringProvince = url[startIndex:-5]
        
        target_path = result_directory + stringProvince + ".csv"
        
        
        # json text
        jsonObject = json.loads(response.text)
        
        # Open file writing
        # // Using CSV
        data_file = open(target_path, "w")
        
        
        #create the csv writer object
        csv_writer = csv.writer(data_file)

        count = 0

        for row in jsonObject["list_perkembangan"]: 
            if count == 0:
                
                # Writing headers of CSV file
                header = row.keys()
                csv_writer.writerow(header)
                count += 1
            
            # Writing data of CSV file
            csv_writer.writerow(row.values())
        
        data_file.close()
        
    
    def crawl_to_worksheet(): 
        url = response.url

        keyword = 'prov_detail_'

        stringIndex = url.find(keyword)
        startIndex = stringIndex + len(keyword)

        stringProvince = url[startIndex:-5]

        jsonObject = json.loads(response.text)

        # // Using WorkBook
        workbook = Workbook(stringProvince + ".xlsx")
        worksheet = workbook.add_worksheet()

        # Date Format
        cell_date_format = workbook.add_format({'num_format': 'dd mmmm yyyy'})
        cell_numeric_format = workbook.add_format({'num_format': '#,##0'})

        row_index = 0
        for row in jsonObject["list_perkembangan"]: 

            rowItem = row.values()

            if row_index == 0:
                rowItem = row.keys()
            
            column_index = 0
            for value in rowItem:
                # Header
                if row_index == 0: 
                    worksheet.write(row_index, column_index, value, )

                # Value Date Time
                elif column_index == 0 and row_index != 0:
                    timestamp = int(value)
                    date_time = datetime.datetime.fromtimestamp(timestamp / 1e3)
                    worksheet.write_datetime(row_index, column_index, date_time, cell_date_format)

                ## Other Numeric 
                else: 
                    new_value = int(value)
                    worksheet.write(row_index, column_index, new_value, cell_numeric_format)

                column_index += 1
            
            column_index = 0
            row_index += 1
        workbook.close()

    def convert_csv_to_xlsx(): 
        print("hello")
        # for csvfile in glob.glob( os.path.join(".", "*.csv") ):
        #     workbook = Workbook(csvfile[:-4] + ".xlsx")
            
        #     worksheet = workbook.add_worksheet("Jawa Barat")
            
        #     with open(csvfile, "rt", encoding="utf8") as f:
        #         reader = csv.reader(f)

        #         for r, row in enumerate(reader):
        #             for c, col in enumerate(row): 
        #                 worksheet.write(r, c, col)
                
        #     workbook.close()
        
        

