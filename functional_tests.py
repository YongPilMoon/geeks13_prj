from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("/home/nick/webdriver/chromedriver")

    def tearDown(self):
        self.browser.quit()

    def test_start_site(self):
        # 릴리는 파이썬에 대한 질문을 올리기 위해 웹사이트에 접속한다
        self.browser.get('http://localhost:5000')

        # 웹 페이지 타이틀 헤더가 'Geeks13'을 표시하고 있다
        self.assertIn('Geeks13', self.browser.title)
        self.fail('Finish the test!')
        # 그녀는 글을 작성하기 위해 회원가입 페이지로 이동한다

if __name__ == '__main__':
    unittest.main(warnings='ignore')
