from django.db import models

# Create your models here.
class Stock_List(models.Model):
    symbol = models.CharField(max_length=30,default ="")
    is_active = models.BooleanField(default =True)

    def __str__(self) -> str:
        return self.symbol