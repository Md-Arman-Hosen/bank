from django.shortcuts import render
from django.http import HttpResponse
from.models import Contact
# Create your views here.
def index(request):
    return render(request,'index.html')
def banking(request):
    return render(request,'banking.html')    
def contact(request):
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact()
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
        return HttpResponse('<h1> Thanks for your Response </h1>')
    return render(request,'contact.html')
def showdata(request):
    contacts = Contact.objects.all()
    # for i in contacts:
    #     print(i.id,i.name,i.message)
    data = {'Contact': contacts}    
    return render(request,'showdata.html',data)