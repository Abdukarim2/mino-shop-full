from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings
BASE_URL = settings.BASE_URL


class Category(models.Model):
    name = models.CharField("Kategoruya nomi", max_length=100)
    slug = models.SlugField("*", max_length=100)
    img = models.ImageField("Katego'riya rasmi", upload_to="category images/")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_img_url(self):
        return f"{BASE_URL}{self.img.url}"

    class Meta:
        ordering = ['-id']
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Color(models.Model):
    name = models.CharField("Rang ko'di yoki nomi", max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']


class Size(models.Model):
    name = models.CharField("Hajm nomi", max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']


class Material(models.Model):
    name = models.CharField("Material nomi", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product_category")
    name = models.CharField("Tovar nomi", max_length=150)
    slug = models.SlugField("*", max_length=150)
    price = models.IntegerField("Narxi UZS")
    priceDolor = models.FloatField("Narxi USD", blank=True)
    about = RichTextField()
    imgFont = models.ImageField("Tovar rasmi oldi tomoni", upload_to="product images")
    imgSide = models.ImageField("Tovar rasmi yon tomoni hohishiy", upload_to="product images", blank=True)
    imgBack = models.ImageField("Tovar rasmi orqa tomoni hohishiy", upload_to="product images", blank=True)
    size = models.ManyToManyField(Size, blank=True)
    color = models.ManyToManyField(Color, blank=True)
    material = models.ManyToManyField(Material,  blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_colors(self):
        colors = []
        for i in self.color.all():
            colors.append(i.name)
        return colors

    def get_sizes(self):
        sizes = []
        for i in self.size.all():
            sizes.append(i.name)
        return sizes

    def get_img_url(self):
        images = [f"{BASE_URL}{self.imgFont.url}"]
        if self.imgSide:
            images.append(f"{BASE_URL}{self.imgSide.url}")
        if self.imgBack:
            images.append(f"{BASE_URL}{self.imgBack.url}")
        return images

    class Meta:
        ordering = ['-id']
