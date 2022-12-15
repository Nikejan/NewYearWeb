from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.views.generic import TemplateView, ListView



from .models import *

@csrf_exempt
def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)


class HomePageView(TemplateView):
    template_name = 'main.html'


class SearchResultsView(ListView):
    model = Product
    template_name = 'product_list.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Product.objects.filter(
            Q(name__icontains=query)
        )
        return object_list
    
