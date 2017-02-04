# Django KBBI
Django KBBI adalah Kamus Besar Bahasa Indonesia yang ditulis ulang(recode) menggunakan framework django(python). Dikembangkan dari https://github.com/bgli/kbbi-qt beserta database KBBI tanpa mengubah struktur data yang telah tersedia. Alur program menggunakan Queryset ORM Django untuk fitur pencarian sebagai fitur utama. Interface HTML menggunakan material design. 

# Fitur lain yang dikembangkan
1. API Restfull yang bersifat open, dapat digunakan dan di implementasikan ke berbagai macam platform.
2. Penambahan kata dalam database, siapapun dapat bergabung sebagai admin. Memperbanyak kosa bahasa dalam database.
3. Export to File (xls, pdf, csv)
4. Offline mode , aplikasi dapat digunakan mode offline. Secara periodik database terupdate melalui service API.

# Opensource dan Pengembangan
Project yang dikembangkan adalah opensource lanjutan dari forum pembuatan kamus bahasa indonesia. Beberapa yang exist diantaranya adalah :
- http://kbbi.web.id/ by ebta setiawan (ebsoft)
- https://github.com/bgli/kbbi-qt (C++ and QT interface)

untuk berkontribusi,silahkan clone dan push buat branch baru, semisal dev, development.. dll...

# Install
```bash
1. clone atau download project git@github.com:efenfauzi/django_kbbi.git
2. cd "django_kbbi"
3. git checkout master
4. mkvirtualenv "nama_venv" 
5. source "nama_venv"
6. pip install -r requirements.txt
7. cp django_kbbi/settings.py.example --> django_kbbi/settings.py , sesuaikan dengan settingan server
8. ./manage.py migrate (migrate database untuk django)
9. ./manage.py makemigrations kbbi , lalu  ./manage.py migrate kbbi --fake (database kbbi sdh tersedia)
10. ./manage.py collectstatic, yes
11. ./manage.py runserver "port"
12. open browser
```
# ScreenShot
![Index](https://github.com/efenfauzi/django_kbbi/blob/master/screenshot/index.png)
![Pencarian Ketemu](https://github.com/efenfauzi/django_kbbi/blob/master/screenshot/pencarian_ketemu.png)
![Pencarian Tidak Ketemu](https://github.com/efenfauzi/django_kbbi/blob/master/screenshot/pencarian_tidak_ketemu.png)


