from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Question, Choice


# Create your views here.

# def index(request):   # request 上下文对象
#     return HttpResponse("""
#         <html>
#         <head>
#         </head>
#         <body>
#         <h1>hello world</h1>
#         </body>
#         </html>
#     """)


# def index(request):
#     """
#     展示问题列表
#     """
#     question_list = Question.objects.all().order_by('-pub_date')[0:5]
#
    # question_list = result_set[0:5]   # 上面的那种写法更节省资源

    # print(question_list)  # <QuerySet [<Question: 晚饭吃什么>, <Question: 下周五考试吗>]>

    # 第一种写法
    # output = ''
    # for q in question_list:
    #     print(q.id, q.question_text, q.pub_date)  # 结果集是一个类的形式，只能用类.属性形式查找 # 不能写成字典和下标查找的方式
    #     # 2 晚饭吃什么 2018-12-14 07:53:48+00:00
    #     # 1 下周五考试吗 2018-12-13 03:21:04+00:00
    #     output = output + q.question_text + ','
    # print(output)

    # 第二种写法
    # output = ','.join([q.question_text for q in question_list])   # 列表生成器，分隔符
    # 晚饭吃什么,下周五考试吗

    # template = loader.get_template('polls/index.html')
    # context = {
    #     'question_list': question_list
    # }
    # return HttpResponse(template.render(context, request))




def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'question_list': question_list
    }
    return render(request, 'polls/index.html', context)
def detail(request, question_id):
    """
    显示一个问题的详细信息，问题内容、问题发布时间、选项内容、每一个选项投票数
    """

    # 第一种写法
    try:
        question = Question.objects.get(id=question_id)

        # 第一种（基本思想）choices = Choice.objects.filter(question_id=question_id)  # 看数据库就懂了

        # 由于orm代劳，question直接带出对应的choices
        # 第二种  choices = question.choice_set.all()   # 反向查询
        # 由于前端模版语言本质是后端代码，可以把上句话放html页面中写，有助于降低后端复杂度

    except Question.DoesNotExist:     # DoesNotExist: 不存在
        raise Http404('404，此id的问题不存在')
    print(question)
    context = {
        'question': question,

    }

    # 第二种写法
    # question = Question.objects.filter(id=question_id)
    # if not question:    # not 空  为真，  if 空为假
    #     raise Http404()

    return render(request, 'polls/detail.html/', context)

    # 第三种写法
    # question = get_object_or_404(Question, id=question_id)  #  get_object_or_404  如果没有取到数据，就会报404，返回到网页
    # print(question)
    # return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    """
    投票结果
    """
    pass


def vote(request, question_id):
    """

    """




