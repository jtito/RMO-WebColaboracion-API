from django.db import models

# Create your models here.
class Scenario(models.Model):

    id = models.IntegerField(primary_key=True) 
    description = models.CharField(max_length=100)  

    def __str__(self):
        return self.description

    class Meta: 
        db_table = "scenarios"