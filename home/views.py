from django.shortcuts import render
from django.views import View
from django_serverside_datatable.views import ServerSideDatatableView
from .models import Member
from django.http import JsonResponse
from django_serverside_datatable import datatable
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
class HomeView(View):
    template_name = 'home.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class ItemListView(ServerSideDatatableView):
    columns = ['id', 'name', 'gender', 'date_of_birth','duration', 'contact','categories__title','duration_type' ]
    # queryset = Member.objects.all()

    def get(self, request, *args, **kwargs):
        category = request.GET.get('category')
        if category :
            self.queryset = Member.objects.filter(categories__title=category)
        else:
            self.queryset = Member.objects.all()
        #------------------------------------ 
        result = datatable.DataTablesServer(
            request, self.columns, self.get_queryset()).output_result()
        return JsonResponse(result, safe=False)

