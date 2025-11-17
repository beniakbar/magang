from django.urls import path
from . import views
from .auth_views import register_api, login_api, logout_api

urlpatterns = [

    # CRUD
    path('tes/', views.tes, name='tes'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # CRUD Pengguna
    path('pengguna/', views.pengguna_list, name='pengguna_list'),
    path('pengguna/tambah/', views.pengguna_create, name='pengguna_create'),
    path('pengguna/edit/<int:id>/', views.pengguna_update, name='pengguna_update'),
    path('pengguna/hapus/<int:id>/', views.pengguna_delete, name='pengguna_delete'),

    # CRUD Satpam
    path('satpam/', views.satpam_list, name='satpam_list'),
    path('satpam/tambah/', views.satpam_create, name='satpam_create'),
    path('satpam/edit/<int:id>/', views.satpam_update, name='satpam_update'),
    path('satpam/hapus/<int:id>/', views.satpam_delete, name='satpam_delete'),
]
