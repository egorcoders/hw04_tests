from http import HTTPStatus

from django.test import Client, TestCase
from django.urls import reverse


class AboutViewsTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.guest_client = Client()
        cls.templates_url_names = {
            'about/author.html': 'about:author',
            'about/tech.html': 'about:tech',
        }

    def test_about_pages_are_accessible_by_name(self):
        """Проверка доступны ли страницы неавторизованному пользователю."""
        for template, reverse_name in self.templates_url_names.items():
            with self.subTest():
                response = self.guest_client.get(reverse(reverse_name))
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_about_pages_use_correct_template(self):
        """Проверка используются ли корректные шаблоны в приложении about."""
        for template, reverse_name in self.templates_url_names.items():
            with self.subTest():
                response = self.guest_client.get(reverse(reverse_name))
                self.assertTemplateUsed(response, template)
