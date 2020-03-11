import requests
from bs4 import BeautifulSoup
from django.db import IntegrityError

from api.models import Location, Datum

link = "https://www.lgl.bayern.de/gesundheit/infektionsschutz/infektionskrankheiten_a_z/coronavirus/" \
       "karte_coronavirus/index.htm"


def gather_data():
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.find_all(name="table")[0]
    rows = data.find_all(name="tr")
    data_list = []
    for row in rows:
        cells = row.find_all(name="td")
        if not cells:
            continue
        data_list.append((str(cells[0].string.replace(u'\ufeff', '')), int(cells[1].string)))
    data_list = data_list[:-1]

    loc_counter = data_counter = 0
    for entry in data_list:
        loc = Location(name=entry[0])
        try:
            loc.save()
            loc_counter += 1
        except IntegrityError:
            loc = Location.objects.filter(name=entry[0])[0]

        if Datum.objects.filter(location=loc).filter(infected=entry[1]):
            continue
        datum = Datum(infected=entry[1], location=loc)
        try:
            datum.save()
            data_counter += 1
        except IntegrityError:
            pass

    return loc_counter, data_counter