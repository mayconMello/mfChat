from rest_framework import serializers

from chat.models import Group, GroupMember
from users.serializer import UserSerializer


class GroupMemberSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = GroupMember
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    members = GroupMemberSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ('name', 'owner', 'members')
        read_only_fields = ('owner',)
