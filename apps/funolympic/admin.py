from django.contrib import admin
from .models import Category, OlympicGame, FeaturedCategory

# Register your models here.
admin.site.register([Category])
admin.site.register([OlympicGame])
admin.site.register([FeaturedCategory])