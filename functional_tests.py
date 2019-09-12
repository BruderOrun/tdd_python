from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys 
import time


# browser = webdriver.Firefox()
# # Эдит слышала про крутое новое онлайн-приложение со списком
# # неотложных дел. Она решает оценить его домашнюю страницу

# browser.get('http://localhost:8000')
# # Она видит, что заголовок и шапка страницы говорят о списках
# # неотложных дел

# assert 'To-Do' in browser.title, "Browser title was " + browser.title

# # Ей сразу же предлагается ввести элемент списка
# # Она набирает в текстовом поле "Купить павлиньи перья" (ее хобби – # вязание рыболовных мушек)
# # Когда она нажимает enter, страница обновляется, и теперь страница # содержит "1: Купить павлиньи перья" в качестве элемента списка
# # Текстовое поле по-прежнему приглашает ее добавить еще один элемент. # Она вводит "Сделать мушку из павлиньих перьев"
# # (Эдит очень методична)
# # Страница снова обновляется, и теперь показывает оба элемента ее списка
# # Эдит интересно, запомнит ли сайт ее список. Далее она видит, что # сайт сгенерировал для нее уникальный URL-адрес – об этом
# # выводится небольшой текст с объяснениями.
# # Она посещает этот URL-адрес – ее список по-прежнему там.
# # Удовлетворенная, она снова ложится спать
# browser.quit()

class NewVisitorTest(unittest.TestCase):
	'''тест нового посетителя'''
	def setUp(self):
		'''установка'''
		self.browser = webdriver.Firefox()
	def tearDown(self):
		'''демонтаж'''
		self.browser.quit()
	def test_can_start_a_list_and_retrieve_it_later(self):
		'''тест: можно начать список и получить его позже'''
		# Эдит слышала про крутое новое онлайн-приложение со
		# списком неотложных дел. Она решает оценить его
		# домашнюю страницу 
		self.browser.get('http://localhost:8000')
		# Она видит, что заголовок и шапка страницы говорят о # списках неотложных дел
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)
		# Ей сразу же предлагается ввести элемент списка
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
			)
		#она набирает в тестовом пуле "Купить павлиньи перья"
		# (ее хобби - вязвание рыболовных мушек)
		inputbox.send_keys('Купить павлиньи перья')

		# Когда она нажимает enter, страница обновляется, и теперь страница
		# содержит "1: Купить павлиньи перья" в качестве элемента списка
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_ekements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Купить павлиньи перья' for row in rows)
			)

		# Текстовое поле по-прежнему приглашает ее добавить еще один элемент.
		# Она вводит "Сделать мушку из павлиньих перьев"
		# (Эди очень методична)

		self.fail('Закончить тест!')
		# Страница снова обновляется и теперь показывает оба элемента # ее списка

if __name__ == '__main__':
	unittest.main(warnings='ignore')



