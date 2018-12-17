import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField('问题内容', max_length=200)
    pub_date = models.DateTimeField('发布时间')


    def __str__(self):      # 给人类看的 (了解)控制打印对象时的输出信息
        return self.question_text

    def was_published_recently(self):
        # return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)
        if timezone.now() - datetime.timedelta(days=1) <= self.pub_date:
            return True
        else:
            return False

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # CASCADE 这个类只用传一个类名，不需要实例化
    choice_text = models.CharField('选项内容', max_length=200)
    votes = models.IntegerField('投票数', default=0)


    # def __repr__(self):   # 给机器看的
    #     pass
    def __str__(self):  # 给人类看的，
        return self.choice_text


"""
类被翻译成sql执行
CREATE TABLE QUESTION IF NOT EXISTS(
    id INT PRIMARY KEY INCREASE,
    question_text CHAR(200) comment "发布时间",
    pub_data DATETIME comment "发布时间"
)
create table votes if not exists(
    id int primary key increase,
    choice_text char(200) comment "选项内容",
    votes int default 0 comment "投票数",
    question int,
    foriegn key question reference question.id on cascade,
)
"""

# django自带ORM框架，用法类似sqlalchemy
# 自定义的类要继承ORM框架中的Model类，这样ORM框架能把类和数据库联系起来。