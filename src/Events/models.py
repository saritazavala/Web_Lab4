from django.db import models

class Event(models.Model):
    description = models.CharField(max_length=35, null=True)
    type = models.CharField(max_length=25, null = True)
    date = models.DateTimeField(auto_now_add=True)
    
    baby = models.ForeignKey(
        'Babies.Baby',
        on_delete = models.CASCADE,
        null = True,
        blank = False
    )

    
