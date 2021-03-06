from django.db import models
from django.contrib.auth.models import User
from profiles.models import UserProfile

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=250)
    GENDER_CHOICES = [
        ('man', 'Man'),
        ('woman', 'Woman'),
        ('other', 'Other'),
    ]
    RATING_CHOICES = [
        (1, 'Poor'),
        (2, 'Average'),
        (3, 'Good'),
        (4, 'Very Good'),
        (5, 'Excellent'),
    ]
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES)
    brand_name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    color = models.CharField(max_length=10, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    size = models.TextField(default="", null=True, blank=True)
    quantity = models.IntegerField(default=1)
    image_url = models.URLField(max_length=1024, null=True,
                                blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


RATE_CHOICES = [
    (1, '1 - Poor'),
    (2, '2 - Average'),
    (3, '3 - Good'),
    (4, '4 - Very Good'),
    (5, '5 - Excellent'),
]


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.CharField(max_length=250, blank=True)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, default=3)
    time_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wished_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.wished_product.name
