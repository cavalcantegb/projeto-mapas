from unidecode import unidecode
from carga.models import Bairro

def run():
    file = open('data/idh_bairros', encoding="utf-8")
    bairros = file.readlines()

    for row in bairros:
        elements = row.split(",")
        bairro = Bairro()
        bairro.name = unidecode(elements[0].replace("\"", "").upper().strip())
        bairro.idh = elements[1].replace("\"", "")
        bairro.save()
