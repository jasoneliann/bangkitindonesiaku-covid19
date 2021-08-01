# BangkitIndonesiaKu 🇮🇩
BangkitIndonesiaKu merupakan sebuah open-source yang bertujuan untuk mengkolaborasikan analisa data Covid-19, terutama di Indonesia. Di negara Indonesia yang tercinta inilah kita dilahirkan dan dibesarkan. Kini negeri ini sedang mengalami gejolak pandemi yang tak kunjung usai. Dahsyatnya hempasan pandemi ini menciderai akal sehat manusia. Perut yang kosong, oknum-oknum yang tidak bertanggung jawab, informasi yang simpang siur, dan ekonomi yang tak kunjung pulih membuat masyarakat mulai muak atas semua ini.

Mencari formula kebijakan yang tepat merupakan salah satu cara untuk negeri ini bisa kembali pulih. Project open-source ini merupakan salah satu cara kita untuk berkolaborasi menemukan formula kebijakan yang tepat, terukur, dan transparan. Berkontribusi untuk negeri ini tidaklah harus menggunakan tenaga lapangan, namun juga bisa dengan donasi, maupun mengontribusikan ilmu-ilmu yang telah dikuasai. Saatnya generasi muda Indonesia bergerak untuk negeri ini, memberikan apapun yang kita bisa. Tidak perlu pintar ataupun kaya melainkan seseorang yang ingin belajar dan memiliki empati yang bisa membangkitkan Indonesia ini.

Pandemi Covid-19 merupakan masalah global yang sekarang sedang marak-maraknya. Oleh karena itu, Indonesia tidak bisa tinggal diam mengikuti apa aturan WHO. Kita juga harus memiliki terobosan-terobosan yang konkrit. Ajaklah seluruh teman-temanmu untuk berkontribusi untuk negeri ini. 
1. Bagi yang memiliki dana yang lebih, sumbangkan.
2. Bagi yang memiliki waktu yang lebih, kontribusikan.
3. Bagi yang memiliki intelek yang lebih, kolaborasikan.


## Sumber Data
- [Covid19.go.id](https://covid19.go.id)
- [WHO CSV](https://covid19.who.int/WHO-COVID-19-global-data.csv)

# Sekilas Mengenai Project
Project ini merupakan project yang menggunakan `Python3`. Didukung oleh crawler yang bertugas mengumpulkan data yang menggunakan `scrapy`. Lalu menggunakan `xlsxwriter` untuk men-generate data. `pandas` sebagai referensi utama pengolahan data.

## Command
### Crawl Covid19.go.id
```
scrapy crawl crawler
```

### Crawl WHO data csv
```
scrapy crawl crawlerWHO
```

### Convert CSV to XLSX
```
python3 csv_to_xslx.py
```

## Data Only
[Kaggle](https://www.kaggle.com/jasoneliann/bangkitindonesiakucovid19realtime/settings)