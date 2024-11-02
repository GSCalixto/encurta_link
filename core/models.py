from django.db import models

# Create your models here.
class Links(models.Model):
    link_original = models.URLField()
    link_encurtado = models.CharField(max_length= 10, unique= True)

    def __str__(self) -> str:
        return self.link_encurtado