import unittest
import oxo_dialog_ui

class test_unit(unittest.TestCase):
    
    def startGame_test(self):
        l = list(" " * 9)
        self.assertEqual(oxo_dialog_ui.startGame(),l)
    def quitGame_test(self):
        self.assertRaises(oxo_dialog_ui.quit, SystemExit)
   



if __name__ == '__main__':
    unittest.main()