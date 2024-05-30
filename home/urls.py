from django.urls import path
from . import views


urlpatterns = [
    path('upload-exel/', views.upload_file, name='upload-exel'),
    path('table/', views.display_data, name='table-exel'),
    path('asa/', views.tesete, name='table-exel'),
]
