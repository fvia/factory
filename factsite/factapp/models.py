from django.db import models


class Process(models.Model):
    """  
    """
    class Meta:
        verbose_name_plural = "processes"

    code = models.CharField(max_length=2,primary_key=True)
    name = models.CharField(max_length=50)


class Machine(models.Model):
    """
    """
    code = models.CharField(max_length=20,primary_key=True)
    name = models.CharField(max_length=50)
    process = models.ForeignKey(Process)    

    
class Article(models.Model):
    """
    """
    code = models.CharField(max_length=20,primary_key=True)
    name = models.CharField(max_length=50)
    process = models.ForeignKey(Process)  # The process that build the article  
    

class Component(models.Model):
    """ For Buildin an Article are needed their components
    """
    article = models.ForeignKey(Article) 
    part = models.ForeignKey(Article,related_name='part')
    quantity = models.FloatField() # Kg/Km
