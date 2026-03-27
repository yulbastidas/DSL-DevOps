# Generated from DevOpsDSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .DevOpsDSLParser import DevOpsDSLParser
else:
    from DevOpsDSLParser import DevOpsDSLParser

# This class defines a complete generic visitor for a parse tree produced by DevOpsDSLParser.

class DevOpsDSLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DevOpsDSLParser#program.
    def visitProgram(self, ctx:DevOpsDSLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DevOpsDSLParser#statement.
    def visitStatement(self, ctx:DevOpsDSLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DevOpsDSLParser#nodeCommand.
    def visitNodeCommand(self, ctx:DevOpsDSLParser.NodeCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DevOpsDSLParser#groupCommand.
    def visitGroupCommand(self, ctx:DevOpsDSLParser.GroupCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DevOpsDSLParser#deployCommand.
    def visitDeployCommand(self, ctx:DevOpsDSLParser.DeployCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DevOpsDSLParser#parallelBlock.
    def visitParallelBlock(self, ctx:DevOpsDSLParser.ParallelBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DevOpsDSLParser#statusCommand.
    def visitStatusCommand(self, ctx:DevOpsDSLParser.StatusCommandContext):
        return self.visitChildren(ctx)



del DevOpsDSLParser