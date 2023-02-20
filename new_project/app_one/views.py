from click import UUID
from django.shortcuts import render
from django.http import HttpResponse
from httpx import get
from ipware import get_client_ip
import requests
from .models import CustomUser,Event
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *

def my_view(request):
    client_ip, is_routable = get_client_ip(request)
    ip_address = "123.45.67.89"
    api_key = "your_api_key"

    url = f"http://api.ipstack.com/{ip_address}?access_key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

def index(request):
    table=CustomUser.objects.all()
    return render(request,'crud_user.html',{'table':table})

def add_user(request):
    email = request.POST.get('email')
    dob = request.POST.get('dob')
    primary_contact_number = request.POST.get('pcn')
    secondary_contact_number = request.POST.get('scn')
    currency = request.POST.get('cur')
    print(email,dob,primary_contact_number,secondary_contact_number,currency)
    
    if CustomUser.objects.filter(email=email).exists():
        return HttpResponse('-1')
    else:
        CustomUser.objects.create(email=email, date_of_birth=dob, primary_contact_number=primary_contact_number,secondary_contact_number=secondary_contact_number,currency=currency)
        return HttpResponse('1')
    
def edit_user(request,userid):
    id=request.POST.get('id')
    email = request.POST.get('email')
    dob = request.POST.get('dob')
    primary_contact_number = request.POST.get('pcn')
    secondary_contact_number = request.POST.get('scn')
    currency = request.POST.get('cur')
    print(id)
    CustomUser.objects.filter(id=id).update(email=email, date_of_birth=dob, primary_contact_number=primary_contact_number,secondary_contact_number=secondary_contact_number,currency=currency)
    return HttpResponse('user updated successfully')

def delete_user(request,newuserid):
    print(newuserid)
    CustomUser.objects.filter(id=newuserid).delete()
    return HttpResponse('user deleted.....')


def calender(request):
    return render(request,'calender.html')

class UserMeetingApiView(APIView):
    serializer_class=UserMettings
    def get(self,request):
        AllMeetings=Event.objects.all().values()
        return Response({"Message":"List Of Meetings","Meeting List":AllMeetings})
    
    def post(self,request):
        print("Request data is :",request.data)
        serializers_obj=UserMettings(data=request.data)
        if (serializers_obj.is_valid()):
            Event.objects.create(title=serializers_obj.data.get('title'),
                                start_time=serializers_obj.data.get('startdatetime'),
                                end_time=serializers_obj.data.get('enddatetime'),
                                description=serializers_obj.data.get('description'),)
        return Response({"Message":"New Meeting Added....."})
    def delete(self,request):
        Event.objects.filter(id=request.POST['id']).delete()
        return Response({"Message":"Meeting has been deleted"})
    def put(self,request):
        Event.objects.filter(id=request.POST['id']).update(title=request.POST['title'],start_time=request.POST['start_time'],end_time=request.POST['end_time'],description=request.POST['description'])
        return Response({"Message":"Meeting has been updated"})    