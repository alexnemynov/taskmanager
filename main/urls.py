from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # обращаться через name в url шаблоне правильнее, т.к. позволяет менять адрес ссылки только в 1 месте
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
]

