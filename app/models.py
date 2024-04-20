from django.db import models


class Celebrity(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    films = models.TextField()
    capital = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Celebrity"
        verbose_name_plural = "Celebrities"
