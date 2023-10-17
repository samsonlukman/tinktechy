from django.db import models


class NewMessage(models.Model):
    name = models.TextField(max_length=500)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=20000)

    def __str__(self):
        return f"{self.name} with {self.email} sent {self.message}"
