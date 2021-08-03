from django.db import models

# Create your models here.
class HTML(models.Model):
    html_text = models.CharField(max_length=200)

    def __str__(self):
        return self.html_text