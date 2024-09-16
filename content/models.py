from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserGroup(models.Model):
    name = models.CharField(max_length=100)  
    leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='led_groups')
    members = models.ManyToManyField(User, related_name='user_groups')
    def __str__(self):
        return self.name

class ForRent(models.Model):
    mobile = models.IntegerField()
    myhomelink = models.URLField()
    myhomeid = models.IntegerField()
    sslink = models.URLField()
    ssid = models.IntegerField()
    area = models.IntegerField()
    price = models.IntegerField()
    address = models.TextField()
    limitations = models.TextField()
    agent = models.TextField()
    group = models.ForeignKey(UserGroup, on_delete=models.CASCADE, related_name='rent_ads', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rent_posts')
    def save(self, *args, **kwargs):
        if not self.group:
            self.group = self.author.user_groups.first()
        super().save(*args, **kwargs)

class ForSale(models.Model):
    mobile = models.IntegerField()
    myhomelink = models.URLField()
    myhomeid = models.IntegerField()
    sslink = models.URLField()
    ssid = models.IntegerField()
    area = models.IntegerField()
    price = models.IntegerField()
    percentage = models.IntegerField()
    address = models.TextField()
    agent = models.TextField()
    group = models.ForeignKey(UserGroup, on_delete=models.CASCADE, related_name='sale_ads', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sale_posts')
    def save(self, *args, **kwargs):
        if not self.group:
            self.group = self.author.user_groups.first()
        super().save(*args, **kwargs)