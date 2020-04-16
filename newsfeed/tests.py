from django.test import TestCase, SimpleTestCase
from django.urls import reverse


# Create your tests here.
class NewsfeedTest(SimpleTestCase):

    def test_home_path_status(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'newsfeed.html')
        self.assertTemplateUsed(response, 'nav.html')
