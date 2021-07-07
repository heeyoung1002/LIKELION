from django.db import models

# Create your models here.

#게시물을 저장할 클라스 (게시물과 관련된 데이터이다)
#장고의 Model클래스를 상속받는 post라는 클래스
class Post(models.Model):

    #데이터베이스 테이블의 column이 된다 (열)
    author = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField()

    def __str__(self):
        return f'{self.author}: {self.body}'