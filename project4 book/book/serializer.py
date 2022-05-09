from .models import Book
from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    bid = serializers.IntegerField()
    bname = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    bqty = serializers.IntegerField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.bid = validated_data.get('bid', instance.bid)
        instance.bname = validated_data.get('bname', instance.bname)
        instance.author = validated_data.get('author', instance.author)
        instance.bqty = validated_data.get('bqty', instance.bqty)
        print(validated_data.get('bid', instance.bid))
        print(validated_data.get('bname', instance.bname))

        instance.save()
        return instance