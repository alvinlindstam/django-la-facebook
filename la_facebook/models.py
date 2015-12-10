import datetime
from django.conf import settings
from django.db import models

class UserAssociation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, unique=True)
    identifier = models.CharField(max_length=255, db_index=True)
    token = models.TextField()
    expires = models.DateTimeField(null=True)

    def expired(self):
        return datetime.datetime.now() < self.expires
