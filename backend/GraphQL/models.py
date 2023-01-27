from django.db import models

class TestGraphQL(models.Model):
    field1 = models.CharField(max_length=20)
    field2 = models.CharField(max_length=30)
