from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from openpyxl import load_workbook
from io import BytesIO
from .services import Service
import json

def index(request):
    form = UploadFileForm
    return render(request, 'index.html', {'form': form})

def agentes(request):
    return render(request, 'carga_agentes.html')

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
                agents_columns = Service.fill_agent_dict(ws)
                objects_list = Service.parse_agent(ws, agents_columns)
            else:
                objects_list = None

            if objects_list is not None:
                print("\tdentro do if")
                for obj in objects_list:
                    print("\t\t{}".format(obj.__str__()))
                    try:
                        if obj.save():
                            print(obj.__str__())
                    except:
                        None
            return HttpResponseRedirect('/carga/valeu')
    else:
        form = UploadFileForm()

    return render(request, 'index.html', {'form': form})

"""
    This method should be available only if there is no data in the database or user wants to load the agent data from
    Mapa Cultural do Ceará.
"""
# def carga_agents(request):
#     if request.method == 'POST':
#         dados_agentes = open('data/agent_data.json', encoding='utf-8')
#         agents_json = json.load(dados_agentes)
#         agents = []
#         agents = Service.parse_agent_json1(agents_json)

#         for agent in agents:
#             print(agent)
#             if agent is not None:
#                 agent.save()

#     if len(agents) > 0:
#         HttpResponseRedirect('/carga/agentes')

#     return HttpResponseRedirect('/carga/valeu')

"""

"""
def carga_agents(request):
    if request.method == 'POST':
        # dados_agentes = open('data/agent_data.json', encoding='utf-8')
        # agents_json = json.load(dados_agentes)
        agents = []
        agents = Service.load_agents2()

        for agent in agents:
            print(agent)
            if agent is not None:
                agent.save()

    if len(agents) > 0:
        HttpResponseRedirect('/carga/agentes')

    return HttpResponseRedirect('/carga/valeu')