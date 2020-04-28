from rest_framework import serializers
from Babies.models import Baby
from Parents.models import Parent


class BabySerializer(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField()
    class Meta:
        model = Baby
        fields = (
            'id',
            'name',
            'lastName',
            'gender',
            'parent'
        )
    def get_parent(self,obj):
        return obj.parent.name + "" + obj.parent.lastName

