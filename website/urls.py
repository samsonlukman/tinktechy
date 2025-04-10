from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('message/', views.message, name="message"),
    path('python_course', views.python_course, name="python_course"),
    path('full_stack_course', views.full_stack_course, name="full_stack_course"),
    path("pay/<str:tx_ref>", views.pay, name="py_pay"),
    path("cs50p", views.cs50p, name="cs50p"),
    path("article/<str:title>", views.article, name="article"),
    path("articles", views.articles, name="articles")

]
