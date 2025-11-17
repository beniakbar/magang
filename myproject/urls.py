from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from rest_framework.routers import DefaultRouter

from masterdata.api import SatpamViewSet
from masterdata.api.auth import RegisterAPI, LoginAPI
from django.views.generic import TemplateView


router = DefaultRouter()
router.register('satpam', SatpamViewSet)

def dashboard(request):
    return render(request, 'dashboard.html')


urlpatterns = [

    # HTML PAGES
    path('login/', TemplateView.as_view(template_name="login.html"), name="login_page"),
    path('register/', TemplateView.as_view(template_name="register.html"), name="register_page"),
    path('dashboard/', dashboard, name='dashboard'),

    # API AUTH
    path('api/login/', LoginAPI.as_view(), name="api-login"),
    path('api/register/', RegisterAPI.as_view(), name="api-register"),

    path('api/', include(router.urls)),

    # ADMIN
    path('admin/', admin.site.urls),

    # CRUD & halaman lain masterdata
    path('', include('masterdata.urls')),
]
