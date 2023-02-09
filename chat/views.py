# Create your views here.
from rest_framework import viewsets

from chat.serializers import *


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

    def perform_create(self, serializer):
        serializer.save(
            owner=self.request.user
        )
