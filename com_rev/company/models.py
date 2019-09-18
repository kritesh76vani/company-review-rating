from django.db import models

class Company(models.Model):
    name       = models.CharField(max_length=100,null = True, blank = True)
    email      = models.EmailField()
    address    = models.CharField(max_length=100,null = True, blank = True)
    
    is_active  = models.BooleanField(default=True)
    
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


    def __str__(self):
        return "{0}".format(self.name)
