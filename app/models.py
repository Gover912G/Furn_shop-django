from django.db import models

# Create your models here.


class SiteDescription(models.Model):
    fname = models.CharField(max_length=50, blank=False)
    sname = models.CharField(max_length=50, blank=False)
    description = models.TextField(default='')
    image = models.ImageField(upload_to='images', default='profile.png')

    def __int__(self):
        return self.fname

class Products(models.Model):
    name = models.CharField(max_length=50, blank=False)
    price= models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(default='description')
    image = models.ImageField(upload_to='images', default='profile.png', blank=False)

    def __str__(self):
        return self.name

# class Sofa(models.Model):

class Testimony(models.Model):
    name = models.CharField(max_length=50, blank=False)
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(default='description')
    image = models.ImageField(upload_to='images',default='profile.png', blank=False)

    def __str__(self):
        return self.name

class ShopItem(models.Model):
    name = models.CharField(max_length=50, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='shopItems', default='shopitem.png')

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=50, blank=False)
    # lname = models.CharField(max_length=50, blank=False)
    role = models.CharField(max_length=50, blank=False)
    description = models.TextField(default='')
    image = models.ImageField(upload_to="team", default='profile.png')

    def __int__(self):
        return self.name

class Blog(models.Model):
    name = models.CharField(max_length=50, blank=False)
    title = models.CharField(max_length=100, blank=False)
    date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blogs', default='blogs.png')

    def __int__(self):
        return self.name

class Contact(models.Model):
    fname = models.CharField(max_length=50,blank=False)
    lname = models.CharField(max_length=50,blank=False)
    email = models.EmailField(max_length=100, blank=False)
    message = models.TextField(default='')

    def __int__(self):
        return self.email