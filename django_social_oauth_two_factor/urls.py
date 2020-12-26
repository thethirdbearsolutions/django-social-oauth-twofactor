from django.conf import settings
from django.conf.urls import url
from django.urls import path, include
from two_factor.urls import urlpatterns as tf_urls
from two_factor.gateways.twilio.urls import urlpatterns as tf_twilio_urls

from . import views

urlpatterns = [
    url('', include(settings.ORIGINAL_ROOT_URLCONF)),
    path('account/two_factor/login/', views.LoginView.as_view(),         
         name='two_factor_login_step2'),
    path('accounts/logout/', views.logout, name='logout'),
    path('accounts/profile/', views.profile),    
    url(r'', include(tf_urls)),
    url(r'', include(tf_twilio_urls)),
    url('', include('social_django.urls', namespace='social')),
]

