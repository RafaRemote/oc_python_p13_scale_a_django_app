# from django.test import Client, TestCase
# from django.urls import reverse


# class TestLettings(TestCase):
#     client = Client()

#     def test_lettings_index(self):
#         # path = reverse("lettings:index")
#         # res = self.client.get(path)
#         # res_content = res.content.decode().split()
#         # title_index = res_content.index("<title>") + 1
#         # title_expected = "Lettings"
#         # self.assertEqual(res_content[title_index], title_expected)
#         # self.assertEqual(res.status_code, 200)
#         print(reverse("lettings:index"))
        

from django.urls import reverse
from django.test import TestCase

from . import models


class TestLettings(TestCase):

    def test_index(self):
        uri = reverse('lettings:index')
        response = self.client.get(uri)
        assert response.status_code == 200
        assert b'<title>Lettings</title>' in response.content
