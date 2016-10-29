from django.core.validators import URLValidator
from django.db import models


class Seller(models.Model):
    company_name = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.company_name)


class Url_in_Seller(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    url = models.CharField(max_length=1000, validators=[
                           URLValidator()], default="url")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.seller, self.url)


class Category(models.Model):
    category_name = models.CharField(max_length=200, null=True, blank=True)
    parent_category = models.ForeignKey('self', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.parent_category is None:
            return '%s' % (self.category_name)
        else:
            return '%s %s' % (self.parent_category, self.category_name)


class Cutter(models.Model):
    url_in_seller = models.ForeignKey(Url_in_Seller, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    text = models.TextField(null=True)
    image = models.ImageField(upload_to="cutter", null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    pass


class Recipe(models.Model):
    pass
