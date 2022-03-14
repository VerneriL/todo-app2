# API = Application Programming Interface

from rest_framework import serializers, viewsets

from .models import Tehtava


class TehtavaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tehtava
        fields = ['otsikko', 'tehty',] # 'kategoria', 


class TehtavaViewSet(viewsets.ModelViewSet):
    queryset = Tehtava.objects.all()
    serializer_class = TehtavaSerializer