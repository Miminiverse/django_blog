
from django.contrib import admin
from django.urls import path, include
from frontend import views as frontend_views
from django.contrib.auth import views as auth_views
from allauth.socialaccount.providers.google import views as google_views
from .views import google_callback, GoogleConnect
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('blog', include('blog.urls', namespace='blog')),
    path('api/', include('blog_api.urls', namespace='blog_api')),
    path('home/', frontend_views.list, name='home'),
    path('', auth_views.LoginView.as_view(template_name='frontend/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='frontend/logout.html'), name = 'logout'), 
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    
    path('accounts/', include('allauth.urls')),
    path('auth/login', google_views.oauth2_login, name='google_login'),
    path('auth/login/callback/', google_callback, name='google_callback'),
    path('google/connect', GoogleConnect.as_view(), name='google_connect'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
