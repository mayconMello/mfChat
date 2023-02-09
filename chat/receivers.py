from django.db.models import signals
from django.dispatch import receiver

from chat.models import Group


@receiver(signals.post_save, sender=Group)
def callback_add_owner_with_member(
    sender,
    instance: Group,
    created,
    **kwargs
):
    if not created:
        return

    instance.members.create(
        user=instance.owner,
        is_admin=True
    )
