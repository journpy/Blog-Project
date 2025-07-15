from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField()
    author = models.CharField()
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




