from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from openpyxl import load_workbook
from io import BytesIO
from .services import Service


def index(request):
    form = UploadFileForm
    return render(request, 'index.html', {'form': form})


def valeu(request):
    return render(request, 'valeu.html')


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form_data = form.cleaned_data
            file_in_memory = form_data['file'].read()
            wb = load_workbook(filename=BytesIO(file_in_memory))
            ws = wb.active
            print(form_data['table'])
            if form_data['table'] == 'project':
                objects_list = Service.parse_projects(ws)
            elif form_data['table'] == 'agent':
                objects_list = Service.parse_agent(ws)
            else:
                objects_list = None

            if objects_list is not None:
                print("\tdentro do if")
                for obj in objects_list:
                    print("\t\t{}".format(obj.__str__()))
                    if obj.save():
                        print(obj.__str__())
            return HttpResponseRedirect('/carga/valeu')
    else:
        form = UploadFileForm()

    return render(request, 'index.html', {'form': form})