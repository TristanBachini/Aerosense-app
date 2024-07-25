from django.db import models
from django.conf import settings
from django.db.models.fields import CharField




class Token(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, null=True)
    token = CharField(max_length=100, null=True)
