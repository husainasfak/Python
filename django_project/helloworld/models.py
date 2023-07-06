from django.db import models

# Create your models here.
# Used class to make models


class Book(models.Model):
    # String representation of the model
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)
    price = models.IntegerField()
    img = models.ImageField(default='default.jpg', upload_to='book_images/')
