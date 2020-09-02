from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from openpyxl import load_workbook
from io import BytesIO
from pprint import pprint

projects_dict = {'A' : 'id_project',
              'B' : 'name',
              'C' : 'description_short',
              'D' : 'description_long',
              'E' : 'last_update',
              'F' : 'registration_from',
              'G' : 'registration_to',
              'H' : 'created_at',
              'I' : 'parent_entity',
              'J' : 'published_by',
              'K' : 'project_budget',
              'L' : 'project_goal',
              'M' : 'target_audience',
              'O' : 'areas',
              'P' : 'tags',
              'Q' : 'verified_account',
              'R' : 'project_type',
              'S' : 'project_website',
              'T' : 'project_facebook',
              'U' : 'project_twitter',
              'V' : 'project_googleplus',
              'W' : 'project_instagram',
              'X' : 'stamps',
              'Y' : 'opportunity_tab_name',
              'Z' : 'uses_opportunity_tab'
              }

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
                for cell in row:
                    print(cell.value)

            return HttpResponseRedirect('/carga/valeu')
    else:
        form = UploadFileForm()
    return render(request, 'index.html', {'form':form})
