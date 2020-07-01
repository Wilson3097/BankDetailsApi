from django.db import models

# Create your models here.


class BankDetails(models.Model):
    Id = models.AutoField(primary_key=True)
    ifsc = models.CharField(max_length=20)
    bank_id = models.IntegerField()
    branch = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    bank_name = models.CharField(max_length=200)

    def __str__(self):
        return self.bank_name
