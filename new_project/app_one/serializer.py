from rest_framework import serializers

class UserMettings(serializers.Serializer):
    title=serializers.CharField(label="Enter User Meeting Title")
    startdatetime=serializers.CharField(label="Enter Start Date and Time")
    enddatetime=serializers.CharField(label="Enter End Date and Time")
    description=serializers.CharField(label="Enter Metting Description")