# Django
from django.shortcuts import render
from .models import PowerData, File
from .serializers import PowerDataSerializer, FileSerializer
from django.shortcuts import get_object_or_404

# drf
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.renderers import TemplateHTMLRenderer

# Create your views here.
class Pagination(PageNumberPagination):
    pagesize = 10
    pagesize_query_param = 'page_size'
    max_page_size = 100
    
    
class PowerDataViewSet(viewsets.ModelViewSet):
    queryset = PowerData.objects.all()
    serializer_class = PowerDataSerializer
    #paginate
    pagination_class = Pagination
    
    def list(self, request, *args, **kwargs):
        powerdata_list = self.get_queryset()
        return render(request, 'powerdata_table.html', {'powerdata_list': powerdata_list})
    

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    #paginate
    pagination_class = Pagination
    
    def list(self, request, *args, **kwargs):
        file_list = self.get_queryset()
        return render(request, 'file_table.html', {'file_list': file_list})