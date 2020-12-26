from django.shortcuts import redirect
from django_otp import user_has_device

class Admin2FAMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view, *args, **kwargs):
        if not request.path.startswith('/admin'):
            return None
        if request.user.is_verified():
            return None
        if request.user.is_anonymous:
            return None
        if not user_has_device(request.user):
            return redirect('two_factor:profile')
        return redirect('two_factor_login_step2')
