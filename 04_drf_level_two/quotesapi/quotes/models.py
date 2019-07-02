from django.db import models
from django.contrib.auth.models import User


class Quote(models.Model):
    quote_author = models.ForeignKey(User, on_delete=models.CASCADE)
    quote_body = models.TextField()
    context = models.CharField(max_length=60)
    source = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quote_author} - {self.created_at}'
    