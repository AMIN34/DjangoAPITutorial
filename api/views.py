# Django
from django.shortcuts import render
from .models import PowerData, File
from .serializers import PowerDataSerializer, FileSerializer
from django.shortcuts import get_object_or_404

# drf
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser, FormParser

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
    

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    #paginate
    pagination_class = Pagination