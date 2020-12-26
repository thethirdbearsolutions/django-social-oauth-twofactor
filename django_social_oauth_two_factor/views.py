from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login
from django.shortcuts import redirect, resolve_url
from django.utils.http import is_safe_url
from two_factor import signals
from two_factor.views import core

class LoginView(core.LoginView):
    def get_user(self):
        """
        Returns the user authenticated by the AuthenticationForm. Returns False
        if not a valid user; see also issue #65.
        """
        return self.request.user

    form_list = (
        ('token', core.AuthenticationTokenForm),
        ('backup', core.BackupTokenForm),
    )

    def done(self, form_list, **kwargs):
        login(self.request,
              self.get_user(),
              backend='django.contrib.auth.backends.ModelBackend',
        )        
        redirect_to = self.request.POST.get(
            self.redirect_field_name,
            self.request.GET.get(self.redirect_field_name, '')
        )

        if not is_safe_url(url=redirect_to, allowed_hosts=[self.request.get_host()]):
            redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

        device = getattr(self.get_user(), 'otp_device', None)
        if device:
            signals.user_verified.send(sender=__name__, request=self.request,
                                       user=self.get_user(), device=device)
        return redirect(redirect_to)

def logout(request):
    auth_logout(request)
    return redirect("/")

def profile(request):
    return redirect("/")

