import datetime
from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object

class CarMake(models.Model):
    name = models.CharField(max_length=200, default="Car make")
    description = models.CharField(max_length=200, default="Description")
    def __str__(self):
        return "Name: " + self.name + "," + \
               "Description: " + self.description
    

class CarModel(models.Model):
    carmake = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default="Car Model")
    dealerId = models.PositiveIntegerField()
    YEAR_CHOICES = [(r,r) for r in range(1984, datetime.date.today().year+1)]
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    SUV = 'SUV'
    SEDAN = 'Sedan'
    HB = 'Hatchback'
    WAGON = 'Wagon'
    TYPE_CHOICES = [
        (SUV, 'SUV'),
        (SEDAN, 'Sedan'),
        (HB, 'Hatchback'),
        (WAGON, 'Wagon')
    ]
    type = models.CharField(
        null=False,
        max_length=20,
        choices=TYPE_CHOICES,
        default=SEDAN
    )
    def __str__(self):
        return "Name: " + self.name + "," 
            
# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name 

# <HINT> Create a plain Python class `DealerReview` to hold review data

class DealerReview:

    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year,sentiment,id):
        # Dealer address
        self.dealership = dealership
        # Dealer city
        self.name = name
        # Dealer Full Name

        self.purchase = purchase

        self.review = review

        self.purchase_date = purchase_date

        self.car_make = car_make
         
        # Location lat
        self.car_model = car_model
        # Location long
        self.car_year = car_year
        # Dealer short name
        self.sentiment = sentiment

        self.id = id
    def __str__(self):
        return "Dealership: " + str(self.dealership) + '\n' + \
            "Name: " + self.name + '\n' + \
            "Purchase: " + str(self.purchase) + '\n' + \
            "Review: " + self.review + '\n' + \
            "Car Make: " + self.car_make + '\n' + \
            "Car Model: " + self.car_model + \
            "Sentiment: " + self.sentiment



