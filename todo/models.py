from django.db import models
import datetime

# Create your models here.


STATUS_CHOICES = ( 
    (-1, 'Cancelled'),
    (0, 'To Do'), 
    (1, 'Done'),
)

class Item(models.Model): 
    description = models.CharField(max_length=250)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    created_date = models.DateTimeField(default=datetime.datetime.now)
    owner = models.CharField(max_length=250)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['-status', 'description']

    class Admin:
        pass