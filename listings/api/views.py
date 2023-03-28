from .serializers import ListingSerializer
from listings.models import Listing, Poi
from rest_framework import generics
from listings.scripts import Scripts
from django.contrib.gis.geos import Point
from rest_framework.response import Response
from rest_framework.decorators import api_view

class ListingList(generics.ListAPIView):
    queryset = Listing.objects.all().order_by('-date_posted')
    serializer_class = ListingSerializer

class ListingCreate(generics.CreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class ListingDetail(generics.RetrieveAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class ListingDelete(generics.DestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class ListingUpdate(generics.UpdateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

@api_view()
def create_initial_pois(self):
    all_names, all_types, all_lat, all_lng = Scripts.create_pois()
    for i in range(len(all_names)):
        poi = Poi(name=all_names[i], type=all_types[i], location=Point(all_lat[i], all_lng[i]))
        poi.save()
    return Response({"message": "Hello for today! See you tomorrow!"})
    
