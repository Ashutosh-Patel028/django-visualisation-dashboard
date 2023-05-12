# from django.shortcuts import render

# # import viewsets
# from rest_framework import viewsets
 
# # import local data
# from .serializers import GeeksSerializer
# from .models import IndustrialData

# # create a viewset
# class GeeksViewSet(viewsets.ModelViewSet):
#     # define queryset
#     queryset = IndustrialData.objects.all()
     
#     # specify serializer to be used
#     serializer_class = GeeksSerializer


# # Create your views here.
# class dataView():


# views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import IndustrialData

def home_view(request):
    return render(request, 'base.html', {'content': 'dashboard.html'})

def data(request):
    data = list(IndustrialData.objects.all().values())
    return JsonResponse(data, safe=False)


def dashboard_view(request):
    data = list(IndustrialData.objects.all().values())
    return render(request, 'dashboard.html', {'data': data})
