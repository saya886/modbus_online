from django.db import models

# Create your models here.
class data_history(models.Model):
    id = models.BigAutoField(primary_key=True)
    value = models.CharField('value',max_length=50, default='')
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

class sensor_data(models.Model):
    id = models.BigAutoField(primary_key=True)
    data = models.CharField('value',max_length=50, default=',,,,,')
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id