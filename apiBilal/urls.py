from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('home', views.index, name='home'),
    path('nuevolibro', views.nuevolibro, name='nuevolibro'),
    path('nuevoprestamo', views.nuevoprestamo, name='nuevoprestamo'),
    path('addlibro', views.addlibro, name='addlibro'),
    path('addprestamo', views.addprestamo, name='addprestamo'),
    path('editarlibro', views.accioneslibro, name='editarlibro'),
    path('modlibro', views.modlibro, name='modlibro'),
    path('editarprestamo', views.accionesprestamo, name='editarprestamo'),
    path('modprestamo', views.modprestamo, name='modprestamo'),
    path('verlibros', views.verlibros, name='verlibros'),
    path('verprestamos', views.verprestamos, name='verprestamos'),
    path('accioneslibro', views.accioneslibro, name='accioneslibro'),
    path('accionesprestamo', views.accionesprestamo, name='accionesprestamo'),
    path('test_template', views.test_template, name='test_template'),
    path('authError', views.authError, name='authError'),
    path('logout', views.logout, name='logout')
]
