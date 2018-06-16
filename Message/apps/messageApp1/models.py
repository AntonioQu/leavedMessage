from django.db import models

# Create your models here.
class UserMessage(models.Model):
    name = models.CharField(max_length = 20, verbose_name = 'username')
    email = models.EmailField(verbose_name = "mail" )
    address = models.CharField(max_length = 100, verbose_name = "address")
    message = models.CharField(max_length = 500, verbose_name = "message")
    object_id = models.CharField(max_length = 10, primary_key = True, verbose_name = "ID")

    class Meta:
        verbose_name = "user leave message"