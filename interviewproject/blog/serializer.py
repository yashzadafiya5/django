from rest_framework import serializers 



class BookSerializer(serializers.Serializer):
    title=serializers.CharField(label='Enter Book title')
    Author=serializers.CharField(label='Enter Book Author')