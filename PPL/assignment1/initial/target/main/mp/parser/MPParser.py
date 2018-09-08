# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3E")
        buf.write("%\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\5\3\5\5\5\34")
        buf.write("\n\5\3\6\3\6\3\6\5\6!\n\6\3\6\3\6\3\6\2\2\7\2\4\6\b\n")
        buf.write("\2\3\3\2\4\5\2!\2\f\3\2\2\2\4\24\3\2\2\2\6\26\3\2\2\2")
        buf.write("\b\33\3\2\2\2\n\35\3\2\2\2\f\r\5\4\3\2\r\16\7\3\2\2\16")
        buf.write("\17\79\2\2\17\20\7:\2\2\20\21\7\b\2\2\21\22\7\t\2\2\22")
        buf.write("\23\7\2\2\3\23\3\3\2\2\2\24\25\t\2\2\2\25\5\3\2\2\2\26")
        buf.write("\27\5\n\6\2\27\30\7;\2\2\30\7\3\2\2\2\31\34\5\n\6\2\32")
        buf.write("\34\7\7\2\2\33\31\3\2\2\2\33\32\3\2\2\2\34\t\3\2\2\2\35")
        buf.write("\36\7\6\2\2\36 \79\2\2\37!\5\b\5\2 \37\3\2\2\2 !\3\2\2")
        buf.write("\2!\"\3\2\2\2\"#\7:\2\2#\13\3\2\2\2\4\33 ")
        return buf.getvalue()


class MPParser ( Parser ):

    grammarFileName = "MP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'int'", "'void'", "<INVALID>", 
                     "<INVALID>", "'{'", "'}'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'+'", "'*'", "'not'", "'or'", "'<>'", "'<'", "'<='", 
                     "'div'", "'-'", "'/'", "'mod'", "'and'", "'='", "'>'", 
                     "'>='", "'['", "']'", "'('", "')'", "';'", "'..'", 
                     "','", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "INTTYPE", "VOIDTYPE", "ID", 
                      "INTLIT", "LP", "RP", "IDENTIFIERS", "BREAK", "CONTINUE", 
                      "FOR", "TO", "DOWNTO", "DO", "IF", "THEN", "ELSE", 
                      "RETURN", "WHILE", "BEGIN", "END", "FUNCTION", "PROCEDURE", 
                      "VAR", "TRUE", "FALSE", "ARRAY", "OF", "REAL", "BOOLEAN", 
                      "INTEGER", "STRING", "NOT", "AND", "OR", "DIV", "MOD", 
                      "ADDITION", "MULTIPLICATION", "LOGICAL_NOT", "LOGICAL_OR", 
                      "NOT_EQUAL", "LESS_THAN", "LESS_THAN_OR_EQUAL", "INTEGER_DIVISION", 
                      "SUBSTACTION", "DIVISION", "MODULUS", "LOGICAL_AND", 
                      "EQUAL", "GREATER_THAN", "GREATER_THAN_OR_EQUAL", 
                      "LSB", "RSB", "LB", "RB", "SM", "DD", "CM", "CL", 
                      "INTEGERLIT", "FlOATLIT", "BOOLEANLIT", "STRINGLIT", 
                      "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_mptype = 1
    RULE_body = 2
    RULE_exp = 3
    RULE_funcall = 4

    ruleNames =  [ "program", "mptype", "body", "exp", "funcall" ]

    EOF = Token.EOF
    T__0=1
    INTTYPE=2
    VOIDTYPE=3
    ID=4
    INTLIT=5
    LP=6
    RP=7
    IDENTIFIERS=8
    BREAK=9
    CONTINUE=10
    FOR=11
    TO=12
    DOWNTO=13
    DO=14
    IF=15
    THEN=16
    ELSE=17
    RETURN=18
    WHILE=19
    BEGIN=20
    END=21
    FUNCTION=22
    PROCEDURE=23
    VAR=24
    TRUE=25
    FALSE=26
    ARRAY=27
    OF=28
    REAL=29
    BOOLEAN=30
    INTEGER=31
    STRING=32
    NOT=33
    AND=34
    OR=35
    DIV=36
    MOD=37
    ADDITION=38
    MULTIPLICATION=39
    LOGICAL_NOT=40
    LOGICAL_OR=41
    NOT_EQUAL=42
    LESS_THAN=43
    LESS_THAN_OR_EQUAL=44
    INTEGER_DIVISION=45
    SUBSTACTION=46
    DIVISION=47
    MODULUS=48
    LOGICAL_AND=49
    EQUAL=50
    GREATER_THAN=51
    GREATER_THAN_OR_EQUAL=52
    LSB=53
    RSB=54
    LB=55
    RB=56
    SM=57
    DD=58
    CM=59
    CL=60
    INTEGERLIT=61
    FlOATLIT=62
    BOOLEANLIT=63
    STRINGLIT=64
    WS=65
    ERROR_CHAR=66
    ILLEGAL_ESCAPE=67

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mptype(self):
            return self.getTypedRuleContext(MPParser.MptypeContext,0)


        def LB(self):
            return self.getToken(MPParser.LB, 0)

        def RB(self):
            return self.getToken(MPParser.RB, 0)

        def LP(self):
            return self.getToken(MPParser.LP, 0)

        def RP(self):
            return self.getToken(MPParser.RP, 0)

        def EOF(self):
            return self.getToken(MPParser.EOF, 0)

        def getRuleIndex(self):
            return MPParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MPParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.mptype()
            self.state = 11
            self.match(MPParser.T__0)
            self.state = 12
            self.match(MPParser.LB)
            self.state = 13
            self.match(MPParser.RB)
            self.state = 14
            self.match(MPParser.LP)
            self.state = 15
            self.match(MPParser.RP)
            self.state = 16
            self.match(MPParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MptypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(MPParser.INTTYPE, 0)

        def VOIDTYPE(self):
            return self.getToken(MPParser.VOIDTYPE, 0)

        def getRuleIndex(self):
            return MPParser.RULE_mptype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMptype" ):
                return visitor.visitMptype(self)
            else:
                return visitor.visitChildren(self)




    def mptype(self):

        localctx = MPParser.MptypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mptype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            _la = self._input.LA(1)
            if not(_la==MPParser.INTTYPE or _la==MPParser.VOIDTYPE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(MPParser.FuncallContext,0)


        def SM(self):
            return self.getToken(MPParser.SM, 0)

        def getRuleIndex(self):
            return MPParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = MPParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.funcall()
            self.state = 21
            self.match(MPParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(MPParser.FuncallContext,0)


        def INTLIT(self):
            return self.getToken(MPParser.INTLIT, 0)

        def getRuleIndex(self):
            return MPParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = MPParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_exp)
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MPParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.funcall()
                pass
            elif token in [MPParser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.match(MPParser.INTLIT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MPParser.ID, 0)

        def LB(self):
            return self.getToken(MPParser.LB, 0)

        def RB(self):
            return self.getToken(MPParser.RB, 0)

        def exp(self):
            return self.getTypedRuleContext(MPParser.ExpContext,0)


        def getRuleIndex(self):
            return MPParser.RULE_funcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncall" ):
                return visitor.visitFuncall(self)
            else:
                return visitor.visitChildren(self)




    def funcall(self):

        localctx = MPParser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(MPParser.ID)
            self.state = 28
            self.match(MPParser.LB)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MPParser.ID or _la==MPParser.INTLIT:
                self.state = 29
                self.exp()


            self.state = 32
            self.match(MPParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





