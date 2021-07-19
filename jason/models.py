from django.db import models
from django.urls import reverse
# Create your models here.

class 인편_jason(models.Model) :
    작성자 = models.CharField(max_length=7)
    제목 = models.CharField(max_length=50)
    내용 = models.TextField()
    작성일 = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.작성자