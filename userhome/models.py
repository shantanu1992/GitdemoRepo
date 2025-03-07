from django.db import models
from django.contrib.auth.models import User  


class Registration_model(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='pics', blank=True, null=True)

    def __str__(self):
        return self.user.first_name