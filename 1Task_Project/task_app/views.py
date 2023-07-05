from django.shortcuts import render
from rest_framework.response import Response
from .models import Region,State,Zone,District
from task_app.serializers import StateSerializer,RegionSerializer,ZoneSerializer,DistrictSerializer
from rest_framework.decorators import api_view,authentication_classes,permission_classes
# Create your views here.

@api_view(['GET'])
def GetRegion(request):
    region = Region.objects.all()
    serializer = RegionSerializer(region,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GetState(request):
    region = request.query_params.get('region')
    states = State.objects.filter(region__region__iexact=region,region__region__icontains=region)
    serializer = StateSerializer(states, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GetZone(request):
    state = request.query_params.get('state')
    zone =Zone.objects.filter(state__state__iexact= state)
    serializer = ZoneSerializer(zone, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GetDistrict(request):
    zone = request.query_params.get('zone')
    district = District.objects.filter(zone__zone__iexact=zone)
    serializer = DistrictSerializer(district, many=True)
    return Response(serializer.data)
