import pytest
from django.contrib.auth.models import User
from django.test import TestCase
from profiles.models import Profile
from django.urls import reverse


@pytest.mark.django_db
class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", first_name="Jean", last_name="Dupont"
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city="Paris"
        )

    def test_str_method(self):
        """__str__() doit retourner le username"""
        self.assertEqual(str(self.profile), "testuser")

    def test_favorite_city_field(self):
        """Le champ favorite_city doit être bien enregistré"""
        self.assertEqual(self.profile.favorite_city, "Paris")


@pytest.mark.django_db
class ProfileViewsTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="alice")
        self.user2 = User.objects.create_user(username="bob")
        self.profile1 = Profile.objects.create(user=self.user1, favorite_city="Rennes")
        self.profile2 = Profile.objects.create(user=self.user2, favorite_city="Lyon")

    def test_index_view_status_code(self):
        """La vue index doit répondre avec un statut 200"""
        url = reverse("profiles:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_index_view_context_contains_profiles_list(self):
        """La vue index doit contenir profiles_list dans le contexte"""
        url = reverse("profiles:index")
        response = self.client.get(url)
        self.assertIn("profiles_list", response.context)
        profiles_list = response.context["profiles_list"]
        self.assertIn(self.profile1, profiles_list)
        self.assertIn(self.profile2, profiles_list)

    def test_profile_view_status_code(self):
        """La vue profile doit répondre avec un statut 200"""
        url = reverse("profiles:profile", kwargs={"username": "alice"})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_profile_view_context_contains_profile(self):
        """La vue profile doit contenir profile dans le contexte"""
        url = reverse("profiles:profile", kwargs={"username": "bob"})
        response = self.client.get(url)
        self.assertIn("profile", response.context)
        self.assertEqual(response.context["profile"], self.profile2)
