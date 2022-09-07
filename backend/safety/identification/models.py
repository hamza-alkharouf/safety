from django.db import models
# Create your models here.
class PaymentMethod(models.Model):

    payment_method = models.CharField(max_length=30 )

    def __str__(self):
        return  self.payment_method

class Coin(models.Model):

    name = models.CharField(max_length=30,unique=True)
    currency = models.CharField(max_length=30,unique=True )
    def __str__(self):
        return  self.name




class SupplierName(models.Model):

    name = models.CharField(unique=True,max_length=30 )
    email = models.EmailField(unique=True)
    secondary_email = models.EmailField(unique=True,blank=True)
    phone_number =  models.CharField(unique=True,max_length=10 )
    fax_number =  models.CharField(unique=True ,max_length=10)

    payment_method = models.ForeignKey('identification.PaymentMethod', on_delete=models.CASCADE)
    coin = models.ForeignKey('identification.Coin', on_delete=models.CASCADE)
    limit_of_debt = models.FloatField()
    balance = models.FloatField()
    payment_terms = models.TextField()

    def __str__(self):
        return  self.name

