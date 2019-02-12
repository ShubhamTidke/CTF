from django.db import models
from passlib.hash import pbkdf2_sha256

class Team(models.Model):
	team = models.CharField(max_length=100, default="")
	user_1 = models.CharField(max_length=100, default = "")
	password_1 = models.CharField(max_length=100, default = "")
	user_2 = models.CharField(max_length=100, default = "")
	password_2 = models.CharField(max_length=100, default = "")
	email = models.EmailField(default = "")
	def __str__(self):
		return self.team
"""
	def verify_password(self, pwd):
		return pbkdf2_sha256.verify(pwd, self.enc_password)"""
