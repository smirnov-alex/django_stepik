from django.test import TestCase
from .zodiac_data import zodiac_dict


class TestHoroscope(TestCase):

    def test_index(self):
        response = self.client.get('/horoscope/')
        self.assertEqual(response.status_code, 200)

    def test_libra(self):
        response = self.client.get('/horoscope/libra')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
                      response.content.decode())

    def test_redirect(self):
        zodiac_list = list(zodiac_dict)
        for i in range(1, 13):
            response = self.client.get(f'/horoscope/{i}')
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, f'/horoscope/{zodiac_list[i-1]}')

    def test_signs(self):
        for key in zodiac_dict.keys():
            response = self.client.get(f'/horoscope/{key}')
            self.assertEqual(response.status_code, 200)
            self.assertIn(zodiac_dict[key],
                          response.content.decode())
