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
