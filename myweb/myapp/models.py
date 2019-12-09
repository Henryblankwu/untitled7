from django.db import models

# Create your models here.

''' def stu table of modele class '''
class cloud_ready(models.Model):
    '''自定义cloud_ready表对应的Model类'''
    #定义属性：默认主键自增id字段可不写
    Qid = models.AutoField(primary_key=True)
    Cid = models.CharField(max_length=16)
    Bid = models.CharField(max_length=16)
    PSP = models.CharField(max_length=16)
    Uid = models.CharField(max_length=16)
    Qtime = models.CharField(max_length=16)
    SLT = models.CharField(max_length=16)
    QUE = models.CharField(max_length=16)
    BG = models.CharField(max_length=16)
    C3 = models.CharField(max_length=16)
    C2 = models.CharField(max_length=16)
    C1 = models.CharField(max_length=16)

    # 定义默认输出格式
    def __str__(self):
        return "%d:%d:%d:%s:%s:%s:%s:%s:%s:%s:%s"%(self.Qid,self.Cid,self.Bid,self.PSP,self.Uid,self.Qtime,self.SLT,self.QUE,self.BG,self.C3,self.C2,self.C1)

    # 自定义对应的表名，默认表名：cloud_ready
    class Meta:
        db_table="cloud_ready"