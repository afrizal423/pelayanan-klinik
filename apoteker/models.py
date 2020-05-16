from django.db import models
from dokter.models import RekamMedis

# Create your models here.
class Obat(models.Model):
    nama_obat = models.CharField(max_length=200, unique=True)
    stok_obat = models.BigIntegerField()
    harga_obat = models.BigIntegerField()
    dosis_obat = models.IntegerField()
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.nama_obat

class PemesananObat(models.Model):
    idobat = models.ForeignKey(Obat,on_delete=models.CASCADE)
    idrm = models.ForeignKey(RekamMedis,on_delete=models.CASCADE)
    jumlah_obat = models.IntegerField()
    subtotal_obat = models.BigIntegerField()
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.nama_obat