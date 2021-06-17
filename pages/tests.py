from django.test import TestCase
from django.shortcuts import reverse

# Create your tests here.


class LandingPageTest(TestCase):
    def test_status_code(self):
        response = self.client.get(reverse('pages:landing-page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/landing_page.html')
