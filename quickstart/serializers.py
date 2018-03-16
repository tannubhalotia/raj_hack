from .models import Table1
from .models import Table2
from .models import Table3
from rest_framework import serializers


class Table1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Table1
        fields = ('id', 'choice1','choice2','name')

class Table2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Table2
        fields = ('id', 'rest_names')

class Table3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Table3
        fields = ('id', 'loc_names')






