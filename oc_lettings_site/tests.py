import pytest
from django.test import Client, TestCase
from django.urls import reverse


@pytest.mark.django_db
class TestOcLettingsSite(TestCase):
    client = Client()

    def test_oc_lettings_site_index(self):
        path = reverse("index")
        res = self.client.get(path)
        res_content = res.content.decode().split()
        title_index = res_content.index("<h1>") + 1
        title_expected = "Welcome"
        self.assertIn(res_content[title_index].lower(), title_expected.lower())
        self.assertEqual(res.status_code, 200)
