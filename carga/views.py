from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

def index(request):
    return render(request, 'index.html')

def valeu(request):
    return render(request, 'valeu.html')

def upload_spreadsheet(request):
    if request.method == 'POST':
        return HttpResponseRedirect('valeu')

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        print('form\n',flush=True)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()
    return render(request, 'name.html', {'form': form})