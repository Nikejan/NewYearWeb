from django.urls import path
from . import views
from .views import HomePageView, SearchResultsView


urlpatterns = [
    path('', views.store, name="store"),
    path("", HomePageView.as_view(), name="store"),
    path("search/", SearchResultsView.as_view(), name="product_list")
]





    
   