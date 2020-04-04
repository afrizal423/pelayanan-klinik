from django.contrib import admin
from .models import Akun, DataPegawai, User
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
class AkunAdmin (admin.ModelAdmin):
    list_display = ['pegawai','jenis_akun']
    list_filter = ('jenis_akun',)
    search_fields = ['pegawai','jenis_akun']
    list_per_page = 7

class DataAdmin (admin.ModelAdmin):
    list_display = ['nama','no_telepon']
    list_filter = ('jenis_kelamin','golongan_darah')
    search_fields = ['nama','alamat']
    list_per_page = 7
    
admin.site.register(Akun, AkunAdmin)
admin.site.register(DataPegawai, DataAdmin)


# Register your models here.
