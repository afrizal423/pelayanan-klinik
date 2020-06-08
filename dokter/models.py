from django.db import models
from pegawaiadmin.models import Antrian, Pendaftaran
from akun.models import User
# Create your models here.
class RekamMedis(models.Model):
    idantrian = models.ForeignKey(Antrian,on_delete=models.CASCADE)
    iddokter = models.ForeignKey(User,blank = True, null = True,on_delete=models.CASCADE)
    idpendaftaran = models.ForeignKey(Pendaftaran, on_delete=models.CASCADE)
    diagnosa = models.TextField(blank = True, null = True,)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return "{}. {}".format(self.idpendaftaran, self.diagnosa)

class Temp_Obat(models.Model):
    id_obat = models.IntegerField()
    nama_obat = models.TextField(blank = True, null = True,)
    jumlah_obat = models.BigIntegerField()
    harga_obat = models.BigIntegerField()
    url = models.TextField(blank = True, null = True,)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.nama_obat