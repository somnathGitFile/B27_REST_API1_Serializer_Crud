from .models import Customer
from rest_framework import serializers

class CustomerSerializer(serializers.Serializer):
    cid = serializers.IntegerField()
    cname = serializers.CharField(max_length =100)
    cmail = serializers.EmailField()
    cadd = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)


    def update (self,instance, validated_data):
        instance.cid = validated_data.get('cid', instance.cid)
        instance.cname = validated_data.get('cname', instance.cname)
        instance.cmail = validated_data.get('cmail', instance.cmail)
        instance.cadd = validated_data.get('cadd', instance.cadd)

        instance.save()
        return instance
