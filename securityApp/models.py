from django.db import models

# Create your models here.
class Author(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    ratings = models.DecimalField(max_digits=5, decimal_places=2)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
