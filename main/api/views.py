from django.http import JsonResponse
from django.views.generic import TemplateView

from main import crawler


class RefreshView(TemplateView):
    def get(self, request, *args, **kwargs):
        ret = crawler.gather_data()
        return JsonResponse({"status": "ok",
                             "message": "",
                             "value": {"new_county": ret[0],
                                       "new_data": ret[1]}})
