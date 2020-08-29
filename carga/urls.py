from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('valeu',views.valeu, name='valeu'),
    path('upload-spreadsheet', views.upload_spreadsheet, name='upload-spreadsheet')
]
