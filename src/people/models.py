from django.db import models


class Contact(models.Model):
    name = models.CharField(
        max_length=50
    )
    email = models.EmailField(
        unique=True
    )
    phone = models.CharField(
        null=True,
        blank=True,
        max_length=13,
        unique=True
    )

    def __str__(self):
        return "contact {name} with email: {email}".format(
            name=self.name, email=self.email
        )
