from django.db import models

# Create your models here.

class Product(models.Model):
	title = models.CharField(max_length=30)
	description = TextField()
	target_amount = IntegerField()
	end_date = DateField()
	amount_per_time = IntegerField()
