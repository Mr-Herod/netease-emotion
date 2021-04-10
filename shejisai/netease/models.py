from django.db import models

class Users(models.Model):
    num       = models.AutoField(primary_key=True)  
    username  = models.CharField(max_length=24)
    password  = models.CharField(max_length=24)
    class Meta:
        verbose_name = "Users"    # 表名改成中文名
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.username)


# Create your models here.
