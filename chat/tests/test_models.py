from django.contrib.auth import get_user_model
from django.core.validators import ValidationError
from django.test import TestCase

from chat.models import Group

User = get_user_model()


class GroupModelTest(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            email='jhon@doe.com',
            password='foo'
        )

    def test_create_group(self):
        group = Group.objects.create(
            owner=self.user,
            name='Group Name'
        )

        self.assertEqual(group.__str__(), 'Group Name')
        self.assertTrue(Group.objects.exists())

    def test_create_group_without_name(self):
        group = Group(name='', owner=self.user)
        with self.assertRaises(ValidationError):
            group.full_clean()
            group.save()

        self.assertFalse(Group.objects.exists())

    def test_create_group_without_owner(self):
        group = Group(name='Group Name')
        with self.assertRaises(ValidationError):
            group.full_clean()
            group.save()

        self.assertFalse(Group.objects.exists())
