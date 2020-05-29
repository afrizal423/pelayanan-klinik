from django.contrib import admin

# Register your models here.
from pegawaiadmin.models import Pendaftaran, Antrian, Pembayaran, BiayaPemeriksaan
# Register your models here.
admin.site.register(Antrian)
admin.site.register(Pendaftaran)
admin.site.register(Pembayaran)
admin.site.register(BiayaPemeriksaan)