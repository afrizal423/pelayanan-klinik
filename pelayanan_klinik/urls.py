"""pelayanan_klinik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from pelayanan_klinik import views as pkl
from django.views.static import serve 
from django.conf import settings

admin.site.site_header="Sistem Pelayanan Klinik"
admin.site.site_title="AdminPortal | Sistem Pelayanan Klinik"
admin.site.index_title="Selamat datang di Sistem Pelayanan Klinik"


urlpatterns = [
    path('',pkl.index,name='index_klinik'),
    path('admin/', admin.site.urls),
    path('akun/', include('akun.urls',namespace="akun")),
    path('pegawaiadmin/', include('pegawaiadmin.urls',namespace="pegawaiadmin")),
    path('dokter/', include('dokter.urls',namespace="dokter")),
    path('apoteker/', include('apoteker.urls',namespace="apoteker")),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_DIR}), 

]
