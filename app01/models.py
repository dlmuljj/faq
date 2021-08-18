from django.db import models

# Create your models here.
class DDR(models.Model):
    question =  models.TextField(verbose_name='问题')
    answers = models.TextField('回复')
    replier = models.CharField(verbose_name='回复人',max_length=32,null=True)
    creator = models.CharField(verbose_name='创建人',max_length=32,null=True)
    create_time = models.DateField(verbose_name='创建时间',auto_now=False,null=True)

    class Meta:
        verbose_name_plural = 'DDR'
    def __str__(self):
        return 'DDR'


class Serdes(models.Model):
    question =  models.TextField(verbose_name='问题')
    answers = models.TextField(verbose_name='回复',null=True)
    replier = models.CharField(verbose_name='回复人',max_length=32,null=True)
    creator = models.CharField(verbose_name='创建人',max_length=32,null=True)
    create_time = models.DateField(verbose_name='创建时间',auto_now=False,null=True)

    class Meta:
        verbose_name_plural = 'Serdes'

class U2(models.Model):
    question =  models.TextField(verbose_name='问题')
    answers = models.TextField(verbose_name='回复',null=True)
    replier = models.CharField(verbose_name='回复人',max_length=32,null=True)
    creator = models.CharField(verbose_name='创建人',max_length=32,null=True)
    create_time = models.DateField(verbose_name='创建时间',auto_now=False,null=True)
    class Meta:
        verbose_name_plural = 'U2'

class U3(models.Model):
    question =  models.TextField(verbose_name='问题')
    answers = models.TextField(verbose_name='回复',null=True)
    replier = models.CharField(verbose_name='回复人',max_length=32,null=True)
    creator = models.CharField(verbose_name='创建人',max_length=32,null=True)
    create_time = models.DateField(verbose_name='创建时间',auto_now=False,null=True)
    class Meta:
        verbose_name_plural = 'U3'

class Pll(models.Model):
    question =  models.TextField(verbose_name='问题')
    answers = models.TextField(verbose_name='回复',null=True)
    replier = models.CharField(verbose_name='回复人',max_length=32,null=True)
    creator = models.CharField(verbose_name='创建人',max_length=32,null=True)
    create_time = models.DateField(verbose_name='创建时间',auto_now=False,null=True)
    class Meta:
        verbose_name_plural = 'PLL'


class Hdmi(models.Model):
    question =  models.TextField(verbose_name='问题')
    answers = models.TextField(verbose_name='回复',null=True)
    replier = models.CharField(verbose_name='回复人',max_length=32,null=True)
    creator = models.CharField(verbose_name='创建人',max_length=32,null=True)
    create_time = models.DateField(verbose_name='创建时间',auto_now=False,null=True)
    class Meta:
        verbose_name_plural = 'HDMI'

class Dp(models.Model):
    question =  models.TextField(verbose_name='问题')
    answers = models.TextField(verbose_name='回复',null=True)
    replier = models.CharField(verbose_name='回复人',max_length=32,null=True)
    creator = models.CharField(verbose_name='创建人',max_length=32,null=True)
    create_time = models.DateField(verbose_name='创建时间',auto_now=False,null=True)
    class Meta:
        verbose_name_plural = 'DP'

class TVSensor(models.Model):
    question =  models.TextField(verbose_name='问题')
    answers = models.TextField(verbose_name='回复',null=True)
    replier = models.CharField(verbose_name='回复人',max_length=32,null=True)
    creator = models.CharField(verbose_name='创建人',max_length=32,null=True)
    create_time = models.DateField(verbose_name='创建时间',auto_now=False,null=True)
    class Meta:
        verbose_name_plural = 'TVSensor'

class MIPI(models.Model):
    question =  models.TextField(verbose_name='问题')
    answers = models.TextField(verbose_name='回复',null=True)
    replier = models.CharField(verbose_name='回复人',max_length=32,null=True)
    creator = models.CharField(verbose_name='创建人',max_length=32,null=True)
    create_time = models.DateField(verbose_name='创建时间',auto_now=False,null=True)
    class Meta:
        verbose_name_plural = 'MIPI'

class SARADC(models.Model):
    question =  models.TextField(verbose_name='问题')
    answers = models.TextField(verbose_name='回复',null=True)
    replier = models.CharField(verbose_name='回复人',max_length=32,null=True)
    creator = models.CharField(verbose_name='创建人',max_length=32,null=True)
    create_time = models.DateField(verbose_name='创建时间',auto_now=False,null=True)
    class Meta:
        verbose_name_plural = 'SARADC'

class VDAC(models.Model):
    question =  models.TextField(verbose_name='问题')
    answers = models.TextField(verbose_name='回复',null=True)
    replier = models.CharField(verbose_name='回复人',max_length=32,null=True)
    creator = models.CharField(verbose_name='创建人',max_length=32,null=True)
    create_time = models.DateField(verbose_name='创建时间',auto_now=False,null=True)
    class Meta:
        verbose_name_plural = 'VDAC'


class Package(models.Model):
    question =  models.TextField(verbose_name='问题')
    answers = models.TextField(verbose_name='回复',null=True)
    replier = models.CharField(verbose_name='回复人',max_length=32,null=True)
    creator = models.CharField(verbose_name='创建人',max_length=32,null=True)
    create_time = models.DateField(verbose_name='创建时间',auto_now=False,null=True)
    class Meta:
        verbose_name_plural = 'Package'

