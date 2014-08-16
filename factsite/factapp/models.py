from django.db import models


class Process(models.Model):
    """  
    """
    class Meta:
        verbose_name_plural = "processes"

    code = models.CharField(max_length=2,primary_key=True)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return "({}) {}".format(self.code,self.name)


class Machine(models.Model):
    """
    """
    code = models.CharField(max_length=20,primary_key=True)
    name = models.CharField(max_length=50)
    process = models.ForeignKey(Process)    

    def __str__(self):
        return "({}) {}".format(self.code,self.name)

    
class Article(models.Model):
    """
    """
    code = models.CharField(max_length=20,primary_key=True)
    name = models.CharField(max_length=50)
    process = models.ForeignKey(Process)  # The process that build the article  
    weight = models.FloatField() # Kg/Km if raw matherial 0

    def __str__(self):
        return "({}) {}".format(self.code,self.name)
    

class Component(models.Model):
    """ For Buildin an Article are needed their components
    """
    conjunt = models.ForeignKey(Article,related_name='conjunt') 
    n = models.IntegerField()
    part = models.ForeignKey(Article,related_name='part')
    quantity = models.FloatField() # Kg/Km 
