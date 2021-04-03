from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.


class BlogPost(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,default='')
    timestamp=models.DateTimeField(default=now)
    summary=models.CharField(max_length=1000,default='')
    content=RichTextField()
    about=models.TextField(max_length=10000,default='')
    image=models.ImageField(upload_to="images",blank=True)

    def get_absolute_url(self): # new
        return reverse('detailView', args=[str(self.id),(self.title)])
    
    def human_readable_title(self):
        return self.title.replace(' ', '-')
    
    def __str__(self) -> str:
        return self.title


class Contact(models.Model):
    name=models.CharField(max_length=50,default='Anonymous')
    email=models.EmailField(max_length=100,default='Anonymous@gmail.com')
    phone=models.BigIntegerField()
    message=models.TextField(max_length=1000,default='')

    def __str__(self) -> str:
        return f'{self.name} {self.email}'

