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
    year = models.DateField(null=True)
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
        return "Name: " + self.name + "," + \
            "Car maker: " + self.carmake + \
            "Model year: " + self.year + \
            "Dealer Id: " + self.dealerId + \
            "Type:" + self.type 
# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
