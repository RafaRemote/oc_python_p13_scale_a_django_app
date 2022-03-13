import pytest
from django.test import Client, TestCase
from django.urls import reverse
from .models import Address, Letting


@pytest.mark.django_db
class TestLettings(TestCase):
    client = Client()

    def test_lettings_index(self):
        path = reverse("lettings:index")
        res = self.client.get(path)
        res_content = res.content.decode().split()
        title_index = res_content.index("<title>") + 1
        title_expected = "Lettings"
        self.assertEqual(res_content[title_index], title_expected)
        self.assertEqual(res.status_code, 200)

    def test_letting_page(self):
        address = Address.objects.create(
            number="1",
            street="street",
            city="city",
            state="state",
            zip_code="000000",
            country_iso_code="XXX"
        )
        letting = Letting.objects.create(
            title="title",
            address=address
        )
        path = reverse("lettings:letting", kwargs={"letting_id": 1})
        res = self.client.get(path)
        res_content = res.content.decode().split()
        title_page = res_content.index("<title>") + 1
        title_expected = letting.title
        self.assertEqual(res_content[title_page], title_expected)
        self.assertEqual(res.status_code, 200)
