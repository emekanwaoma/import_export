from datetime import datetime
from operator import mod
from django.db import models

class Author(models.Model):
    GENDER_OPTIONS = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=7, choices=GENDER_OPTIONS)

    def __str__(self):
        return f'{self.name}'


class Book(models.Model):
    PUBLISH_OPTIONS = (
        ('Published', 'published'),
        ('Unpublished', 'unpublished'),
        ('Unknown', 'unknown')
    )

    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='author_set'
    )
    publish_status = models.CharField(max_length=12, choices=PUBLISH_OPTIONS)
    created = models.DateTimeField(default=datetime.now)
    updated = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f'{self.title}'
    
    def save(self, *args, **kwargs):
        self.updated = datetime.now()
        super(Book, self).save(*args, **kwargs)