from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *


# Create your views here.
class BookApiView(APIView):
    serializers_class=BookSerializer
    def get(self,request):
        allbooks=Book.objects.all().values()
        return Response({'Message':'All Books','Books':allbooks})
    
    def post(self,request):
        print(request.data)
        serializers_obj=BookSerializer(data=request.data)
        if (serializers_obj.is_valid()):
            Book.objects.create(title=serializers_obj.data.get('title'),
                                Author=serializers_obj.data.get('Author'))
        # book=Book.objects.all().values()
        return Response({'Message':'Book Added.....'})
    
    
