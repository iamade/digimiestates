from rest_framework import serializers
from .models import Estatedata

class EstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estatedata
        fields = ['id', 
                  'first_name_of_estate_representative',
                  'last_name_of_estate_representative',
                  'phone_number',
                  'picture',
                  'estate_name',
                  'estate_location',
                  'excos',
                  'number_of_excos',
                  'estate_worker',
                  'number_of_estate_workers',
                  'residents',
                  'number_of_residents']