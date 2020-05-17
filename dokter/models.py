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