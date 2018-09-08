import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    """test identifiers"""
    def test_identifier_1(self):
        self.assertTrue(TestLexer.test("__abc_____","__abc_____,<EOF>",101))
    def test_identifier_2(self):
        self.assertTrue(TestLexer.test("_!___Babc","_,!,___Babc,<EOF>",102))
    def test_identifier_3(self):
        self.assertTrue(TestLexer.test("123ABC___","123,ABC___,<EOF>",103))
    def test_identifier_4(self):
        self.assertTrue(TestLexer.test("Aaaa__","Aaaa__,<EOF>",104))
    def test_identifier_5(self):
        self.assertTrue(TestLexer.test("!!@!@!@!@!@!@","!,!,@,!,@,!,@,!,@,!,@,!,@,<EOF>",105))
    def test_identifier_6(self):
        self.assertTrue(TestLexer.test("ABCDEFGHIJKLMNOPQRSTUVWXYZ123123123123","ABCDEFGHIJKLMNOPQRSTUVWXYZ123123123123,<EOF>",106))
    def test_identifier_7(self):
        self.assertTrue(TestLexer.test("_11111111111111111111111~~~~~~~","_11111111111111111111111,~,~,~,~,~,~,~,<EOF>",107))
    def test_identifier_8(self):
        self.assertTrue(TestLexer.test("......___asdasd","..,..,..,___asdasd,<EOF>",108))
    def test_identifier_9(self):
        self.assertTrue(TestLexer.test("tandung251298@gmail.com","tandung251298,@,gmail,.,com,<EOF>",109))
    def test_identifier_10(self):
        self.assertTrue(TestLexer.test("dung_dep_trai_____________","dung_dep_trai_____________,<EOF>",110))
        """test KEYWORDS"""
    def test_keywords_1(self):
        self.assertTrue(TestLexer.test("WhilE And","WhilE,And,<EOF>",111))
    def test_keywords_2(self):
        self.assertTrue(TestLexer.test("BeGINNNN AAND","BeGINNNN,AAND,<EOF>",112))
    def test_keywords_3(self):
        self.assertTrue(TestLexer.test("begin end do while","begin,end,do,while,<EOF>",113))
    def test_keywords_4(self):
        self.assertTrue(TestLexer.test("and or not but fuck","and,or,not,but,fuck,<EOF>",114))
    def test_keywords_5(self):
        self.assertTrue(TestLexer.test("!!!!and@@@@","!,!,!,!,and,@,@,@,@,<EOF>",115))
        """test OPERATOR"""
    def test_operator_1(self):
        self.assertTrue(TestLexer.test("112121212+12121212122/1212121212","112121212,+,12121212122,/,1212121212,<EOF>",141))
    def test_operator_2(self):
        self.assertTrue(TestLexer.test("a and as","a,and,as,<EOF>",142))
    def test_operator_3(self):
        self.assertTrue(TestLexer.test("< 123 >","<,123,>,<EOF>",143))
    def test_operator_4(self):
        self.assertTrue(TestLexer.test("<>123123","<>,123123,<EOF>",144))
    def test_operator_5(self):
        self.assertTrue(TestLexer.test("____123123asd<=12","____123123asd,<=,12,<EOF>",145))
        """test literal """
        """test integerLIT """
    def test_integer_1(self):
        self.assertTrue(TestLexer.test("-123123123123123123123123123123123","-,123123123123123123123123123123123,<EOF>",116))
    def test_integer_2(self):
        self.assertTrue(TestLexer.test("-12312312312312312-123123123123","-,12312312312312312,-,123123123123,<EOF>",117))
    def test_integer_3(self):
        self.assertTrue(TestLexer.test("-+12312312312312312312","-,+,12312312312312312312,<EOF>",118))
    def test_integer_4(self):
        self.assertTrue(TestLexer.test("+_+-____+123123123","+,_,+,-,____,+,123123123,<EOF>",119))
    def test_integer_5(self):
        self.assertTrue(TestLexer.test("__+123123123","__,+,123123123,<EOF>",120))
        """test floatLIT """
    def test_F_point_1(self):
        self.assertTrue(TestLexer.test("1.1e666666","1.1e666666,<EOF>",121))
    def test_F_point_2(self):
        self.assertTrue(TestLexer.test("1.e666666","1.,e666666,<EOF>",122))
    def test_F_point_3(self):
        self.assertTrue(TestLexer.test("-.12e666666","-,.12e666666,<EOF>",123))
    def test_F_point_4(self):
        self.assertTrue(TestLexer.test("12e12","12e12,<EOF>",124))
    def test_F_point_5(self):
        self.assertTrue(TestLexer.test("e12","e12,<EOF>",125))
    def test_F_point_6(self):
        self.assertTrue(TestLexer.test("0.0.0.0","0.0,.0,.0,<EOF>",126))
    def test_F_point_7(self):
        self.assertTrue(TestLexer.test("0.0e.e.e.e.e.e.e.e.e.e.e.123E3E3E3E3E3","0.0,e,.,e,.,e,.,e,.,e,.,e,.,e,.,e,.,e,.,e,.,e,.123E3,E3E3E3E3,<EOF>",127))
        """ test stringLIT"""
    def test_string_1(self):
        self.assertTrue(TestLexer.test("\"ajefjisejfiejifjeifja sejfi jweif iwejf w e\"","\"ajefjisejfiejifjeifja sejfi jweif iwejf w e\",<EOF>",128))
    # def test_string_2(self):
    #     self.assertTrue(TestLexer.test("\" \\\! \\\: aaaaaa\"","\" \\\! \\\: aaaaaa\",<EOF>",129))
    def test_string_3(self):
        self.assertTrue(TestLexer.test("\"\"asdasd\"","\"\",asdasd,\",<EOF>",130))
    def test_string_4(self):
        self.assertTrue(TestLexer.test("\"\\tasdfsadf\"","\"\\tasdfsadf\",<EOF>",131))
    def test_string_5(self):
        self.assertTrue(TestLexer.test("\"\"","\"\",<EOF>",132))
    def test_string_6(self):
        self.assertTrue(TestLexer.test("\"asdasd\t\"","\",asdasd,\",<EOF>",133))
    def test_string_7(self):
        self.assertTrue(TestLexer.test("\"asdasdasd\fqweqwe\\\"\"","\",asdasdasd,\f,qweqwe,\\,\"\",<EOF>",134))
    def test_string_8(self):
        self.assertTrue(TestLexer.test("\"asdasdasd\\tqweqwe\\\"\"","\"asdasdasd\\tqweqwe\\\"\",<EOF>",135))
    def test_string_9(self):
        self.assertTrue(TestLexer.test("\"asdasd\\n\"","\"asdasd\\n\",<EOF>",136))


    # def test_string(self):
    #     """test identifiers"""
    #     self.assertTrue(TestLexer.test("\"abc\"","\"abc\",<EOF>",104))
    # def test_string_1(self):
    #     self.assertTrue(TestLexer.test("\"bacas:!!!!\"","\"bacas:!!!!\",<EOF>",105))
    # def test_string_2(self):
    #     self.assertTrue(TestLexer.test("\"aAsVN\"\"","\"aAsVN\",\",<EOF>",106))
