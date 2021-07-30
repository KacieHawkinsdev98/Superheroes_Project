from django.db import models

# Create your models here.


class Superheroes(super_heroes.Superheroes):
     name = super_heroes.Charfield(max_length=50)
     