from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField("Название" , max_length=100,unique=True)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена",max_digits=10,decimal_places=2)
    image = models.ImageField("Фото",upload_to="product_image/")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField("Активный", default=True)

    class Meta:
        verbose_name="Курс"
        verbose_name_plural ="Курсы"
        ordering = ["-created"]


    def __str__(self):
        return self.name