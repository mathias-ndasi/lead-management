from django.test import TestCase

# Create your tests here.
from django.urls import reverse


class HomePageTest(TestCase):

    def test_get(self):
        response = self.client.get(reverse("landing_page"))
        self.assertEqual(first=response.status_code, second=200)
        self.assertTemplateUsed(response=response, template_name="landing.html")
