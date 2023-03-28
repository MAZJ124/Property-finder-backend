from django import forms
from .models import Poi
from django.contrib.gis.geos import Point



class PoiForm(forms.ModelForm):
    class Meta:
        model = Poi
        fields = ['name', 'type', 'location', 'latitude', 'longitude']
    latitude = forms.FloatField()
    longitude = forms.FloatField()

    def clean(self):
        data = super().clean()
        latitude = data.pop('latitude')
        longitude = data.pop('longitude')
        data['location'] = Point(latitude, longitude, srid=4326)
        return data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # To display latitude and longitude in form after listing creation
        location = self.initial.get('location')
        if isinstance(location, Point):
            self.initial['latitude'] = location.tuple[0]
            self.initial['longitude'] = location.tuple[1]
