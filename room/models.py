import uuid
from django.db import models
from user.models import User

class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Entry(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    is_children = models.BooleanField(default=False)
    is_valid = models.BooleanField(default=True)
    parent = models.ForeignKey('self', related_name="children", null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, related_name="entries", on_delete=models.PROTECT, null=True)
    room = models.ForeignKey(Room, related_name="entries", on_delete=models.PROTECT)
    votes = models.IntegerField(null=True, default=0)
    

