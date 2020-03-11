from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "basic.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
