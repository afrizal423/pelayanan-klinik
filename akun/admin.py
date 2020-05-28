from django.contrib import admin
from .models import Akun, DataPegawai, User
from django.contrib.auth.admin import UserAdmin

class ProfileInline(admin.StackedInline):
    model = Akun
    can_delete = True
    verbose_name_plural = 'Profile'
    fk_name = 'akun'

class UserAdmini(UserAdmin):
    # inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserAdmini, self).get_inline_instances(request, obj)

    list_display = ['username','is_active','is_pegawaiadmin', 'is_dokter', 'is_apoteker']
    search_fields = ['username']
    list_per_page = 5
    fieldsets = (
        (('Personal info'), {'fields': ('username',)}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'is_pegawaiadmin', 'is_dokter', 'is_apoteker')}),
        (('Important dates'), {'fields': ('date_joined', 'last_login')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_pegawaiadmin', 'is_dokter', 'is_apoteker'),
        }),
    )

admin.site.register(User, UserAdmini)
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
