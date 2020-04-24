from django.contrib import admin

# Register your models here.
from pegawaiadmin.models import Pendaftaran, Antrian
# Register your models here.
admin.site.register(Antrian)
admin.site.register(Pendaftaran)