from django.db import models
from django.contrib.auth.models import User
from company.models import Company
class Review(models.Model):
    company    = models.ForeignKey(Company, on_delete = models.CASCADE, null=True, blank=True)
    user       = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    content    = models.CharField(max_length = 500,null = True, blank = True)
    rating     = models.FloatField()
    
    is_active  = models.BooleanField(default = True)
    
    created_on = models.DateTimeField(auto_now_add = True, null = True, blank = True)
    updated_at = models.DateTimeField(auto_now = True, null = True, blank = True)


    def __str__(self):
        return "{0}----{1}".format(self.company,self.user)

