import datetime
from django.db import models
from django.utils import timezone

class Channel(models.Model):
	sensor_name = models.CharField(max_length=200)
	channel_root = models.CharField(max_length=200)
	channel_next_root = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.sensor_name