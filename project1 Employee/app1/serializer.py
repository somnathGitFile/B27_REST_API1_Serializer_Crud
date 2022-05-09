from unittest.util import _MAX_LENGTH
from .models import Employee
from rest_framework import serializers

class EmployeeSerializer(serializers.Serializer):
    eid = serializers.IntegerField()
    ename = serializers.CharField(max_length =100)
    eadd = serializers.CharField(max_length=500)
    esal = serializers.FloatField()

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update (self,instance, validated_data):
        instance.eid = validated_data.get('eid', instance.eid)
        instance.ename = validated_data.get('ename', instance.ename)
        instance.eadd = validated_data.get('eadd', instance.eadd)
        instance.esal = validated_data.get('esal', instance.esal)

        instance.save()
        return instance
