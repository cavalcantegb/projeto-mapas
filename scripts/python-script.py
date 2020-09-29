from unidecode import unidecode
from carga.models import Edital

def run():
    file = open('data/_0_acessibilidade', encoding="utf-8")
    acessibilidade = file.readlines()

    for row in acessibilidade:
        elements = row.split(";")
        edital = Edital()
        edital.number = elements[0].replace("\"", "")
        edital.subscription_number = unidecode(elements[1].replace("\"", "").upper().strip())
        edital.project_name = unidecode(elements[2].replace("\"", "").upper().strip())
        edital.user_name = unidecode(elements[3].replace("\"", "").upper().strip())
        edital.city = unidecode(elements[4].replace("\"", "").upper().strip())
        edital.neighbourhood = ""
        edital.points = elements[5].replace("\"", "").replace(",",".")
        edital.status = elements[6].replace("\"", "")
        edital.edital_type = "acessibilidade"
        edital.save()

    file = open('data/_1_capital', encoding="utf-8")
    acessibilidade = file.readlines()

    for row in acessibilidade:
        elements = row.split(";")
        edital = Edital()
        edital.number = elements[0].replace("\"", "")
        edital.subscription_number = unidecode(elements[1].replace("\"", "").upper().strip())
        edital.project_name = unidecode(elements[2].replace("\"", "").upper().strip())
        edital.user_name = unidecode(elements[3].replace("\"", "").upper().strip())
        edital.city = "FORTALEZA"
        edital.neighbourhood = unidecode(elements[4].replace("\"", "").upper().strip())
        edital.points = elements[5].replace("\"", "").replace(",",".")
        edital.status = elements[6].replace("\"", "")
        edital.edital_type = "capital"
        edital.save()

    file = open('data/_2_interior', encoding="utf-8")
    acessibilidade = file.readlines()

    for row in acessibilidade:
        elements = row.split(";")
        edital = Edital()
        edital.number = elements[0].replace("\"", "")
        edital.subscription_number = unidecode(elements[1].replace("\"", "").upper().strip())
        edital.project_name = unidecode(elements[2].replace("\"", "").upper().strip())
        edital.user_name = unidecode(elements[3].replace("\"", "").upper().strip())
        edital.city = unidecode(elements[4].replace("\"", "").upper().strip())
        edital.neighbourhood = ""
        edital.points = elements[5].replace("\"", "").replace(",",".")
        edital.status = elements[6].replace("\"", "")
        edital.edital_type = "interior"
        edital.save()