from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class
class CarMakeInline(admin.StackedInline):
    model = CarMake
# CarModelAdmin class
class CarModelInline(admin.StackedInline):
    model = CarModel

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]



# Register models here
admin.site.register(CarModel)
admin.site.register(CarMake, CarMakeAdmin)