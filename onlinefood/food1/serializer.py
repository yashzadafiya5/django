from rest_framework import serializers 


class Bookserializer(serializers.Serializer):
    title=serializers.CharField(label="Enter A Book Title:")
    author=serializers.CharField(label="Enter Author Name:")