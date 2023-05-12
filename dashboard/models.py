from django.db import models

# Create your models here.
class IndustrialData(models.Model):
    end_year=models.CharField(max_length=50)
    intensity=models.CharField(max_length=100)
    sector=models.CharField(max_length=20)
    topic=models.CharField(max_length=20)
    insight=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    region=models.CharField(max_length=20)
    start_year=models.CharField(max_length=100)
    impact=models.CharField(max_length=100)
    added=models.CharField(max_length=100)
    published=models.CharField(max_length=100)
    country=models.CharField(max_length=50)
    relevance=models.CharField(max_length=100)
    pestle=models.CharField(max_length=100)
    source=models.CharField(max_length=200)
    title=models.CharField(max_length=500)
    likelihood=models.CharField(max_length=100)
