import urllib.request
from django.shortcuts import redirect
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from django.urls import reverse


def google_callback(request):
    params = urllib.parse.urlencode(request.GET)
    print(params)
    return redirect (f'http://localhost:3000/google/{params}')

class GoogleConnect(SocialLoginView):
    client_class = OAuth2Client
    adapter_class = GoogleOAuth2Adapter

    @property
    def callback_url(self):
        return self.request.build_absolute_uri(reverse('google_callback'))


        