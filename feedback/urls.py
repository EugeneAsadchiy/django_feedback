from django.contrib import admin
from django.urls import path


from feedback import views

urlpatterns = [
    path('done', views.DoneView.as_view()),
    path('', views.FeedBackView.as_view()),
    path('<int:id_feedback>', views.FeedBackUpdateView.as_view()),
    # path('hello', views.hello),
]