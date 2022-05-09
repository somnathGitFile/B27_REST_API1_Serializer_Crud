from .models import Student
from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    sid = serializers.IntegerField()
    sname = serializers.CharField(max_length =100)
    smail = serializers.EmailField()
    sadd = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)


    def update (self,instance, validated_data):
        instance.sid = validated_data.get('sid', instance.sid)
        instance.sname = validated_data.get('sname', instance.sname)
        instance.smail = validated_data.get('smail', instance.smail)
        instance.sadd = validated_data.get('sadd', instance.sadd)

        instance.save()
        return instance
