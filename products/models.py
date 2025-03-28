from django.db import models
from django.conf import settings


class Category(models.Model):
    METHOD_NAMES = [
        ('GYM', 'SWIM BODYBUILDING'),
        ('US', 'UNITED STATE OF AMERICA'),
        ('UK', 'UNITED KINGDOM'),
        ('AUS', 'AUSTRALIA'),
        ('CHN', 'CHINA'),
    ]

    TYPE_SWIMMERS = [
        ('بانوان', 'FEMALE'),
        ('آقایان', 'MALE'),
        ('سرعتی', 'FAST'),
        ('نیمه استقامتی', 'SEMI-ENDURANCE'),
        ('استقامتی', 'ENDURANCE'),
    ]

    method_name = models.CharField(max_length=255, choices=METHOD_NAMES)
    type_swimmer = models.CharField(max_length=255, choices=TYPE_SWIMMERS)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'Method: {self.method_name} | Type_swimmer: {self.type_swimmer}'


class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    duration = models.CharField(max_length=255)
    number_of_sessions = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Title: {self.title} | Method: {self.category.method_name} | Type_swimmer: {self.category.type_swimmer}'


class PurchaseFile(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    pdf_file = models.FileField(verbose_name='Product PDF File', upload_to='product/product_pdf/')

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return f'{self.user}'
