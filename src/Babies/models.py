from django.db import models

class Baby(models.Model):
    name = models.CharField(max_length=20,null=True)
    lastName = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=20, null=True)
 
    parent = models.ForeignKey(
        'Parents.Parent',
        on_delete = models.CASCADE,
        null = True,
        blank = False
    )
    


