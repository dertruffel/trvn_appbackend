from django.db import models

# Create your models here.


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='cars', default=None, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='cars')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    for_sale = models.BooleanField(default=False)
    views = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.price}"

    class Meta:
        ordering = ['-created_at']

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='posts', default=None, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['-created_at']

