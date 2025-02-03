from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about, name='about'),
    path('media/', views.show_media, name='show_media'),
    path('new/', views.new_view, name='new_view'),
]
