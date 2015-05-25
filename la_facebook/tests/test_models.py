from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
from django.test import TestCase
from la_facebook.models import UserAssociation

class UserAssociationTests(TestCase):
    def setUp(self):
        self.user1 = get_user_model().objects.create(username='tester1', password="test")
        self.user1.save()
        self.user2 = get_user_model().objects.create(username='tester2', password="test")
        self.user2.save()

    def test_expired(self):
        ua_active = UserAssociation.objects.create(
            user=self.user1,
            identifier='12345',
            token='12345',
            expires=datetime.now() + timedelta(1)
        )
        ua_active.save()
        self.assertTrue(ua_active.expired())

        ua_expired = UserAssociation.objects.create(
            user=self.user2,
            identifier='54321',
            token='54321',
            expires=datetime.now() - timedelta(1)
        )
        ua_expired.save()
        self.assertFalse(ua_expired.expired())
