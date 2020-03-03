from rest_framework import serializers
from api.models import rock
class RockDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = rock
        fields = '__all__'


# class RockDetail...
