from django.db import models


class AccountsModel(models.Model):
    name_acc = models.CharField(max_length=100)
    cash = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name_acc
