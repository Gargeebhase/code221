from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^ask$',views.ask_q, name='ask_q'),
    url(r'^ans/',views.ans_p, name='ans_p'),
    url(r'^ans_list$',views.ans_list, name='ans_list'),
]
