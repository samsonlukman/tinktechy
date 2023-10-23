from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('message/', views.message, name="message"),
    path('python_course', views.python_course, name="python_course"),
     path("pay/<str:tx_ref>", views.pay, name="py_pay"),
]
