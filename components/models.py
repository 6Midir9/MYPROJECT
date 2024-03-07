from django.db import models

class Announcement(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    price = models.CharField(max_length=255)
    contact_email = models.EmailField()

    def __str__(self):
        return self.title