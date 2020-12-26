from django.conf import settings
from django.shortcuts import redirect
from django_otp import user_has_device

def enforce_2fa_setup(view):
    def inner(request, *args, **kw):
        if not request.user.is_authenticated:
            return redirect(settings.LOGIN_URL)
        if request.user.is_verified():
            return view(request, *args, **kw)
        if not user_has_device(request.user):
            return redirect('two_factor:profile')
        return redirect('two_factor_login_step2')
    inner.__name__ = view.__name__
    return inner
