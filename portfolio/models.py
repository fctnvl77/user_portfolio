from django.db import models




class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True)
    description = models.CharField(max_length=250)