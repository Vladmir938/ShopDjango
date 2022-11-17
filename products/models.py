from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    discount = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="static/images/")

    def get_sale(self):
        price = int(self.price - self.price * (self.discount / 100))
        return price

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'