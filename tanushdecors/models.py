import datetime

from django.db import models
from django.utils import timezone


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('sofa', 'Sofa'),
        ('chair', 'Chair'),
        ('table', 'Table'),
    ]
    
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='images/', default='products/default.jpg')  # Default image

    category = models.CharField(
        max_length=10, 
        choices=CATEGORY_CHOICES, 
        null=True,  # Allows NULL in the database
        blank=True  # Allows the field to be optional in forms
    )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    
    def __str__(self):
        return self.name
    

