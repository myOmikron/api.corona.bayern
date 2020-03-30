import requests
import json
from api.models import County, Datum
from background_task import background

ENDPOINT = "https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_Landkreisdaten/FeatureServer/0/query?where=BL_ID%3D9&geometryType=esriGeometryEnvelope&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&outFields=*&returnGeometry=false&returnCentroid=false&featureEncoding=esriDefault&multipatchOption=xyFootprint&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&returnZ=false&returnM=false&returnExceededLimitFeatures=true&sqlFormat=none&f=json"


def receive_data():
    ret = requests.get(ENDPOINT)
    if ret.status_code != 200:
        raise ConnectionError
    decoded = json.loads(ret.text)
    return [x["attributes"] for x in decoded["features"]]


@background
def process_data():
    data = receive_data()
    county_list = [x["GEN"] for x in data]
    county_list_db = [x for x in County.objects.all()]
    for county in county_list:
        if county ==
    c = County()


    d = Datum()
    d.date = data["last_update"]
    d.cases = data["cases"]
    d.cases_per_100k = data["cases_per_100k"]
    d.cases_per_population = data["cases_per_population"]
    d.deaths = data["deaths"]
    d.death_rate = data["death_rate"]
    d.county = data["GEN"]
    d.county_population = data["EWZ"]
    d.save()


if __name__ == '__main__':
    print(receive_data())
