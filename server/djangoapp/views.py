import email
from multiprocessing import context
from sre_parse import State
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from .models import CarModel, CarMake, CarDealer, DealerReview

from django.contrib import messages
from datetime import datetime
from .restapis import get_dealers_from_cf, get_dealers_by_state, get_reviews_by_id,post_request
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.
# Create an `about` view to render a static about page
# def about(request):
def about(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/about.html', context)


# Create a `contact` view to return a static contact page
#def contact(request):
def contact(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/contact.html', context)
        
# Create a `login_request` view to handle sign in request
# def login_request(request):
def login_request(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('djangoapp:index')
        else:
            context['message'] = "Invalid username or password."
            return render(request, 'djangoapp/login.html', context)
    else:
        return render(request, 'djangoapp/login.html', context)

# Create a `logout_request` view to handle sign out request
# def logout_request(request):
def logout_request(request):
    logout(request)
    return redirect('djangoapp:index')

# Create a `registration_request` view to handle sign up request
# def registration_request(request):
def registration_request(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'djangoapp/registration.html', context)
    elif request.method == 'POST':
        # Check if user exists
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email= request.POST['email']
        user_exist = False
        try:
            if User.objects.get(username=username):
                user_exist = True
        except:
            logger.error("New user")
        if not user_exist:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,password=password, email=email)
            login(request, user)
            return redirect("djangoapp:index")
        else:
            context['message'] = "User already exists."
            return render(request, 'djangoapp/registration.html', context)


#Get all dealerships
def get_dealerships(request):
    if request.method == "GET":
        context={}
        url = "https://b97fa902.us-south.apigw.appdomain.cloud/API/dealership"
        # Get dealers from the URL
        dealerships = get_dealers_from_cf(url)

        context['dealership_list']=dealerships
        # Concat all dealer's short name
        return render(request, 'djangoapp/index.html', context)


# # # Update the `get_dealerships` view to render the index page with a list of dealerships
# def get_dealerships_by_state(request,id):
#     if request.method == "GET":
#         url = "https://b97fa902.us-south.apigw.appdomain.cloud/API/dealerships"
#         # Get dealers from the URL
#         dealerships = get_dealers_by_state(url, id)
#         # Concat all dealer's short name
#         dealer_names = ' '.join([dealer.st for dealer in dealerships])
#         # Return a list of dealer short name
#         return HttpResponse(dealer_names)




# # Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, id):
#     if request.method == "GET":
#         url = "https://b97fa902.us-south.apigw.appdomain.cloud/API/review"
#         # Get dealers from the URL
#         reviews = get_reviews_by_id(url, id)
#         # Concat all dealer's short name
#         # dealer_names = ' '.join([dealer.st for dealer in dealerships])
#         # Return a list of dealer short name
#         return HttpResponse(reviews)


def get_dealer_details(request, id):
    if request.method == "GET":
        context = {}
        dealer_url = "https://b97fa902.us-south.apigw.appdomain.cloud/API/dealerships"
        dealer = get_dealers_by_state(dealer_url, id)
        context["dealership"] = dealer
    
        review_url = "https://b97fa902.us-south.apigw.appdomain.cloud/API/review"
        reviews =  get_reviews_by_id(review_url, id)
        context["review"] = reviews
        return render(request, 'djangoapp/dealer_details.html', context)
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

def add_review(request, id):
    context = {}
    dealer_url = "https://b97fa902.us-south.apigw.appdomain.cloud/API/dealerships"
    dealer = get_dealers_by_state(dealer_url, id)
    context["dealership"] = dealer
    if request.method == 'GET':
        # Get cars for the dealer
        cars = CarModel.objects.filter(dealerId=id)
        context["cars"] = cars
        return render(request, 'djangoapp/add_review.html', context)
    elif request.method == 'POST':
        if request.user.is_authenticated:
            username = request.user.username
            payload = dict()
            car_id = request.POST["car"]
            car = CarModel.objects.get(pk=car_id)
            payload["time"] = datetime.utcnow().isoformat()
            payload["name"] = username
            payload["dealership"] = id
            payload["id"] = id
            payload["review"] = request.POST["content"]
            payload["purchase"] = False
            if "purchasecheck" in request.POST:
                if request.POST["purchasecheck"] == 'on':
                    payload["purchase"] = True
            payload["purchase_date"] = request.POST["purchasedate"]
            payload["car_make"] = car.carmake.name
            payload["car_model"] = car.name
            payload["car_year"] = car.year
            new_payload = {}
            new_payload["review"] = payload
            review_post_url = "https://b97fa902.us-south.apigw.appdomain.cloud/API/review"
            post_request(review_post_url, new_payload, id=id)
        return redirect("djangoapp:dealer_details", id=id)