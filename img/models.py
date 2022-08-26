from django.db import models


class ProfilePic(models.Model):
    objecs = models.Manager()
    profileusername = models.CharField(max_length=1000)
    imagelink = models.CharField(max_length=1000)
    username = models.CharField(max_length=1000)

    def __str__(self):
        return self.profileusername