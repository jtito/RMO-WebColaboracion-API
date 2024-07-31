from django.db import models

class Permission(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description
    class Meta:
        db_table = "permission"
