from __future__ import unicode_literals

from django.db import models
from ..loginReg_app.models import User
# Create your models here.
class Poke(models.Model):
	giver = models.ForeignKey(User, related_name = "gave")
	receiver = models.ForeignKey(User, related_name= "got")