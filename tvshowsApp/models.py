from django.db import models
from datetime import datetime

class showManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "network should be at least 3 characters"
        if len(postData['description']) < 10 and postData['description'] != "":
            errors["description"] = "description should be at least 10 characters if not empty"
        if postData['release_date'] == "" or postData['release_date'] > str(datetime.date(datetime.now())):
            errors["release_date"] = "release date can't be empty or in the future"
        return errors

class show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = showManager()