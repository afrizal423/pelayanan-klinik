<p align="right">
بِسْــــــــــــــمِ اللَّهِ الرَّحْمَنِ الرَّحِيم 
</p>

# Pelayanan Klinik :hospital:
Projek ini adalah tugas akhir di semester genap TA2019/2020 mata kuliah pemrogaman framework.
## Author :computer:
- [Afrizal Muhammad Yasin](https://github.com/afrizal423)
- [Tria Nur Mayasari](https://github.com/triamay)
- [Anisa Fadilasari](https://github.com/nisafdlsr)
- [Baskara Dipa A](https://github.com/baskaradipaaa)

### User Level :boy: :woman:
- Pegawai Administrasi
- Dokter
- Apoteker

### Action Setiap User :paperclip:
User  | Aksi
------------- | -------------
Pegawai admin  | Mengelola akun user(pegawai klinik)
Pegawai admin  | Mengelola biodata user(pegawai klinik)
Pegawai admin  | Mengelola data pasien
Pegawai admin  | Mengelola antrian pasien
Pegawai admin  | Mengelola pembayaran
Dokter  | Mendiagnosa penyakit pasien
Dokter  | Mengelola obat yang tepat untuk pasien
Apotek | Mengelola data obat
Apotek | Mengelola data pemesanan obat(dari dokter)
Apotek | Mengelola data biaya obat(akan diteruskan ke pembayaran di pegawai admin)

### Fitur Aplikasi :package:
- Manajemen Pasien
  - Mencatat rekam medis
  - Mencatat history transaksi
- Manajemen Pemeriksaan
  - Mencatat diagnosa dari dokter
  - Mencatat obat yang dibutuhkan
  - Mencatat obat yang tersedia dari apoteker
 - Manajemen Apoteker
  - Mengelola obat(stok, jumlah, harga,dll)

### Poli yang tersedia :telescope:
- Poli Umum
- Poli Gigi

### Workflow :gem:
- pasien datang ke klinik
- pasien datang lalu menuju ke pendaftaran (pegawai admin)
- pegawai admin akan mencatat keluhan / gejala pasien 
- pegawai admin menentukan tujuan poli
- pasien menunggu pemanggilan secara manual di depan poli tujuan
- pasien masuk ke ruangan poli setelah di panggil
- pemeriksaan oleh dokter
- dokter mengisi pada halaman diagnosa
- dokter menentukan obat untuk pasien ( dokter juga bisa melihat stok dari obat )
- pasien menuju ke ruangan pembayaran 
- pasien menunggu untuk pemangilan pembayaran
- selama proses menunggu, data obat yang diisi oleh dokter akan diteruskan ke bagian apotek
- apotek akan menyiapkan obat
- ketika selesai,apotek mengirim data harga ke bagian pembayaran.
- pegawai admin akan mengecek semua data dari dokter maupun apotek
- pegawai admin memanggil pasien untuk pembayaran
- pasien akan akan membayar
- <b><i>Jika pasien adalah dari poli gigi</i></b> maka setelah selesai pembayaran bisa meninggalkan klinik <b>(proses selesai)</b>
- pasien akan diberikan sebuah nota yang akan dikasih ke apotek
- apotek akan melihat nota tersebut dan memberikan obatnya
- pasien meninggalkan klinik

### ToDo List Pengerjaan Project :pushpin:

<b><i>Untuk lebih detailnya setiap perubahan, bisa dicek pada [Commit](https://github.com/afrizal423/pelayanan-klinik/commits/develop)</i></b>

- [x] Landing page Login (Frontend) (Status: <b>Fix clear</b>)
- [x] Login Sistem (Status: <b>Fix clear</b>) 
- [x] Landing page dashboard admin (Frontend) (Status: Pengembangan lagi)
- [x] Landing page dashboard untuk pencatatan antrian (Frontend)
- [x] Landing page dashboard untuk edit antrian (Frontend)
- [x] Pencatatan antrian Sistem (Backend)
- [x] Landing page dashboard diagnosa untuk dokter (Frontend)
- [x] Landing page dashboard detail diagnosa untuk dokter (Frontend)
- [x] Sistem mengetahui stok obat agar dokter tau (Backend)
- [x] Sistem mencatat diagnosa dari dokter (Backend) <b>Proggres</b>
- [x] Landing page dashboard apotek untuk apoteker (Frontend) (Status: Pengembangan lagi)
- [x] CRUD data Obat (Status: <b>Fix clear</b>) 
- [x] Landing page dashboard detail pemesanan obat dari dokter untuk apoteker (Frontend)
- [x] Sistem menghitung jumlah nominal harga obat dari apoteker (Backend)
- [x] Landing page untuk pembayaran (Frontend)
- [x] Sistem mencatat pembayaran (Backend)
- [x] Print pembayaran
- [x] <b> DONE!!</b> 

## Installation

Buat virtualenv terlebih dahulu (Windows)
```bash
virtualenv {nama_virtual}
```
Masuk kedalam virtual (Windows)
```bash
source {nama_virtual}/Scripts/activate
```
Jika menggunakan linux
```bash
virtualenv -p python3 {nama_virtual} ##untuk python3, ubuntu biasanya menggunakan ini
source {nama_virtual}/bin/activate
```
Install requirements menggunakan [pip](https://pip.pypa.io/en/stable/).
```bash
pip install --upgrade pip
pip install --upgrade setuptools
pip install -r requirements.txt
```
Buat database di phpmyadmin / sejenisnya dengan nama database pelayanan_klinik <br>
Buka terminal untuk collectstatic
```bash
python manage.py collectstatic 
```
tetap pada terminal, jalankan perintah migrasi
```bash
python manage.py makemigrations && python manage.py migrate
```
Jalankan server
```bash
python manage.py runserver
```
<b>Jika error saat deploy</b> <br>
[dikarenakan cairocffi](https://stackoverflow.com/questions/29596426/how-to-pip-install-cairocffi)

## Demo <br>
[Demo in here](https://klinik.dj.afrizalmy.com/)<br>
