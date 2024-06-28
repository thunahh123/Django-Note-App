from django.db import models
from django.utils import timezone

# Create your models here.

class Entry(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
 
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Entries"
        ordering = ('-created_at',)
