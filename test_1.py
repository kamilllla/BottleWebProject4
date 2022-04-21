import unittest
import module1

class Test_test_1(unittest.TestCase):
    def test_A(self):
        mail=["Kamilla_balaeva@mail.ru", "contact-international@info.iu.org", "join@greenpeace.ru", "noreply@e.geekbrains.ru", "hello@jewelry-in-august.com", "info@email.cantata.ru", "selivanov@spb.ccrs.ru", "natbali@mail.ru", "lana_balaeva@mail.ru","alinka.balaeva@mail.ru","karonako2104@gmail.com","karinalyapkalo@ya.ru","vlad.xan2015@mail.ru"]
        for i in mail:
            self.assertTrue(module1.check(i))

if __name__ == '__main__':
    unittest.main()
