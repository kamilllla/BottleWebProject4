import unittest
import module1
class Test_test_2(unittest.TestCase):
    def test_mail_not_suited(self):
        mail=[ "\contact\'internat\'ional@info.iu.org","io@nal@info.iu.org","oingreenpeace.ru","selivanov.@spb.ccrs.ru","abcdefghixyz_@example.com","bcdefghixyz_@example.com", "h<e>llo@jewelry-in-august.com", "info@e@mail.cantata.ru", "alinka.()[]balaeva@mail.ru", "karonako'210'4@gmail.com", "@ya.ru", "vlad.xan2015@mail..ru"]
        for i in mail:
            self.assertFalse(module1.check(i))
if __name__ == '__main__':
    unittest.main()
