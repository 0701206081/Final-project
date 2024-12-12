from django.db import models

# Create your models here.

class Hero(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='images/')
    btn_link = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField()
    link = models.CharField(max_length=100)


    def __str__(self):
        return self.title
    
class AboutFeatures(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    

class Deliveries(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Section(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    feature1 = models.TextField()
    feature2 = models.TextField()
    feature3= models.TextField()
    more = models.TextField()
    img = models.ImageField(upload_to='sections/')

    def __str__(self):
        return self.title
    

class Service(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()


    def __str__(self):
        return  self.title
    

class ServiceSection(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Business(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    location = models.CharField(max_length=255)
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class PortfolioItem(models.Model):
    CATEGORY_CHOICES = [
        ('retail', 'Retail'),
        ('beauty', 'Beauty'),
        ('food', 'Food and Bevarage'),
        ('restuarant', 'Restuarant'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title







