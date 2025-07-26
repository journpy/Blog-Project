from django.db import models

from django.contrib.auth.models import User as UserModel


class Blog(models.Model):
    title = models.CharField()
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date_created']




