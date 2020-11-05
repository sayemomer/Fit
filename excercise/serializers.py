from rest_framework import serializers
from .models import Excercise

class ExcerciseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Excercise
        fields = ('id','user_id','description','duration','date')