from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.
class Bookmark(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200, default="", editable=True)

    bookmark_type = models.CharField(max_length=6, choices=[('u', 'url'), ('f', 'folder')], default='u')


class PersonalBookmark(Bookmark):
    user = models.ForeignKey(User, on_delete=models.CASCADE)