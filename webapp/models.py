from django.db import models

# Create your models here.
class Card(models.Model):
    card_img = models.ImageField(upload_to='media/carding/%Y')
    card_title = models.CharField(max_length=20)
    card_desc = models.TextField()

    # returns the string
    def __str__(self):
        return self.card_title




