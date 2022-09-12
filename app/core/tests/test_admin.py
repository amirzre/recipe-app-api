"""
Tests for the Django admin modification.
"""
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    """Test for Django admin."""

    def setUp(self):
        """Create user and client."""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@email.com',
            password='testpass',
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@email.com',
            password='testpass',
            name='test name',
        )

    def test_user_list(self):
        """Test that user are listed on page."""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        """Test the edit user page works."""
        url = reverse(
            'admin:core_admin_change',
            args=[self.user.id],
        )
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
