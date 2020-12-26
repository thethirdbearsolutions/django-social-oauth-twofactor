from django.db import models

class UserPermission(models.Model):
    permission = models.CharField(max_length=255)
    email = models.EmailField()

    class Meta:
        unique_together = [
            ("email", "permission"),
        ]


