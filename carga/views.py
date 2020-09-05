from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from openpyxl import load_workbook
from io import BytesIO
from pprint import pprint
import datetime
from .models import Project
from .dictionaries import projects_dict_letter

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
            for row in ws.iter_rows(min_row=6, max_col=26, max_row=ws.max_row):
                project = Project()
                for cell in row:
                    check_column = cell.column in projects_dict_letter
                    if check_column:
                        if cell.column == "A":
                            project.id_project = cell.value
                        elif cell.column == "B":
                            project.name = cell.value
                        elif cell.column == "C":
                            project.description_short = cell.value
                        elif cell.column == "D":
                            project.description_long = cell.value
                        elif cell.column == "E":
                            if cell.value != None:
                                project.last_update = cell.value
                        elif cell.column == "F":
                            if cell.value != None:
                                project.registration_from = cell.value
                        elif cell.column == "G":
                            if cell.value != None:
                                project.registration_to = cell.value
                        elif cell.column == "H":
                            if cell.value != None:
                                project.created_at = cell.value
                        elif cell.column == "I":
                            project.parent_entity = cell.value
                        elif cell.column == "J":
                            project.published_by = cell.value
                        elif cell.column == "K":
                            project.project_budget = cell.value
                        elif cell.column == "L":
                            project.project_goal = cell.value
                        elif cell.column == "M":
                            project.target_audience = cell.value
                        elif cell.column == "O":
                            project.areas = cell.value
                        elif cell.column == "P":
                            project.tags = cell.value
                        elif cell.column == "Q":
                            project.verified_account = cell.value
                        elif cell.column == "R":
                            project.project_type = cell.value
                        elif cell.column == "S":
                            project.project_website = cell.value
                        elif cell.column == "T":
                            project.project_facebook = cell.value
                        elif cell.column == "U":
                            project.project_twitter = cell.value
                        elif cell.column == "V":
                            project.project_google_plus = cell.value
                        elif cell.column == "W":
                            project.project_instagram = cell.value
                        elif cell.column == "X":
                            project.stamps = cell.value
                        elif cell.column == "Y":
                            project.opportunity_tab_name = cell.value
                        elif cell.column == "Z":
                            project.uses_opportunity_tab = cell.value
                pprint(project.__str__())
                try:
                    project.validate_unique()
                    project.save()
                except:
                    None

            return HttpResponseRedirect('/carga/valeu')
    else:
        form = UploadFileForm()
    return render(request, 'index.html', {'form': form})