from django.http import HttpResponse

def index(request):
    return HttpResponse("Bem vindo a página de carga de dados!")

