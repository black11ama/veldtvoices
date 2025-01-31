import uuid

from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.
class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='covers/', blank=True)
    description = models.TextField(max_length=1000, blank=True)  # Added description with a suitable limit
    isbn = models.CharField(max_length=13, blank=True)  # Added ISBN, can be blank
    publisher = models.CharField(max_length=200, blank=True)  # Added publisher, can be blank
    number_of_pages = models.PositiveIntegerField(blank=True, null=True)  # Added number of page
    language = models.CharField(max_length=50, blank=True)
    publication_date = models.DateTimeField(blank=True, null=True)
    edition = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = [
            ('special_status', 'Can read all books')
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])

class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.review