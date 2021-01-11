from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Quotes
from django.db.models import Q

class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Quotes
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Quotes.objects.filter(
            Q(topic__icontains=query) | Q(quotation__icontains=query) | Q(by__icontains=query)
        )
        return object_list
