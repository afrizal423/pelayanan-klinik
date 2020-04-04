from django.conf.urls import url
from django.urls import path
from . import views# SET THE NAMESPACE!
app_name = 'apoteker' # Be careful setting the name to just /login use userlogin instead!

urlpatterns=[
    path('index/',views.index,name='index_apoteker'),
    # path('logout/',views.user_logout,name='user_logout'),
    # path('user_login/',views.user_login,name='user_login'),
    # url(r'^register/$',views.register,name='register'),
    # url(r'^user_login/$',views.user_login,name='user_login'),
]