# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u027c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\6\5\u00d1\n\5\r\5\16\5\u00d2\3")
        buf.write("\6\6\6\u00d6\n\6\r\6\16\6\u00d7\3\7\3\7\3\b\3\b\3\t\3")
        buf.write("\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3")
        buf.write("\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37")
        buf.write("\3 \3 \3!\3!\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#")
        buf.write("\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\5#\u012c")
        buf.write("\n#\3$\3$\5$\u0130\n$\3$\3$\7$\u0134\n$\f$\16$\u0137\13")
        buf.write("$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'")
        buf.write("\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3+\3+")
        buf.write("\3+\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\61")
        buf.write("\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67\38")
        buf.write("\38\38\39\39\39\39\39\3:\3:\3:\3:\3:\3:\3:\3:\3;\3;\3")
        buf.write(";\3;\3;\3;\3;\3;\3<\3<\3<\3<\3<\3<\3<\3=\3=\3=\3=\3>\3")
        buf.write(">\3>\3>\3?\3?\3?\3@\3@\3@\3@\3A\3A\3A\3A\3B\3B\3C\3C\3")
        buf.write("D\3D\3D\3D\3E\3E\3E\3F\3F\3F\3G\3G\3H\3H\3H\3I\3I\3I\3")
        buf.write("I\3J\3J\3K\3K\3L\3L\3L\3L\3M\3M\3M\3M\3N\3N\3O\3O\3P\3")
        buf.write("P\3P\3Q\3Q\3R\3R\3S\3S\3T\3T\3U\3U\3V\3V\3V\3W\3W\3X\3")
        buf.write("X\3Y\6Y\u0213\nY\rY\16Y\u0214\3Z\6Z\u0218\nZ\rZ\16Z\u0219")
        buf.write("\3Z\3Z\5Z\u021e\nZ\3Z\6Z\u0221\nZ\rZ\16Z\u0222\3Z\7Z\u0226")
        buf.write("\nZ\fZ\16Z\u0229\13Z\3Z\3Z\6Z\u022d\nZ\rZ\16Z\u022e\3")
        buf.write("Z\3Z\5Z\u0233\nZ\3Z\6Z\u0236\nZ\rZ\16Z\u0237\3Z\6Z\u023b")
        buf.write("\nZ\rZ\16Z\u023c\3Z\3Z\7Z\u0241\nZ\fZ\16Z\u0244\13Z\3")
        buf.write("Z\7Z\u0247\nZ\fZ\16Z\u024a\13Z\3Z\3Z\6Z\u024e\nZ\rZ\16")
        buf.write("Z\u024f\5Z\u0252\nZ\3[\3[\3[\3[\3[\3[\3[\3[\3[\5[\u025d")
        buf.write("\n[\3\\\3\\\3\\\3\\\3\\\3\\\3\\\3\\\3\\\3\\\7\\\u0269")
        buf.write("\n\\\f\\\16\\\u026c\13\\\3\\\3\\\3]\6]\u0271\n]\r]\16")
        buf.write("]\u0272\3]\3]\3^\3^\3_\3_\3`\3`\2\2a\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\2\23\2\25\2\27\2\31\2\33\2\35\2\37\2!\2")
        buf.write("#\2%\2\'\2)\2+\2-\2/\2\61\2\63\2\65\2\67\29\2;\2=\2?\2")
        buf.write("A\2C\2E\2G\nI\13K\fM\rO\16Q\17S\20U\21W\22Y\23[\24]\25")
        buf.write("_\26a\27c\30e\31g\32i\33k\34m\35o\36q\37s u!w\"y#{$}%")
        buf.write("\177&\u0081\'\u0083(\u0085)\u0087*\u0089+\u008b,\u008d")
        buf.write("-\u008f.\u0091/\u0093\60\u0095\61\u0097\62\u0099\63\u009b")
        buf.write("\64\u009d\65\u009f\66\u00a1\67\u00a38\u00a59\u00a7:\u00a9")
        buf.write(";\u00ab<\u00ad=\u00af>\u00b1?\u00b3@\u00b5A\u00b7B\u00b9")
        buf.write("C\u00bb\2\u00bdD\u00bfE\3\2\"\4\2C\\c|\3\2\62;\4\2CCc")
        buf.write("c\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4\2")
        buf.write("JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4")
        buf.write("\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWw")
        buf.write("w\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\4\2\62;aa")
        buf.write("\7\2\n\f\16\17$$))^^\5\2\13\f\17\17\"\"\5\2\n\f\16\17")
        buf.write("^^\2\u0293\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2G\3\2\2\2")
        buf.write("\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2")
        buf.write("\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2")
        buf.write("\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3")
        buf.write("\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o")
        buf.write("\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2")
        buf.write("y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2")
        buf.write("\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d")
        buf.write("\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2")
        buf.write("\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab")
        buf.write("\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2")
        buf.write("\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9")
        buf.write("\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf\3\2\2\2\3\u00c1\3\2\2")
        buf.write("\2\5\u00c6\3\2\2\2\7\u00ca\3\2\2\2\t\u00d0\3\2\2\2\13")
        buf.write("\u00d5\3\2\2\2\r\u00d9\3\2\2\2\17\u00db\3\2\2\2\21\u00dd")
        buf.write("\3\2\2\2\23\u00df\3\2\2\2\25\u00e1\3\2\2\2\27\u00e3\3")
        buf.write("\2\2\2\31\u00e5\3\2\2\2\33\u00e7\3\2\2\2\35\u00e9\3\2")
        buf.write("\2\2\37\u00eb\3\2\2\2!\u00ed\3\2\2\2#\u00ef\3\2\2\2%\u00f1")
        buf.write("\3\2\2\2\'\u00f3\3\2\2\2)\u00f5\3\2\2\2+\u00f7\3\2\2\2")
        buf.write("-\u00f9\3\2\2\2/\u00fb\3\2\2\2\61\u00fd\3\2\2\2\63\u00ff")
        buf.write("\3\2\2\2\65\u0101\3\2\2\2\67\u0103\3\2\2\29\u0105\3\2")
        buf.write("\2\2;\u0107\3\2\2\2=\u0109\3\2\2\2?\u010b\3\2\2\2A\u010d")
        buf.write("\3\2\2\2C\u010f\3\2\2\2E\u012b\3\2\2\2G\u012f\3\2\2\2")
        buf.write("I\u0138\3\2\2\2K\u013e\3\2\2\2M\u0147\3\2\2\2O\u014b\3")
        buf.write("\2\2\2Q\u014e\3\2\2\2S\u0155\3\2\2\2U\u0158\3\2\2\2W\u015b")
        buf.write("\3\2\2\2Y\u0160\3\2\2\2[\u0165\3\2\2\2]\u016c\3\2\2\2")
        buf.write("_\u0172\3\2\2\2a\u0178\3\2\2\2c\u017c\3\2\2\2e\u0185\3")
        buf.write("\2\2\2g\u018f\3\2\2\2i\u0193\3\2\2\2k\u0198\3\2\2\2m\u019e")
        buf.write("\3\2\2\2o\u01a4\3\2\2\2q\u01a7\3\2\2\2s\u01ac\3\2\2\2")
        buf.write("u\u01b4\3\2\2\2w\u01bc\3\2\2\2y\u01c3\3\2\2\2{\u01c7\3")
        buf.write("\2\2\2}\u01cb\3\2\2\2\177\u01ce\3\2\2\2\u0081\u01d2\3")
        buf.write("\2\2\2\u0083\u01d6\3\2\2\2\u0085\u01d8\3\2\2\2\u0087\u01da")
        buf.write("\3\2\2\2\u0089\u01de\3\2\2\2\u008b\u01e1\3\2\2\2\u008d")
        buf.write("\u01e4\3\2\2\2\u008f\u01e6\3\2\2\2\u0091\u01e9\3\2\2\2")
        buf.write("\u0093\u01ed\3\2\2\2\u0095\u01ef\3\2\2\2\u0097\u01f1\3")
        buf.write("\2\2\2\u0099\u01f5\3\2\2\2\u009b\u01f9\3\2\2\2\u009d\u01fb")
        buf.write("\3\2\2\2\u009f\u01fd\3\2\2\2\u00a1\u0200\3\2\2\2\u00a3")
        buf.write("\u0202\3\2\2\2\u00a5\u0204\3\2\2\2\u00a7\u0206\3\2\2\2")
        buf.write("\u00a9\u0208\3\2\2\2\u00ab\u020a\3\2\2\2\u00ad\u020d\3")
        buf.write("\2\2\2\u00af\u020f\3\2\2\2\u00b1\u0212\3\2\2\2\u00b3\u0251")
        buf.write("\3\2\2\2\u00b5\u025c\3\2\2\2\u00b7\u025e\3\2\2\2\u00b9")
        buf.write("\u0270\3\2\2\2\u00bb\u0276\3\2\2\2\u00bd\u0278\3\2\2\2")
        buf.write("\u00bf\u027a\3\2\2\2\u00c1\u00c2\7o\2\2\u00c2\u00c3\7")
        buf.write("c\2\2\u00c3\u00c4\7k\2\2\u00c4\u00c5\7p\2\2\u00c5\4\3")
        buf.write("\2\2\2\u00c6\u00c7\7k\2\2\u00c7\u00c8\7p\2\2\u00c8\u00c9")
        buf.write("\7v\2\2\u00c9\6\3\2\2\2\u00ca\u00cb\7x\2\2\u00cb\u00cc")
        buf.write("\7q\2\2\u00cc\u00cd\7k\2\2\u00cd\u00ce\7f\2\2\u00ce\b")
        buf.write("\3\2\2\2\u00cf\u00d1\t\2\2\2\u00d0\u00cf\3\2\2\2\u00d1")
        buf.write("\u00d2\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2")
        buf.write("\u00d3\n\3\2\2\2\u00d4\u00d6\t\3\2\2\u00d5\u00d4\3\2\2")
        buf.write("\2\u00d6\u00d7\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d7\u00d8")
        buf.write("\3\2\2\2\u00d8\f\3\2\2\2\u00d9\u00da\7}\2\2\u00da\16\3")
        buf.write("\2\2\2\u00db\u00dc\7\177\2\2\u00dc\20\3\2\2\2\u00dd\u00de")
        buf.write("\t\4\2\2\u00de\22\3\2\2\2\u00df\u00e0\t\5\2\2\u00e0\24")
        buf.write("\3\2\2\2\u00e1\u00e2\t\6\2\2\u00e2\26\3\2\2\2\u00e3\u00e4")
        buf.write("\t\7\2\2\u00e4\30\3\2\2\2\u00e5\u00e6\t\b\2\2\u00e6\32")
        buf.write("\3\2\2\2\u00e7\u00e8\t\t\2\2\u00e8\34\3\2\2\2\u00e9\u00ea")
        buf.write("\t\n\2\2\u00ea\36\3\2\2\2\u00eb\u00ec\t\13\2\2\u00ec ")
        buf.write("\3\2\2\2\u00ed\u00ee\t\f\2\2\u00ee\"\3\2\2\2\u00ef\u00f0")
        buf.write("\t\r\2\2\u00f0$\3\2\2\2\u00f1\u00f2\t\16\2\2\u00f2&\3")
        buf.write("\2\2\2\u00f3\u00f4\t\17\2\2\u00f4(\3\2\2\2\u00f5\u00f6")
        buf.write("\t\20\2\2\u00f6*\3\2\2\2\u00f7\u00f8\t\21\2\2\u00f8,\3")
        buf.write("\2\2\2\u00f9\u00fa\t\22\2\2\u00fa.\3\2\2\2\u00fb\u00fc")
        buf.write("\t\23\2\2\u00fc\60\3\2\2\2\u00fd\u00fe\t\24\2\2\u00fe")
        buf.write("\62\3\2\2\2\u00ff\u0100\t\25\2\2\u0100\64\3\2\2\2\u0101")
        buf.write("\u0102\t\26\2\2\u0102\66\3\2\2\2\u0103\u0104\t\27\2\2")
        buf.write("\u01048\3\2\2\2\u0105\u0106\t\30\2\2\u0106:\3\2\2\2\u0107")
        buf.write("\u0108\t\31\2\2\u0108<\3\2\2\2\u0109\u010a\t\32\2\2\u010a")
        buf.write(">\3\2\2\2\u010b\u010c\t\33\2\2\u010c@\3\2\2\2\u010d\u010e")
        buf.write("\t\34\2\2\u010eB\3\2\2\2\u010f\u0110\t\35\2\2\u0110D\3")
        buf.write("\2\2\2\u0111\u012c\5\21\t\2\u0112\u012c\5\23\n\2\u0113")
        buf.write("\u012c\5\25\13\2\u0114\u012c\5\27\f\2\u0115\u012c\5\31")
        buf.write("\r\2\u0116\u012c\5\33\16\2\u0117\u012c\5\35\17\2\u0118")
        buf.write("\u012c\5\37\20\2\u0119\u012c\5!\21\2\u011a\u012c\5#\22")
        buf.write("\2\u011b\u012c\5%\23\2\u011c\u012c\5\'\24\2\u011d\u012c")
        buf.write("\5)\25\2\u011e\u012c\5+\26\2\u011f\u012c\5-\27\2\u0120")
        buf.write("\u012c\5/\30\2\u0121\u012c\5\61\31\2\u0122\u012c\5\63")
        buf.write("\32\2\u0123\u012c\5\65\33\2\u0124\u012c\5\67\34\2\u0125")
        buf.write("\u012c\59\35\2\u0126\u012c\5;\36\2\u0127\u012c\5=\37\2")
        buf.write("\u0128\u012c\5? \2\u0129\u012c\5A!\2\u012a\u012c\5C\"")
        buf.write("\2\u012b\u0111\3\2\2\2\u012b\u0112\3\2\2\2\u012b\u0113")
        buf.write("\3\2\2\2\u012b\u0114\3\2\2\2\u012b\u0115\3\2\2\2\u012b")
        buf.write("\u0116\3\2\2\2\u012b\u0117\3\2\2\2\u012b\u0118\3\2\2\2")
        buf.write("\u012b\u0119\3\2\2\2\u012b\u011a\3\2\2\2\u012b\u011b\3")
        buf.write("\2\2\2\u012b\u011c\3\2\2\2\u012b\u011d\3\2\2\2\u012b\u011e")
        buf.write("\3\2\2\2\u012b\u011f\3\2\2\2\u012b\u0120\3\2\2\2\u012b")
        buf.write("\u0121\3\2\2\2\u012b\u0122\3\2\2\2\u012b\u0123\3\2\2\2")
        buf.write("\u012b\u0124\3\2\2\2\u012b\u0125\3\2\2\2\u012b\u0126\3")
        buf.write("\2\2\2\u012b\u0127\3\2\2\2\u012b\u0128\3\2\2\2\u012b\u0129")
        buf.write("\3\2\2\2\u012b\u012a\3\2\2\2\u012cF\3\2\2\2\u012d\u0130")
        buf.write("\5E#\2\u012e\u0130\7a\2\2\u012f\u012d\3\2\2\2\u012f\u012e")
        buf.write("\3\2\2\2\u0130\u0135\3\2\2\2\u0131\u0134\t\36\2\2\u0132")
        buf.write("\u0134\5E#\2\u0133\u0131\3\2\2\2\u0133\u0132\3\2\2\2\u0134")
        buf.write("\u0137\3\2\2\2\u0135\u0133\3\2\2\2\u0135\u0136\3\2\2\2")
        buf.write("\u0136H\3\2\2\2\u0137\u0135\3\2\2\2\u0138\u0139\5\23\n")
        buf.write("\2\u0139\u013a\5\63\32\2\u013a\u013b\5\31\r\2\u013b\u013c")
        buf.write("\5\21\t\2\u013c\u013d\5%\23\2\u013dJ\3\2\2\2\u013e\u013f")
        buf.write("\5\25\13\2\u013f\u0140\5-\27\2\u0140\u0141\5+\26\2\u0141")
        buf.write("\u0142\5\67\34\2\u0142\u0143\5!\21\2\u0143\u0144\5+\26")
        buf.write("\2\u0144\u0145\59\35\2\u0145\u0146\5\31\r\2\u0146L\3\2")
        buf.write("\2\2\u0147\u0148\5\33\16\2\u0148\u0149\5-\27\2\u0149\u014a")
        buf.write("\5\63\32\2\u014aN\3\2\2\2\u014b\u014c\5\67\34\2\u014c")
        buf.write("\u014d\5-\27\2\u014dP\3\2\2\2\u014e\u014f\5\27\f\2\u014f")
        buf.write("\u0150\5-\27\2\u0150\u0151\5=\37\2\u0151\u0152\5+\26\2")
        buf.write("\u0152\u0153\5\67\34\2\u0153\u0154\5-\27\2\u0154R\3\2")
        buf.write("\2\2\u0155\u0156\5\27\f\2\u0156\u0157\5-\27\2\u0157T\3")
        buf.write("\2\2\2\u0158\u0159\5!\21\2\u0159\u015a\5\33\16\2\u015a")
        buf.write("V\3\2\2\2\u015b\u015c\5\67\34\2\u015c\u015d\5\37\20\2")
        buf.write("\u015d\u015e\5\31\r\2\u015e\u015f\5+\26\2\u015fX\3\2\2")
        buf.write("\2\u0160\u0161\5\31\r\2\u0161\u0162\5\'\24\2\u0162\u0163")
        buf.write("\5\65\33\2\u0163\u0164\5\31\r\2\u0164Z\3\2\2\2\u0165\u0166")
        buf.write("\5\63\32\2\u0166\u0167\5\31\r\2\u0167\u0168\5\67\34\2")
        buf.write("\u0168\u0169\59\35\2\u0169\u016a\5\63\32\2\u016a\u016b")
        buf.write("\5+\26\2\u016b\\\3\2\2\2\u016c\u016d\5=\37\2\u016d\u016e")
        buf.write("\5\37\20\2\u016e\u016f\5!\21\2\u016f\u0170\5\'\24\2\u0170")
        buf.write("\u0171\5\31\r\2\u0171^\3\2\2\2\u0172\u0173\5\23\n\2\u0173")
        buf.write("\u0174\5\31\r\2\u0174\u0175\5\35\17\2\u0175\u0176\5!\21")
        buf.write("\2\u0176\u0177\5+\26\2\u0177`\3\2\2\2\u0178\u0179\5\31")
        buf.write("\r\2\u0179\u017a\5+\26\2\u017a\u017b\5\27\f\2\u017bb\3")
        buf.write("\2\2\2\u017c\u017d\5\33\16\2\u017d\u017e\59\35\2\u017e")
        buf.write("\u017f\5+\26\2\u017f\u0180\5\25\13\2\u0180\u0181\5\67")
        buf.write("\34\2\u0181\u0182\5!\21\2\u0182\u0183\5-\27\2\u0183\u0184")
        buf.write("\5+\26\2\u0184d\3\2\2\2\u0185\u0186\5/\30\2\u0186\u0187")
        buf.write("\5\63\32\2\u0187\u0188\5-\27\2\u0188\u0189\5\25\13\2\u0189")
        buf.write("\u018a\5\31\r\2\u018a\u018b\5\27\f\2\u018b\u018c\59\35")
        buf.write("\2\u018c\u018d\5\63\32\2\u018d\u018e\5\31\r\2\u018ef\3")
        buf.write("\2\2\2\u018f\u0190\5;\36\2\u0190\u0191\5\21\t\2\u0191")
        buf.write("\u0192\5\63\32\2\u0192h\3\2\2\2\u0193\u0194\5\67\34\2")
        buf.write("\u0194\u0195\5\63\32\2\u0195\u0196\59\35\2\u0196\u0197")
        buf.write("\5\31\r\2\u0197j\3\2\2\2\u0198\u0199\5\33\16\2\u0199\u019a")
        buf.write("\5\21\t\2\u019a\u019b\5\'\24\2\u019b\u019c\5\65\33\2\u019c")
        buf.write("\u019d\5\31\r\2\u019dl\3\2\2\2\u019e\u019f\5\21\t\2\u019f")
        buf.write("\u01a0\5\63\32\2\u01a0\u01a1\5\63\32\2\u01a1\u01a2\5\21")
        buf.write("\t\2\u01a2\u01a3\5A!\2\u01a3n\3\2\2\2\u01a4\u01a5\5-\27")
        buf.write("\2\u01a5\u01a6\5\33\16\2\u01a6p\3\2\2\2\u01a7\u01a8\5")
        buf.write("\63\32\2\u01a8\u01a9\5\31\r\2\u01a9\u01aa\5\21\t\2\u01aa")
        buf.write("\u01ab\5\'\24\2\u01abr\3\2\2\2\u01ac\u01ad\5\23\n\2\u01ad")
        buf.write("\u01ae\5-\27\2\u01ae\u01af\5-\27\2\u01af\u01b0\5\'\24")
        buf.write("\2\u01b0\u01b1\5\31\r\2\u01b1\u01b2\5\21\t\2\u01b2\u01b3")
        buf.write("\5+\26\2\u01b3t\3\2\2\2\u01b4\u01b5\5!\21\2\u01b5\u01b6")
        buf.write("\5+\26\2\u01b6\u01b7\5\67\34\2\u01b7\u01b8\5\31\r\2\u01b8")
        buf.write("\u01b9\5\35\17\2\u01b9\u01ba\5\31\r\2\u01ba\u01bb\5\63")
        buf.write("\32\2\u01bbv\3\2\2\2\u01bc\u01bd\5\65\33\2\u01bd\u01be")
        buf.write("\5\67\34\2\u01be\u01bf\5\63\32\2\u01bf\u01c0\5!\21\2\u01c0")
        buf.write("\u01c1\5+\26\2\u01c1\u01c2\5\35\17\2\u01c2x\3\2\2\2\u01c3")
        buf.write("\u01c4\5+\26\2\u01c4\u01c5\5-\27\2\u01c5\u01c6\5\67\34")
        buf.write("\2\u01c6z\3\2\2\2\u01c7\u01c8\5\21\t\2\u01c8\u01c9\5+")
        buf.write("\26\2\u01c9\u01ca\5\27\f\2\u01ca|\3\2\2\2\u01cb\u01cc")
        buf.write("\5-\27\2\u01cc\u01cd\5\63\32\2\u01cd~\3\2\2\2\u01ce\u01cf")
        buf.write("\5\27\f\2\u01cf\u01d0\5!\21\2\u01d0\u01d1\5;\36\2\u01d1")
        buf.write("\u0080\3\2\2\2\u01d2\u01d3\5)\25\2\u01d3\u01d4\5-\27\2")
        buf.write("\u01d4\u01d5\5\27\f\2\u01d5\u0082\3\2\2\2\u01d6\u01d7")
        buf.write("\7-\2\2\u01d7\u0084\3\2\2\2\u01d8\u01d9\7,\2\2\u01d9\u0086")
        buf.write("\3\2\2\2\u01da\u01db\7p\2\2\u01db\u01dc\7q\2\2\u01dc\u01dd")
        buf.write("\7v\2\2\u01dd\u0088\3\2\2\2\u01de\u01df\7q\2\2\u01df\u01e0")
        buf.write("\7t\2\2\u01e0\u008a\3\2\2\2\u01e1\u01e2\7>\2\2\u01e2\u01e3")
        buf.write("\7@\2\2\u01e3\u008c\3\2\2\2\u01e4\u01e5\7>\2\2\u01e5\u008e")
        buf.write("\3\2\2\2\u01e6\u01e7\7>\2\2\u01e7\u01e8\7?\2\2\u01e8\u0090")
        buf.write("\3\2\2\2\u01e9\u01ea\7f\2\2\u01ea\u01eb\7k\2\2\u01eb\u01ec")
        buf.write("\7x\2\2\u01ec\u0092\3\2\2\2\u01ed\u01ee\7/\2\2\u01ee\u0094")
        buf.write("\3\2\2\2\u01ef\u01f0\7\61\2\2\u01f0\u0096\3\2\2\2\u01f1")
        buf.write("\u01f2\7o\2\2\u01f2\u01f3\7q\2\2\u01f3\u01f4\7f\2\2\u01f4")
        buf.write("\u0098\3\2\2\2\u01f5\u01f6\7c\2\2\u01f6\u01f7\7p\2\2\u01f7")
        buf.write("\u01f8\7f\2\2\u01f8\u009a\3\2\2\2\u01f9\u01fa\7?\2\2\u01fa")
        buf.write("\u009c\3\2\2\2\u01fb\u01fc\7@\2\2\u01fc\u009e\3\2\2\2")
        buf.write("\u01fd\u01fe\7@\2\2\u01fe\u01ff\7?\2\2\u01ff\u00a0\3\2")
        buf.write("\2\2\u0200\u0201\7]\2\2\u0201\u00a2\3\2\2\2\u0202\u0203")
        buf.write("\7_\2\2\u0203\u00a4\3\2\2\2\u0204\u0205\7*\2\2\u0205\u00a6")
        buf.write("\3\2\2\2\u0206\u0207\7+\2\2\u0207\u00a8\3\2\2\2\u0208")
        buf.write("\u0209\7=\2\2\u0209\u00aa\3\2\2\2\u020a\u020b\7\60\2\2")
        buf.write("\u020b\u020c\7\60\2\2\u020c\u00ac\3\2\2\2\u020d\u020e")
        buf.write("\7.\2\2\u020e\u00ae\3\2\2\2\u020f\u0210\7<\2\2\u0210\u00b0")
        buf.write("\3\2\2\2\u0211\u0213\t\3\2\2\u0212\u0211\3\2\2\2\u0213")
        buf.write("\u0214\3\2\2\2\u0214\u0212\3\2\2\2\u0214\u0215\3\2\2\2")
        buf.write("\u0215\u00b2\3\2\2\2\u0216\u0218\t\3\2\2\u0217\u0216\3")
        buf.write("\2\2\2\u0218\u0219\3\2\2\2\u0219\u0217\3\2\2\2\u0219\u021a")
        buf.write("\3\2\2\2\u021a\u021b\3\2\2\2\u021b\u021d\t\b\2\2\u021c")
        buf.write("\u021e\7/\2\2\u021d\u021c\3\2\2\2\u021d\u021e\3\2\2\2")
        buf.write("\u021e\u0220\3\2\2\2\u021f\u0221\t\3\2\2\u0220\u021f\3")
        buf.write("\2\2\2\u0221\u0222\3\2\2\2\u0222\u0220\3\2\2\2\u0222\u0223")
        buf.write("\3\2\2\2\u0223\u0252\3\2\2\2\u0224\u0226\t\3\2\2\u0225")
        buf.write("\u0224\3\2\2\2\u0226\u0229\3\2\2\2\u0227\u0225\3\2\2\2")
        buf.write("\u0227\u0228\3\2\2\2\u0228\u022a\3\2\2\2\u0229\u0227\3")
        buf.write("\2\2\2\u022a\u022c\7\60\2\2\u022b\u022d\t\3\2\2\u022c")
        buf.write("\u022b\3\2\2\2\u022d\u022e\3\2\2\2\u022e\u022c\3\2\2\2")
        buf.write("\u022e\u022f\3\2\2\2\u022f\u0230\3\2\2\2\u0230\u0232\t")
        buf.write("\b\2\2\u0231\u0233\7/\2\2\u0232\u0231\3\2\2\2\u0232\u0233")
        buf.write("\3\2\2\2\u0233\u0235\3\2\2\2\u0234\u0236\t\3\2\2\u0235")
        buf.write("\u0234\3\2\2\2\u0236\u0237\3\2\2\2\u0237\u0235\3\2\2\2")
        buf.write("\u0237\u0238\3\2\2\2\u0238\u0252\3\2\2\2\u0239\u023b\t")
        buf.write("\3\2\2\u023a\u0239\3\2\2\2\u023b\u023c\3\2\2\2\u023c\u023a")
        buf.write("\3\2\2\2\u023c\u023d\3\2\2\2\u023d\u023e\3\2\2\2\u023e")
        buf.write("\u0242\7\60\2\2\u023f\u0241\t\3\2\2\u0240\u023f\3\2\2")
        buf.write("\2\u0241\u0244\3\2\2\2\u0242\u0240\3\2\2\2\u0242\u0243")
        buf.write("\3\2\2\2\u0243\u0252\3\2\2\2\u0244\u0242\3\2\2\2\u0245")
        buf.write("\u0247\t\3\2\2\u0246\u0245\3\2\2\2\u0247\u024a\3\2\2\2")
        buf.write("\u0248\u0246\3\2\2\2\u0248\u0249\3\2\2\2\u0249\u024b\3")
        buf.write("\2\2\2\u024a\u0248\3\2\2\2\u024b\u024d\7\60\2\2\u024c")
        buf.write("\u024e\t\3\2\2\u024d\u024c\3\2\2\2\u024e\u024f\3\2\2\2")
        buf.write("\u024f\u024d\3\2\2\2\u024f\u0250\3\2\2\2\u0250\u0252\3")
        buf.write("\2\2\2\u0251\u0217\3\2\2\2\u0251\u0227\3\2\2\2\u0251\u023a")
        buf.write("\3\2\2\2\u0251\u0248\3\2\2\2\u0252\u00b4\3\2\2\2\u0253")
        buf.write("\u0254\7v\2\2\u0254\u0255\7t\2\2\u0255\u0256\7w\2\2\u0256")
        buf.write("\u025d\7g\2\2\u0257\u0258\7h\2\2\u0258\u0259\7c\2\2\u0259")
        buf.write("\u025a\7n\2\2\u025a\u025b\7u\2\2\u025b\u025d\7g\2\2\u025c")
        buf.write("\u0253\3\2\2\2\u025c\u0257\3\2\2\2\u025d\u00b6\3\2\2\2")
        buf.write("\u025e\u026a\7$\2\2\u025f\u0260\7^\2\2\u0260\u0269\7v")
        buf.write("\2\2\u0261\u0262\7^\2\2\u0262\u0269\7^\2\2\u0263\u0264")
        buf.write("\7^\2\2\u0264\u0269\7p\2\2\u0265\u0266\7^\2\2\u0266\u0269")
        buf.write("\7$\2\2\u0267\u0269\n\37\2\2\u0268\u025f\3\2\2\2\u0268")
        buf.write("\u0261\3\2\2\2\u0268\u0263\3\2\2\2\u0268\u0265\3\2\2\2")
        buf.write("\u0268\u0267\3\2\2\2\u0269\u026c\3\2\2\2\u026a\u0268\3")
        buf.write("\2\2\2\u026a\u026b\3\2\2\2\u026b\u026d\3\2\2\2\u026c\u026a")
        buf.write("\3\2\2\2\u026d\u026e\7$\2\2\u026e\u00b8\3\2\2\2\u026f")
        buf.write("\u0271\t \2\2\u0270\u026f\3\2\2\2\u0271\u0272\3\2\2\2")
        buf.write("\u0272\u0270\3\2\2\2\u0272\u0273\3\2\2\2\u0273\u0274\3")
        buf.write("\2\2\2\u0274\u0275\b]\2\2\u0275\u00ba\3\2\2\2\u0276\u0277")
        buf.write("\t!\2\2\u0277\u00bc\3\2\2\2\u0278\u0279\13\2\2\2\u0279")
        buf.write("\u00be\3\2\2\2\u027a\u027b\13\2\2\2\u027b\u00c0\3\2\2")
        buf.write("\2\32\2\u00d2\u00d7\u012b\u012f\u0133\u0135\u0214\u0219")
        buf.write("\u021d\u0222\u0227\u022e\u0232\u0237\u023c\u0242\u0248")
        buf.write("\u024f\u0251\u025c\u0268\u026a\u0272\3\b\2\2")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INTTYPE = 2
    VOIDTYPE = 3
    ID = 4
    INTLIT = 5
    LP = 6
    RP = 7
    IDENTIFIERS = 8
    BREAK = 9
    CONTINUE = 10
    FOR = 11
    TO = 12
    DOWNTO = 13
    DO = 14
    IF = 15
    THEN = 16
    ELSE = 17
    RETURN = 18
    WHILE = 19
    BEGIN = 20
    END = 21
    FUNCTION = 22
    PROCEDURE = 23
    VAR = 24
    TRUE = 25
    FALSE = 26
    ARRAY = 27
    OF = 28
    REAL = 29
    BOOLEAN = 30
    INTEGER = 31
    STRING = 32
    NOT = 33
    AND = 34
    OR = 35
    DIV = 36
    MOD = 37
    ADDITION = 38
    MULTIPLICATION = 39
    LOGICAL_NOT = 40
    LOGICAL_OR = 41
    NOT_EQUAL = 42
    LESS_THAN = 43
    LESS_THAN_OR_EQUAL = 44
    INTEGER_DIVISION = 45
    SUBSTACTION = 46
    DIVISION = 47
    MODULUS = 48
    LOGICAL_AND = 49
    EQUAL = 50
    GREATER_THAN = 51
    GREATER_THAN_OR_EQUAL = 52
    LSB = 53
    RSB = 54
    LB = 55
    RB = 56
    SM = 57
    DD = 58
    CM = 59
    CL = 60
    INTEGERLIT = 61
    FlOATLIT = 62
    BOOLEANLIT = 63
    STRINGLIT = 64
    WS = 65
    ERROR_CHAR = 66
    ILLEGAL_ESCAPE = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'int'", "'void'", "'{'", "'}'", "'+'", "'*'", "'not'", 
            "'or'", "'<>'", "'<'", "'<='", "'div'", "'-'", "'/'", "'mod'", 
            "'and'", "'='", "'>'", "'>='", "'['", "']'", "'('", "')'", "';'", 
            "'..'", "','", "':'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "ID", "INTLIT", "LP", "RP", "IDENTIFIERS", 
            "BREAK", "CONTINUE", "FOR", "TO", "DOWNTO", "DO", "IF", "THEN", 
            "ELSE", "RETURN", "WHILE", "BEGIN", "END", "FUNCTION", "PROCEDURE", 
            "VAR", "TRUE", "FALSE", "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", 
            "STRING", "NOT", "AND", "OR", "DIV", "MOD", "ADDITION", "MULTIPLICATION", 
            "LOGICAL_NOT", "LOGICAL_OR", "NOT_EQUAL", "LESS_THAN", "LESS_THAN_OR_EQUAL", 
            "INTEGER_DIVISION", "SUBSTACTION", "DIVISION", "MODULUS", "LOGICAL_AND", 
            "EQUAL", "GREATER_THAN", "GREATER_THAN_OR_EQUAL", "LSB", "RSB", 
            "LB", "RB", "SM", "DD", "CM", "CL", "INTEGERLIT", "FlOATLIT", 
            "BOOLEANLIT", "STRINGLIT", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "INTTYPE", "VOIDTYPE", "ID", "INTLIT", "LP", "RP", 
                  "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
                  "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
                  "W", "X", "Y", "Z", "LETTER_ID", "IDENTIFIERS", "BREAK", 
                  "CONTINUE", "FOR", "TO", "DOWNTO", "DO", "IF", "THEN", 
                  "ELSE", "RETURN", "WHILE", "BEGIN", "END", "FUNCTION", 
                  "PROCEDURE", "VAR", "TRUE", "FALSE", "ARRAY", "OF", "REAL", 
                  "BOOLEAN", "INTEGER", "STRING", "NOT", "AND", "OR", "DIV", 
                  "MOD", "ADDITION", "MULTIPLICATION", "LOGICAL_NOT", "LOGICAL_OR", 
                  "NOT_EQUAL", "LESS_THAN", "LESS_THAN_OR_EQUAL", "INTEGER_DIVISION", 
                  "SUBSTACTION", "DIVISION", "MODULUS", "LOGICAL_AND", "EQUAL", 
                  "GREATER_THAN", "GREATER_THAN_OR_EQUAL", "LSB", "RSB", 
                  "LB", "RB", "SM", "DD", "CM", "CL", "INTEGERLIT", "FlOATLIT", 
                  "BOOLEANLIT", "STRINGLIT", "WS", "ERROR_CHARACTER", "ERROR_CHAR", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


