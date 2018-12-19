# 子路由。自己新建的，在大型项目中用的到
from django.urls import path
from django.conf.urls import url   # django 1.x 路由写法
# from .views import index   第一种引入文件的方法
from . import views     #  第二种引入方法，   .为同级  ..为父级


app_name = 'polls'   # 起一个名字，  命名空间

urlpatterns = [
    # 首页 http:/ip:port/polls/
    path('', views.index, name='index'),
    # 首页 问题列表 /polls/index/
    path('index/', views.index, name='index'),  # index 不加斜杠，系统也会自动给你加
    # 问题详情页 ex：/polls/1/
    path('<int:question_id>/', views.detail, name='detail'),
    # 投票结果页  /polls/1/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # 去投票，选项计数加一  /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),   # name也叫别名

    # 通用视图示例
    path('simple/', views.SimpleView.as_view(), name='simple')
]


# (注意)django 1.x路由 写法是 正则风格
# ex：/polls/
# urlpatterns = [
#     # /polls/
#     url(r'^$', views.index, name='index'),  # ^ 是开始   $ 是结束
#     # polls/index/
#     url(r'^index$', views.index),
#     # /polls/5/
#     url(r'^(<?P<question_id>)[0-9]+/$')   # <?P<question_id>是django的语法
#     # [0-9] 表示0-9     + 表示匹配任意字符
# ]


# 先引入视图函数
# path()函数定义的路由最终都会在项目启动时加载
# path(路由规则)
