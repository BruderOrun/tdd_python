from django.urls import resolve
from django.test import TestCase
from list.views import home_page

class HomePageTest(TestCase): 
	'''тест домашней страницы'''
	def test_root_url_resolves_to_home_page_view(self): 
		'''тест: корневой url преобразуется в представление домашней страницы'''
		found = resolve('/')
		self.assertEqual(found.func, home_page)


# class SmokeTest(TestCase):
# 	'''тест на токсичность'''
# 	def test_bad_maths(self):
# 		'''тест: неправильные математические расчеты'''
# 		self.assertEqual(1 + 1, 3)

# # Create your tests here.
