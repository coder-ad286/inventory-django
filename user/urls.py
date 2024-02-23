from django.urls import path
from .views import register,profile
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('register/',register,name="user-register"),
    path('',auth_views.LoginView.as_view(template_name="user/login.html"),name="user-login"),
    path('logout/',auth_views.LoginView.as_view(template_name="user/logout.html"),name="user-logout"),
    path('profile/',profile,name="user-profile")
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)