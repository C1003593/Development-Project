from django.urls import path
from . import views

app_name = 'messaging'

urlpatterns = [
    path('send_message/<str:recipient_username>/', views.send_message, name='send_message'),
    path('inbox/', views.inbox, name='inbox'),
    path('reply_message/<int:message_id>/', views.reply_message, name='reply_message'),
]