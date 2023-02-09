from django.urls import path

from chat.views import GroupViewSet

urlpatterns = [
    path('chat/groups', GroupViewSet.as_view({
        'post': 'create',
        'get': 'list'
    })),
]
