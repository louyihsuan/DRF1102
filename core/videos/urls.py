from django.conf.urls import url

from videos import views

urlpatterns = [

    #url(r'^$', views.dashboard, name='dashboard'),
    url(r'^sendmail/', views.send_mail_to_all, name='sendmail'),
    #url(r'^task_not_use_celery/', views.task_not_use_celery, name='task_not_use_celery'),

]