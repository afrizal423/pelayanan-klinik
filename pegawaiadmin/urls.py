from django.conf.urls import url
from django.urls import path
from pasien import views as ps
from . import views# SET THE NAMESPACE!
app_name = 'pegawaiadmin' # Be careful setting the name to just /login use userlogin instead!

urlpatterns=[
    path('index/',views.index,name='index_pegawaiadmin'),
    path('dtpasien/',ps.index,name='index_pasien'),
    path('antrian/',views.antrian,name='index_antrian'),
    path('pembayaran/',views.pembayaran,name='pembayaran'),
    path('historypembayaran/',views.history,name='history'),
    path('pembayaran/<int:id>/bayar',views.detailbayar,name='detail_pembayaran'),
    path('tambahantrian/',views.tbantrian,name='tambahantrian'),
    path('tambahpasien/',ps.tambah_pasien,name='tambahpasien'),
    path('pdf/',views.generate_pdf,name='pdf2'),
    path('print/<int:id>/pdf',views.generate_pdf,name='pdf'),
    path('hapuspasien/<int:id>',ps.hapus_pasien,name='hapuspasien'),
    path('editpasien/<int:id>',ps.edit_pasien,name='editpasien'),


    # path('logout/',views.user_logout,name='user_logout'),
    # path('user_login/',views.user_login,name='user_login'),
    # url(r'^register/$',views.register,name='register'),
    # url(r'^user_login/$',views.user_login,name='user_login'),
]