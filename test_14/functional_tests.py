from selenium import webdriver
import unittest

class QuestionTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_question_poll(self):
        browser = webdriver.Firefox()
        #ผู้ใช้เปิดหน้าเว็บขึ้นมา
        browser.get('http://localhost:8000/polls/1/')
        #เห็นชื่อ title
        self.assertIn('xxxx', self.browser.title)
        #เห็นคำถาม
        question_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('คำถาม', question_text)
        #เห็นตัวเลือก
        choice_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('ตัวเลือก', choice_text)


        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')

