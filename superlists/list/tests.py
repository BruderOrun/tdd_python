from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from list.views import home_page

class HomePageTest(TestCase): 
	'''тест домашней страницы'''
	def test_root_url_resolves_to_home_page_view(self): 
		'''тест: корневой url преобразуется в представление домашней страницы'''
		found = resolve('/')
		self.assertEqual(found.func, home_page)


	def test_homepage_returns_correct_html(self):
		''' тест: домашняя страницап возвращает правильный html'''
		request = HttpRequest()
		response = home_page(request)
		html = response.content.decode('utf8')
		self.assertTrue(html.startswith('<html>'))
		self.assertIn('<title>To-Do lists</title>', html)
		self.assertTrue(html.endswith('</html>'))


# class SmokeTest(TestCase):
# 	'''тест на токсичность'''
# 	def test_bad_maths(self):
# 		'''тест: неправильные математические расчеты'''
# 		self.assertEqual(1 + 1, 3)

# # Create your tests here.
