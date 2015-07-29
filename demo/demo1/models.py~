from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class History(models.Model):
	user=models.ForeignKey(User,null=True)
	name=models.CharField(max_length=20,null=True)
	hist_date=models.DateTimeField('date published',null=True)
