# Generated from DevOpsDSL.g4 by ANTLR 4.13.2
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
        4,1,14,63,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,
        1,28,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,
        1,4,1,4,1,4,1,4,1,5,1,5,1,5,4,5,51,8,5,11,5,12,5,52,1,5,1,5,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,0,0,61,0,17,1,0,0,
        0,2,27,1,0,0,0,4,29,1,0,0,0,6,36,1,0,0,0,8,42,1,0,0,0,10,47,1,0,
        0,0,12,56,1,0,0,0,14,16,3,2,1,0,15,14,1,0,0,0,16,19,1,0,0,0,17,15,
        1,0,0,0,17,18,1,0,0,0,18,20,1,0,0,0,19,17,1,0,0,0,20,21,5,0,0,1,
        21,1,1,0,0,0,22,28,3,4,2,0,23,28,3,6,3,0,24,28,3,8,4,0,25,28,3,10,
        5,0,26,28,3,12,6,0,27,22,1,0,0,0,27,23,1,0,0,0,27,24,1,0,0,0,27,
        25,1,0,0,0,27,26,1,0,0,0,28,3,1,0,0,0,29,30,5,12,0,0,30,31,5,1,0,
        0,31,32,5,2,0,0,32,33,5,3,0,0,33,34,5,13,0,0,34,35,5,4,0,0,35,5,
        1,0,0,0,36,37,5,12,0,0,37,38,5,1,0,0,38,39,5,5,0,0,39,40,5,3,0,0,
        40,41,5,4,0,0,41,7,1,0,0,0,42,43,5,6,0,0,43,44,5,12,0,0,44,45,5,
        7,0,0,45,46,5,12,0,0,46,9,1,0,0,0,47,48,5,8,0,0,48,50,5,9,0,0,49,
        51,3,2,1,0,50,49,1,0,0,0,51,52,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,
        0,53,54,1,0,0,0,54,55,5,10,0,0,55,11,1,0,0,0,56,57,5,12,0,0,57,58,
        5,1,0,0,58,59,5,11,0,0,59,60,5,3,0,0,60,61,5,4,0,0,61,13,1,0,0,0,
        3,17,27,52
    ]

class DevOpsDSLParser ( Parser ):

    grammarFileName = "DevOpsDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "'run'", "'('", "')'", "'update'", 
                     "'deploy'", "'to'", "'parallel'", "'{'", "'}'", "'status'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "STRING", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_nodeCommand = 2
    RULE_groupCommand = 3
    RULE_deployCommand = 4
    RULE_parallelBlock = 5
    RULE_statusCommand = 6

    ruleNames =  [ "program", "statement", "nodeCommand", "groupCommand", 
                   "deployCommand", "parallelBlock", "statusCommand" ]

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
    T__10=11
    ID=12
    STRING=13
    WS=14

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
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4416) != 0):
                self.state = 14
                self.statement()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
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


        def statusCommand(self):
            return self.getTypedRuleContext(DevOpsDSLParser.StatusCommandContext,0)


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
            self.state = 27
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.nodeCommand()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.groupCommand()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 24
                self.deployCommand()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 25
                self.parallelBlock()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 26
                self.statusCommand()
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
            self.state = 29
            self.match(DevOpsDSLParser.ID)
            self.state = 30
            self.match(DevOpsDSLParser.T__0)
            self.state = 31
            self.match(DevOpsDSLParser.T__1)
            self.state = 32
            self.match(DevOpsDSLParser.T__2)
            self.state = 33
            self.match(DevOpsDSLParser.STRING)
            self.state = 34
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
            self.state = 36
            self.match(DevOpsDSLParser.ID)
            self.state = 37
            self.match(DevOpsDSLParser.T__0)
            self.state = 38
            self.match(DevOpsDSLParser.T__4)
            self.state = 39
            self.match(DevOpsDSLParser.T__2)
            self.state = 40
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
            self.state = 42
            self.match(DevOpsDSLParser.T__5)
            self.state = 43
            self.match(DevOpsDSLParser.ID)
            self.state = 44
            self.match(DevOpsDSLParser.T__6)
            self.state = 45
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
            self.state = 47
            self.match(DevOpsDSLParser.T__7)
            self.state = 48
            self.match(DevOpsDSLParser.T__8)
            self.state = 50 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 49
                self.statement()
                self.state = 52 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4416) != 0)):
                    break

            self.state = 54
            self.match(DevOpsDSLParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatusCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DevOpsDSLParser.ID, 0)

        def getRuleIndex(self):
            return DevOpsDSLParser.RULE_statusCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatusCommand" ):
                listener.enterStatusCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatusCommand" ):
                listener.exitStatusCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatusCommand" ):
                return visitor.visitStatusCommand(self)
            else:
                return visitor.visitChildren(self)




    def statusCommand(self):

        localctx = DevOpsDSLParser.StatusCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_statusCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(DevOpsDSLParser.ID)
            self.state = 57
            self.match(DevOpsDSLParser.T__0)
            self.state = 58
            self.match(DevOpsDSLParser.T__10)
            self.state = 59
            self.match(DevOpsDSLParser.T__2)
            self.state = 60
            self.match(DevOpsDSLParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





