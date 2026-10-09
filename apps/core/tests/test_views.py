
from django.test import TestCase
from django.urls import reverse


class SobrePageViewTest(TestCase):
    def test_sobre_page_renders(self):
        response = self.client.get(reverse('core:sobre'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/sobre.html')
        self.assertContains(response, 'Sobre')

    def test_sobre_url_resolves_to_sobre_path(self):
        self.assertEqual(reverse('core:sobre'), '/sobre/')