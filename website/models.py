from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class NewMessage(models.Model):
    name = models.TextField(max_length=500)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=20000)

    def __str__(self):
        return f"{self.name} with {self.email} sent {self.message}"
    


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} wrote {self.title} on {self.pub_date}"
