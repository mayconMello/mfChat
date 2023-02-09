from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class GroupMember(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='members'
    )
    is_admin = models.BooleanField(
        default=False
    )
    date_joined = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.user}/{self.group}'


class Chat(models.Model):
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sender'
    )
    destination = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='destination'
    )
    group = models.ForeignKey(
        Group,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    text = models.TextField()
    send_in = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        if self.group:
            return f'{self.sender} to {self.group}'

        return f'{self.sender} to {self.destination}'
