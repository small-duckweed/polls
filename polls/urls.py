# 子路由。自己新建的，在大型项目中用的到
from django.urls import path

# from .views import index   第一种引入文件的方法
from . import views     #  第二种引入方法，   .为同级  ..为父级

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
]

# 先引入视图函数
# path()函数定义的路由最终都会在项目启动时加载
# path(路由规则)

