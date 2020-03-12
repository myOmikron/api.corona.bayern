from django.http import JsonResponse
from django.views.generic import TemplateView

from api.models import County, Datum
from main import crawler


class RefreshView(TemplateView):
    def get(self, request, *args, **kwargs):
        ret = crawler.gather_data()
        if not isinstance(ret, tuple):
            return JsonResponse({"status": "failed",
                                 "message": "Problem occurred while gathering data"}, status=500)
        return JsonResponse({"status": "ok",
                             "message": "",
                             "value": {"new_county": ret[0],
                                       "new_data": ret[1]}})


class GetCountiesView(TemplateView):
    def get(self, request, *args, **kwargs):
        ret = County.objects.all()
        ret = [x for x in ret]
        return JsonResponse({"status": "ok",
                             "message": "",
                             "values": [{"id": x.id, "county_name": x.name} for x in ret]})


class GetLatestData(TemplateView):
    def get(self, request, *args, **kwargs):
        for param in request.GET:
            if param != "county_id":
                return JsonResponse({"status": "failed",
                                     "message": "Unsupported parameter"})
            try:
                county_id = int(request.GET["county_id"])
                datum = Datum.objects.filter(county=county_id).latest('date')
                return JsonResponse({"status": "ok",
                                     "message": "",
                                     "values": {"id": datum.id, "infected": datum.infected}})
            except ValueError:
                return JsonResponse({"status": "failed",
                                     "message": "Only integer are accepted"})
        counties = [x for x in County.objects.all()]
        data_list = []
        for county in counties:
            data_list.append(Datum.objects.filter(county=county.id).latest('date'))
        return JsonResponse({"status": "ok",
                             "message: "","
                             "values": [{"id": x.id,
                                         "infected": x.infected,
                                         "county_name": [y.name for y in counties if y.id == x.id][0]}
                                        for x in data_list]})
