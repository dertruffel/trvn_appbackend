from django.db import models

class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    money = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        if self.username is not None:
            return self.username
        else:
            return self.email