from rest_framework import serializers
from Babies.models import Baby
from Parents.models import Parent


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = (
            'id',
            'name',
            'lastName',
            'user'
        )


