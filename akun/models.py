from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_pegawaiadmin = models.BooleanField(default=False)
    is_dokter = models.BooleanField(default=False)
    is_apoteker = models.BooleanField(default=False)

# Create your models here.
class DataPegawai(models.Model):
    JENIS_KELAMIN_CHOICES = (
        ('pria', 'Pria'),
        ('wanita', 'Wanita'),
    )
    GOLDAR_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
    )
    # user = models.OneToOneField(User,on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    alamat = models.TextField(blank=True)
    jenis_kelamin = models.CharField(max_length=10, choices=JENIS_KELAMIN_CHOICES)
    golongan_darah = models.CharField(max_length=10, choices=GOLDAR_CHOICES)
    no_telepon = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.nama

class Akun (models.Model):
    JENIS_AKUN_CHOICES = (
        ('dokter', 'Dokter'),
        ('pegawai_admin', 'Pegawai Admin'),
        ('pegawai_apotek', 'Pegawai Apotek'),
    )
    akun = models.ForeignKey(User,on_delete=models.CASCADE)
    pegawai = models.ForeignKey(DataPegawai,on_delete=models.CASCADE)
    jenis_akun = models.CharField(max_length=20, choices=JENIS_AKUN_CHOICES)
    is_pegawaiadmin = models.BooleanField(default=False)
    is_dokter = models.BooleanField(default=False)
    is_apoteker = models.BooleanField(default=False)

    def __unicode__(self):
        return self.DataPegawai.nama
