from django.db import models

class DailyTotalSummary(models.Model):
    city = models.CharField(max_length=50)
    net_sale = models.IntegerField()
    net_expense = models.IntegerField()
    daily_target = models.IntegerField()
    date = models.DateField()

