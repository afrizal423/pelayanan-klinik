from django.conf.urls import url
from django.urls import path
from . import views# SET THE NAMESPACE!
app_name = 'dokter' # Be careful setting the name to just /login use userlogin instead!

urlpatterns=[
    path('index/',views.index,name='index_dokter'),
    path('antrianpasien/',views.antrian,name='antrian_pasien'),
    path('periksapasien/<int:id>',views.periksa,name='periksa_pasien'),
    path('cariobat/',views.cariobat,name='cari_obat'),
    path('tambahobat/<int:id>',views.tambahobat,name='tambah_obat'),
    path('hapusobat/<int:id>',views.hapusobat,name='hapus_obat'),


    # path('logout/',views.user_logout,name='user_logout'),
    # path('user_login/',views.user_login,name='user_login'),
    # url(r'^register/$',views.register,name='register'),
    # url(r'^user_login/$',views.user_login,name='user_login'),
]