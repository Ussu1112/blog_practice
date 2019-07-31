from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_data = models.DateTimeField('date published')
    body = models.TextField()    
    
    #title이름으로 설정
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
