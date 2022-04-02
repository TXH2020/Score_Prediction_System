from django.db import models
class Accept(models.Model):
    data=models.CharField(max_length=2,default=0)
    def __str__(self):
        return self.data
