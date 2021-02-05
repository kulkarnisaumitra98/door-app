from django.db import models

# Create your models here.


class DeviceModel(models.Model):
    mac_address = models.CharField(
        default="",
        max_length=100,
        primary_key=True
    )
    is_active = models.BooleanField(default=False)

    objects = models.Manager()  # The default manager.

    def __str__(self):
        return f'{self.mac_address}'
