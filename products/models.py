from django.db import models
from django.conf import settings


class Category(models.Model):
    METHOD_NAMES = [
        ('US', 'UNITED STATE OF AMERICA'),
        ('UK', 'UNITED KINGDOM'),
        ('AUS', 'AUSTRALIA'),
        ('CHN', 'CHINA'),
    ]

    TYPE_SWIMMERS = [
        ('F', 'FAST'),
        ('SE', 'SEMI-ENDURANCE'),
        ('E', 'ENDURANCE'),
    ]

    method_name = models.CharField(max_length=255, choices=METHOD_NAMES)
    type_swimmer = models.CharField(max_length=255, choices=TYPE_SWIMMERS)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'Method: {self.method_name} | Type_swimmer: {self.TYPE_SWIMMERS}'


class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    duration = models.DurationField(default=0)
    number_of_sessions = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Title: {self.title} | Price: {self.price}'


class ActiveCommentsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentsManager, self).get_queryset().filter(active=True)


class Comment(models.Model):
    PRODUCT_STARS = [
        ('1', 'Very Bad'),
        ('2', 'Bad'),
        ('3', 'Normal'),
        ('4', 'Good'),
        ('5', 'Perfect'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS, )
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    # Custom Manager
    objects = models.Manager()
    active_comments = ActiveCommentsManager()

    def __str__(self):
        return f'Author: {self.user} | text: {self.text}'


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return f'{self.user}'
