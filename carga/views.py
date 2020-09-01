from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from openpyxl import load_workbook
from io import BytesIO
from pprint import pprint

def index(request):
    return render(request, 'index.html')

def valeu(request):
    return render(request, 'valeu.html')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            file_in_memory = request.FILES['file'].read()
            wb = load_workbook(filename=BytesIO(file_in_memory))
            wob = load_workbook(filename=request.FILES['file'].file)
            ws = wb.active
            for row in ws.iter_rows(min_row=6, max_col=5, max_row=10):
                print(row)

            return HttpResponseRedirect('/carga/valeu')
    else:
        form = UploadFileForm()
    return render(request, 'index.html', {'form':form})
