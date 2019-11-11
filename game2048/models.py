from django.db import models

# Create your models here.
class Top_ten(models.Model):

    nickname = models.CharField(max_length=20,verbose_name='昵称',default='无名大神')
    result = models.CharField(max_length=50,verbose_name='分数',default=0)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'top_ten'