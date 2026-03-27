# Generated from grammar/DevOpsDSL.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,54,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,5,
        0,14,8,0,10,0,12,0,17,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,25,8,1,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,
        1,4,1,5,1,5,1,5,4,5,48,8,5,11,5,12,5,49,1,5,1,5,1,5,0,0,6,0,2,4,
        6,8,10,0,0,52,0,15,1,0,0,0,2,24,1,0,0,0,4,26,1,0,0,0,6,33,1,0,0,
        0,8,39,1,0,0,0,10,44,1,0,0,0,12,14,3,2,1,0,13,12,1,0,0,0,14,17,1,
        0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,18,1,0,0,0,17,15,1,0,0,0,18,
        19,5,0,0,1,19,1,1,0,0,0,20,25,3,4,2,0,21,25,3,6,3,0,22,25,3,8,4,
        0,23,25,3,10,5,0,24,20,1,0,0,0,24,21,1,0,0,0,24,22,1,0,0,0,24,23,
        1,0,0,0,25,3,1,0,0,0,26,27,5,11,0,0,27,28,5,1,0,0,28,29,5,2,0,0,
        29,30,5,3,0,0,30,31,5,12,0,0,31,32,5,4,0,0,32,5,1,0,0,0,33,34,5,
        11,0,0,34,35,5,1,0,0,35,36,5,5,0,0,36,37,5,3,0,0,37,38,5,4,0,0,38,
        7,1,0,0,0,39,40,5,6,0,0,40,41,5,11,0,0,41,42,5,7,0,0,42,43,5,11,
        0,0,43,9,1,0,0,0,44,45,5,8,0,0,45,47,5,9,0,0,46,48,3,2,1,0,47,46,
        1,0,0,0,48,49,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,51,1,0,0,0,
        51,52,5,10,0,0,52,11,1,0,0,0,3,15,24,49
    ]

class DevOpsDSLParser ( Parser ):

    grammarFileName = "DevOpsDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "'run'", "'('", "')'", "'update'", 
                     "'deploy'", "'to'", "'parallel'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "STRING", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_nodeCommand = 2
    RULE_groupCommand = 3
    RULE_deployCommand = 4
    RULE_parallelBlock = 5

    ruleNames =  [ "program", "statement", "nodeCommand", "groupCommand", 
                   "deployCommand", "parallelBlock" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    ID=11
    STRING=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(DevOpsDSLParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DevOpsDSLParser.StatementContext)
            else:
                return self.getTypedRuleContext(DevOpsDSLParser.StatementContext,i)


        def getRuleIndex(self):
            return DevOpsDSLParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = DevOpsDSLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2368) != 0):
                self.state = 12
                self.statement()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 18
            self.match(DevOpsDSLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nodeCommand(self):
            return self.getTypedRuleContext(DevOpsDSLParser.NodeCommandContext,0)


        def groupCommand(self):
            return self.getTypedRuleContext(DevOpsDSLParser.GroupCommandContext,0)


        def deployCommand(self):
            return self.getTypedRuleContext(DevOpsDSLParser.DeployCommandContext,0)


        def parallelBlock(self):
            return self.getTypedRuleContext(DevOpsDSLParser.ParallelBlockContext,0)


        def getRuleIndex(self):
            return DevOpsDSLParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = DevOpsDSLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 24
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.nodeCommand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.groupCommand()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                self.deployCommand()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 23
                self.parallelBlock()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NodeCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DevOpsDSLParser.ID, 0)

        def STRING(self):
            return self.getToken(DevOpsDSLParser.STRING, 0)

        def getRuleIndex(self):
            return DevOpsDSLParser.RULE_nodeCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNodeCommand" ):
                listener.enterNodeCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNodeCommand" ):
                listener.exitNodeCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNodeCommand" ):
                return visitor.visitNodeCommand(self)
            else:
                return visitor.visitChildren(self)




    def nodeCommand(self):

        localctx = DevOpsDSLParser.NodeCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_nodeCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(DevOpsDSLParser.ID)
            self.state = 27
            self.match(DevOpsDSLParser.T__0)
            self.state = 28
            self.match(DevOpsDSLParser.T__1)
            self.state = 29
            self.match(DevOpsDSLParser.T__2)
            self.state = 30
            self.match(DevOpsDSLParser.STRING)
            self.state = 31
            self.match(DevOpsDSLParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GroupCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DevOpsDSLParser.ID, 0)

        def getRuleIndex(self):
            return DevOpsDSLParser.RULE_groupCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroupCommand" ):
                listener.enterGroupCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroupCommand" ):
                listener.exitGroupCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGroupCommand" ):
                return visitor.visitGroupCommand(self)
            else:
                return visitor.visitChildren(self)




    def groupCommand(self):

        localctx = DevOpsDSLParser.GroupCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_groupCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(DevOpsDSLParser.ID)
            self.state = 34
            self.match(DevOpsDSLParser.T__0)
            self.state = 35
            self.match(DevOpsDSLParser.T__4)
            self.state = 36
            self.match(DevOpsDSLParser.T__2)
            self.state = 37
            self.match(DevOpsDSLParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeployCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(DevOpsDSLParser.ID)
            else:
                return self.getToken(DevOpsDSLParser.ID, i)

        def getRuleIndex(self):
            return DevOpsDSLParser.RULE_deployCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeployCommand" ):
                listener.enterDeployCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeployCommand" ):
                listener.exitDeployCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeployCommand" ):
                return visitor.visitDeployCommand(self)
            else:
                return visitor.visitChildren(self)




    def deployCommand(self):

        localctx = DevOpsDSLParser.DeployCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_deployCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(DevOpsDSLParser.T__5)
            self.state = 40
            self.match(DevOpsDSLParser.ID)
            self.state = 41
            self.match(DevOpsDSLParser.T__6)
            self.state = 42
            self.match(DevOpsDSLParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParallelBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DevOpsDSLParser.StatementContext)
            else:
                return self.getTypedRuleContext(DevOpsDSLParser.StatementContext,i)


        def getRuleIndex(self):
            return DevOpsDSLParser.RULE_parallelBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParallelBlock" ):
                listener.enterParallelBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParallelBlock" ):
                listener.exitParallelBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParallelBlock" ):
                return visitor.visitParallelBlock(self)
            else:
                return visitor.visitChildren(self)




    def parallelBlock(self):

        localctx = DevOpsDSLParser.ParallelBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_parallelBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(DevOpsDSLParser.T__7)
            self.state = 45
            self.match(DevOpsDSLParser.T__8)
            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46
                self.statement()
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2368) != 0)):
                    break

            self.state = 51
            self.match(DevOpsDSLParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





