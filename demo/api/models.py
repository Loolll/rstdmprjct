from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class rock(models.Model):
    vid = models.CharField(verbose_name='vid', db_index=True, max_length=64)
    color = models.CharField(verbose_name='Color', max_length=64)
    rcktp = models.CharField(verbose_name='Type', max_length=64, default='Unknown')
    size_types = (
            (1, 'big'),(2, 'small'),(3,'middle'),(4, 'unique')
    )
    size = models.IntegerField(verbose_name='Size', max_length=64, choices=size_types)
    user = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE)
