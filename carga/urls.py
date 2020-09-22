from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agentes', views.agentes, name='agentes'),
    path('valeu',views.valeu, name='valeu'),
    path('upload_file', views.upload_file, name='upload_file'),
    path('carga_agents', views.carga_agents, name='carga_agents'),
]

app_name='carga'