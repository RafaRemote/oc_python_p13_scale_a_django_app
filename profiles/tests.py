import pytest
from django.test import Client, TestCase
from django.urls import reverse
from .models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
class TestProfils(TestCase):
    client = Client()

    def test_profiles_index(self):
        path = reverse("profiles:index")
        res = self.client.get(path)
        res_content = res.content.decode().split()
        title_index = res_content.index("<title>") + 1
        title_expected = "Profiles"
        self.assertEqual(res_content[title_index], title_expected)
        self.assertEqual(res.status_code, 200)

    def test_profile_page(self):
        user = User.objects.create(
            username="username",
            first_name="first_name",
            last_name="last_name",
            email='email@email.com'
        )
        profile = Profile.objects.create(
            user=user,
            favorite_city="favorite_city"
        )
        path = reverse("profiles:profile", kwargs={"username": user.username})
        res = self.client.get(path)
        res_content = res.content.decode().split()
        title_page = res_content.index("<title>") + 1
        title_expected = profile.user.username
        self.assertEqual(res_content[title_page], title_expected)
        self.assertEqual(res.status_code, 200)
