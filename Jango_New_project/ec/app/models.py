from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY_CHOICES=(
    ('MR', "Mahindra"),
    ('TY', "Toyota"),
    ('SZ','Suzuki'),
    ("PY", 'Porscher'),
    ('RY', "Rols Royal"),
    ("TT", "Tata"),
    ('BMW',"BMW"),
    ("WV",'Volkswagen'),
    ('MD', "Mercedes"),
    ('RG', "Range Rower"),
    ("OD", 'Audi'),
)

class product(models.Model):
    title = models.CharField(max_length=100)
    selling_price =  models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField(default='')
    prodapp =models.TextField(default="")
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=3)
    product_image = models.ImageField(upload_to="product")

    def __str__(self):
        return self.title
    
class Customer (models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    mobail=models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

   