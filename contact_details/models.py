from django.db import models
from wagtail.fields import RichTextField



class Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    email = models.EmailField()
    subject = models.TextField()
    Message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)


    def __str__(self):
        return self.subject
