import unittest
import checkSnapshot

class TestCheckSnapshotMethods(unittest.TestCase):
    def test_should_return_success(self):
        inputpath = "src/unittest/case1.xml"
        outputpath = "src/unittest/result/case1.xml"
        message = checkSnapshot.checkVersion(inputpath, outputpath)
        self.assertEqual(message, checkSnapshot.MESSAGE_SUCCESS_REPLACE)

    def test_should_return_error_format(self):
        inputpath = "src/unittest/case2.xml"
        outputpath = ""
        message = checkSnapshot.checkVersion(inputpath, outputpath)
        self.assertEqual(message, checkSnapshot.MESSAGE_ERROR_FORMAT)

    def test_should_return_failed_syntax(self):
        inputpath = "src/unittest/case3.xml"
        outputpath = "src/unittest/result/case3.xml"
        message = checkSnapshot.checkVersion(inputpath, outputpath)
        self.assertEqual(message, checkSnapshot.MESSAGE_ERROR_SYNTAX)

    def test_should_return_failed_check(self):
        inputpath = "src/unittest/case4.xml"
        outputpath = "src/unittest/result/case4.xml"
        message = checkSnapshot.checkVersion(inputpath, outputpath)
        self.assertEqual(message, checkSnapshot.MESSAGE_FAILED_CHECK)

if __name__ == '__main__':
    unittest.main()
