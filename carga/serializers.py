from .models import AgentData
from rest_framework import serializers


class AgentDataSerializer(serializers.ModelSerializer):

    latitude = serializers.NestedBoundField

    class Meta:
        model = AgentData
        fields = ('id', 'name', 'createTimestamp', 'parent', 'geoMunicipio', 'latitude', 'longitude')
        depth = 2