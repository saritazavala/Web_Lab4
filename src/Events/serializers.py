from rest_framework import serializers
from Babies.models import Baby
from Parents.models import Parent
from Events.models import Event

class EventSerializer(serializers.ModelSerializer):
    baby = serializers.SerializerMethodField()
    class Meta:
        model = Event
        fields = (
            'id',
            'description',
            'type',
            'date',
            'baby'
        )
    def get_baby(self,obj):
        return obj.baby.name + "" + obj.baby.lastName

