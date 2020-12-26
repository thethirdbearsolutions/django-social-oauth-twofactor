from django.conf import settings
from django.shortcuts import redirect
from django_otp import user_has_device

class TwoFactorMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response
                                                                                            
    def process_request(self, request):
        import pdb; pdb.set_trace()
        if request.user.is_verified():
            return None
        if request.user.is_anonymous:
            return redirect(settings.LOGIN_URL)            
        if not user_has_device(request.user):
            return redirect('two_factor:profile')
        return redirect('two_factor_login_step2')
