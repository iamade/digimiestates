from django.shortcuts import render
from rest_framework import viewsets

from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from estates.serializers import EstateSerializer
from estates.models import Estatedata

# Create your views here.

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    instance = Estatedata.objects.all()
    data = {}
    if instance:
        data = EstateSerializer(instance)
    return Response(data)

# class EstateViewSet(viewsets.ModelViewSet):
#     queryset = Estatedata.objects.all()
#     serializer_class = EstateSerializer


