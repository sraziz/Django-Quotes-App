from django.db import models

class Quotes(models.Model):
    topic = models.CharField(max_length=255,blank=False)
    quotation = models.CharField(max_length=500)
    by = models.CharField(max_length=100, default="")

    class Meta:
      verbose_name_plural = "quotes"

    def __str__(self):
        return self.topic