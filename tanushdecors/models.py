import datetime
from django.db import models
from django.utils import timezone


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('sofa', 'Sofa'),
        ('chair', 'Chair'),
        ('table', 'Table'),
    ]

    name = models.CharField(max_length=200, verbose_name="Product Name")  # Descriptive verbose name
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0, 
        verbose_name="Product Price"
    )
    pub_date = models.DateTimeField('Date Published', default=timezone.now)  # Defaults to now

    # Image Field
    image = models.ImageField(
        upload_to='images/', 
        default='images/default.jpg',  # Ensure a default image exists
        verbose_name="Product Image"
    )

    # Category Choices
    category = models.CharField(
        max_length=10, 
        choices=CATEGORY_CHOICES, 
        null=True,  # Allows NULL in the database
        blank=True,  # Field is optional in forms
        verbose_name="Product Category"
    )

    def was_published_recently(self):
        """Returns True if the product was published within the last day."""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    # Admin attributes for the `was_published_recently` method
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published Recently?'

    def __str__(self):
        """String representation of the Product model."""
        return self.name
