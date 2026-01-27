from django.db import models


class Transactions(models.Model):
    where = models.CharField(max_length=100)
    time = models.DateTimeField()
    how_much = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    acc = models.CharField(max_length=100)

    def __str__(self):
        return str(self.how_much)
