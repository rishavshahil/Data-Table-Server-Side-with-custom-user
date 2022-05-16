from django.shortcuts import render
from django.views import View
from django_serverside_datatable.views import ServerSideDatatableView
from django_serverside_datatable import datatable
from django_serverside_datatable.datatable import DataTablesServer 
from django.http import JsonResponse
from .models import Member

class HomeView(View):
    template_name = 'home.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

class ItemListView(ServerSideDatatableView):
    columns = ['id', 'name', 'gender', 'date_of_birth','duration', 'contact','duration_type' ]
    queryset = Member.objects.all()

