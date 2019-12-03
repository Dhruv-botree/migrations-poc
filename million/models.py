from django.db import models

# Create your models here.
class Million(models.Model):
    dump = models.TextField(null=True)
    # dump_v2 = models.TextField()