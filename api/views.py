# Django
from django.shortcuts import render
from .models import PowerData
from .serializers import PowerDataSerializer
from django.shortcuts import get_object_or_404

# drf
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

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