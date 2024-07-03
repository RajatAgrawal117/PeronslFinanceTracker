from django.db import models


class YourFinance(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField()

    def __str__(self):
        return f"{self.date} - {self.amount} - {self.details}"
