# Django KBBI
Django KBBI adalah Kamus Besar Bahasa Indonesia yang ditulis ulang(recode) menggunakan framework django(python). Dikembangkan dari https://github.com/bgli/kbbi-qt beserta database KBBI tanpa mengubah struktur data yang telah tersedia. Alur program menggunakan Queryset ORM Django untuk fitur pencarian sebagai fitur utama. Interface HTML menggunakan material design. 

# Fitur lain yang dikembangkan
1. API Restfull yang bersifat open, dapat digunakan dan di implementasikan ke berbagai macam platform.
2. Penambahan kata dalam database, siapapun dapat bergabung sebagai admin. Memperbanyak kosa bahasa dalam database.
3. Export to File (xls, pdf, csv)
4. Offline mode , aplikasi dapat digunakan mode offline. Secara periodik database terupdate melalui service API.

# Opensource dan Pengembangan
Project yang dikembangkan adalah opensource lanjutan dari kontribusi pembuatan kamus bahasa indonesia. Beberapa yang exist diantaranya adalah :
- http://kbbi.web.id/ by ebta setiawan (ebsoft)
- https://github.com/bgli/kbbi-qt (C++ and QT interface)

# Install
1. mkvirtualenv "nama_venv" 
2. source "nama_venv"
3. pip install -r requirements.txt
4. cp settings.py.example --> settings.py , sesuaikan dengan settingan server
5. ./manage.py migrate --database=default (migrate database untuk django)
6. ./manage.py migrate --database=kbbi --fake (database kbbi sdh tersedia)
7. ./manage.py collectstatic, yes
8. ./manage.py runserver "port"
9. open browser

# ScreenShot

