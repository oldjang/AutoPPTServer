from django.db import models


class Template(models.Model):
    image_url = models.CharField(max_length=65536)
    template_url = models.CharField(max_length=65536)


class User(models.Model):
    username = models.CharField(max_length=65536)
