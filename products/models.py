from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title= models.CharField(max_length=200)
    pub_date=models.DateTimeField()
    body = models.TextField()
    url = models.TextField()
    image=models.ImageField(upload_to='images/')
    icon=models.ImageField(upload_to='images/')
    votes_total=models.IntegerField(default=1)#foreign key links users
    hunter=models.ForeignKey(User, on_delete=models.CASCADE)
    #with on_delete if user is delted, all products related to him will be deleted
    def __str__(self): #for naming objects after title
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

  