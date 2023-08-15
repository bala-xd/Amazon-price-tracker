from django.db import models
from .utils import get_data
# Create your models here.


class Link(models.Model):
    name = models.CharField(max_length=220, blank=True)
    url = models.CharField(max_length=220, blank=True)
    cur = models.FloatField(blank=True)
    old = models.FloatField(default=0)
    diff = models.FloatField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('diff', '-created')

    def save(self, *args, **kwargs):
        name, price = get_data(self.url)
        old = self.cur
        if self.cur:
            if price != old:
                d = price - old
                self.diff = round(d, 2)
                self.old = old
        else:
            self.old = 0
            self.diff = 0
        self.name = name
        self.cur = price
        super().save(*args, **kwargs)
