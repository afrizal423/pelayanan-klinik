from django.contrib.auth.decorators import login_required, user_passes_test
from akun.models import Akun

user_login_required = user_passes_test(lambda Akun: Akun.is_pegawaiadmin, login_url='/akun/login')

def pegawaiadmin_area(view_func):
    decorated_view_func = login_required(user_login_required(view_func))
    return decorated_view_func