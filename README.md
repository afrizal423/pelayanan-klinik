<p align="right">
بِسْــــــــــــــمِ اللَّهِ الرَّحْمَنِ الرَّحِيم 
</p>

# Pelayanan Klinik
Projek ini adalah tugas akhir di semester genap TA2019/2020 mata kuliah pemrogaman framework.
## Author
- [Afrizal Muhammad Yasin](https://github.com/afrizal423)
- [Tria Nur Mayasari](https://github.com/triamay)
- [Anisa Fadilasari](https://github.com/nisafdlsr)
- [Baskara Dipa A](https://github.com/baskaradipaaa)
### ToDo List Pengerjaan Project
- [x] Landing page Login (Frontend) (Status: <b>Fix clear</b>
- [x] Login Sistem (Status: <b>Fix clear</b>) 
- [ ] Landing page dashboard admin (Frontend)
- [ ] Landing page dashboard untuk pencatatan antrian (Frontend)
- [ ] Landing page dashboard untuk edit antrian (Frontend)
- [ ] Pencatatan antrian Sistem (Backend)
- [ ] Landing page dashboard diagnosa untuk dokter (Frontend)
- [ ] Landing page dashboard detail diagnosa untuk dokter (Frontend)
- [ ] Sistem mengetahui stok obat agar dokter tau (Backend)
- [ ] Sistem mencatat diagnosa dari dokter (Backend)
- [ ] Landing page dashboard apotek untuk apoteker (Frontend)
- [x] CRUD data Obat (Status: <b>Fix clear</b>) 
- [ ] Landing page dashboard detail pemesanan obat dari dokter untuk apoteker (Frontend)
- [ ] Sistem menghitung jumlah nominal harga obat dari apoteker (Backend)
- [ ] Landing page untuk pembayaran (Frontend)
- [ ] Sistem mencatat pembayaran (Backend)
- [ ] <b> DONE!!</b> 

## Installation

Buat virtualenv terlebih dahulu
```bash
virtualenv {nama_virtual}
```
Masuk kedalam virtual
```bash
source {nama_virtual}/Scripts/activate
```
Jika menggunakan linux
```bash
virtualenv -p python3 {nama_virtual} ##untuk python3, ubuntu biasanya menggunakan ini
cd {nama_virtual}
source bin/activate
```
Install requirements menggunakan [pip](https://pip.pypa.io/en/stable/).
```bash
pip install -r requirements.txt
```
Buat database di phpmyadmin / sejenisnya dengan nama database pelayanan_klinik <br>
Lalu buka terminal, jalankan dengan perintah
```bash
python manage.py migrate && python manage.py runserver
```
## Demo <br>
[Coming soon](https://dj.afrizalmy.com)<br>
