from django.db import models
import hashlib


# Create your models here.
from django.db import models

class Block(models.Model):
    previous_hash = models.CharField(max_length=64, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    data = models.TextField()

    def __str__(self):
        return self.data

    def save(self, *args, **kwargs):
        if not self.pk:
            # If this is the first block, set the previous hash to 0
            self.previous_hash = '0'
        super().save(*args, **kwargs)

    @property
    def hash(self):
        # Calculate the hash for the current block
        hash_object = hashlib.sha256(str(self).encode())
        return hash_object.hexdigest()


class Transaction(models.Model):
    sender = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)
    amount = models.FloatField()

    def __str__(self):
        return f"{self.sender} -> {self.recipient}: {self.amount}"
