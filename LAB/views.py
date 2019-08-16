from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NameForm, ContactForm, CustomerForm, uploadform
from .models import Customer
import boto3
import os



def index(request):
    return render(request, 'lab/login.html')
    
def dashboard(request):
    return render(request, 'lab/index.html')

def addcustomer(request):
    if request.method == 'POST':
        print(request.POST)
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
        return customerlist(request)     
    form = CustomerForm()
    return render(request, 'lab/addcustomer.html', {'form': form})

def tests(request):
    return HttpResponse('This will be the tests page')

def uploadpage(request):
        if request.method == 'POST':
            form = uploadform(request.POST, request.FILES)
            #print(form.name)
            if form.is_valid():
                handle_uploaded_file(request.FILES['file'])
                return HttpResponse('IT Ran' )
        else:
            form =  uploadform()
            return render(request, 'lab/uploadpage.html', {'form':form})

def register(request):
    return render(request, 'lab/register.html')

def login(request):
    return render(request, 'lab/login.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('SOMETHING HERE')
    else:
        form = UserCreationForm()
    return render(request, 'lab/login.html', {'form': form})

def customerlist(request):
    #s3 = boto3.resource('s3')
    #for bucket in s3.buckets.all():
    #    print(bucket.name)
    #data = open('kitty.jpg', 'rb')
    #print(data)
    #s3.Bucket('bucketname').put_object(Key='kitty.jpg', Body=data) 

    customers = Customer.objects.all()  
    return render(request, 'lab/customerlist.html', {'customers':customers})

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # form . whatever should have the data in it?
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'lab/blank.html', {'form': form})

def contactPost(request):
    if request.method == 'POST':
        form = ContactForm()


def handle_uploaded_file(f):
    print(f)
    s3 = boto3.resource('s3')
    s3.Bucket('testfoibucket123456789').put_object(Key=f.name, Body=f) 




    #for bucket in s3.buckets.all():
  
    #with open('testfoibucket123456789', 'wb+') as destination:
     #   for chunk in f.chunks():
      #      destination.write(chunk)
       #     s3.Bucket('elasticbeanstalk-us-west-2-642171684277').put_object(Key='kitty.jpg', Body=data) 


         # acess key ID:   AKIAZLBDKIW2Y4BJRSWY
