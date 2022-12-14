from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    phone = models.CharField(max_length=255, null=True, blank=True)
    is_client = models.BooleanField(default=True)
    is_call_center = models.BooleanField(default=False)
    is_cooker = models.BooleanField(default=False)
    is_deliver = models.BooleanField(default=False)
    is_cashier = models.BooleanField(default=False)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class Categories(models.Model):
    image = models.CharField(max_length=25)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='prod_cat')
    name = models.CharField(max_length=50)
    price = models.FloatField()
    discount = models.FloatField(null=True, blank=True)
    description = models.TextField()
    portion = models.PositiveIntegerField()
    callories = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    
class PImanges(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='image_prod')
    image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.product.name
    

class Shops(models.Model):
    sts = (
        ("opened", "opened"),
        ("booked", "booked"),
        ("canceled", "canceled"),
        ("accepted", "accepted"),
        ("sent", "sent"),
        ("sold", "sold"),
        ("paid", "paid"),
    )
    client = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='shop_user')
    total = models.FloatField(default=0)
    status = models.CharField(choices=sts, max_length=10, default='opened')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class ShopItems(models.Model):
    shop = models.ForeignKey(Shops, on_delete=models.CASCADE, related_name='shop_item')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='prod_item')
    quantity = models.IntegerField(default=1)
    total = models.FloatField()

    def __str__(self):
        return str(self.id)