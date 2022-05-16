from django.urls import path
from .views import HomeView, ItemListView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('data/', ItemListView.as_view(), name="data"),
]