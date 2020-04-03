from django.conf.urls import url
from django.urls import path
from akun import views# SET THE NAMESPACE!
app_name = 'akun' # Be careful setting the name to just /login use userlogin instead!

urlpatterns=[
    path('login/',views.login_view,name='login'),
    # path('user_login/',views.user_login,name='user_login'),
    # url(r'^register/$',views.register,name='register'),
    # url(r'^user_login/$',views.user_login,name='user_login'),
]