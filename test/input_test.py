import unittest


def check_free_word():
    free_word = input('検索ワードを入力してください(例:店名やジャンルなど) > ')
    if 1 <= len(free_word) <= 20:
        return True
    else:
        return False


class TestFreeWord(unittest.TestCase):
    def test_入力されたフリーワードが1文字以上20文字以下か確認(self):
        self.assertEqual(True, check_free_word())


def check_result_number():
    result_number = input('何件表示しますか？(1~100まで) > ')
    if 1 <= int(result_number) <= 100:
        return True
    else:
        return False


class TestResultNumber(unittest.TestCase):
    def test_入力された表示件数が1件以上100件以下か確認(self):
        self.assertEqual(True, check_result_number())

if __name__ == '__main__':
    unittest.main()
