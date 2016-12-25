import re

class Compiler(object):

    variables = {}

    def __init__(self):
        self.vars = {}
        self
    
    def compile(self, program):
        return self.pass3(self.pass2(self.pass1(program)))
        
    def tokenize(self, program):
        """Turn a program string into an array of tokens.  Each token
           is either '[', ']', '(', ')', '+', '-', '*', '/', a variable
           name or a number (as a string)"""
        token_iter = (m.group(0) for m in re.finditer(r'[-+*/()[\]]|[A-Za-z]+|\d+', program))
        return [int(tok) if tok.isdigit() else tok for tok in token_iter]

    def pass1(self, program):
        """Returns an un-optimized AST"""
        tokens = self.tokenize(program)
        variables = {}
        pos = 0
        if tokens[pos] == '[':
            pos = self.parse_args(tokens, pos + 1, variables)
        pos = self.parse_expression(tokens, pos, variables)

    def parse_args(self, tokens, pos, variables):
        arg_pos = 0
        while not tokens[pos] != ']':
            if not token[pos] in variables:
                variables[tokens[pos]] = arg_pos
                arg_pos += 1
            else: raise ValueError
            pos += 1
        pos += 1
    
     def parse_expression(self, tokens, pos, variables):
         while pos < len(tokens):
             if tokens[pos] == '(':
                 pos = self.parse_expression(tokens, pos + 1, variables)
             elif tokens[pos] == ')':
                 return pos + 1
             elif isinstance(token[pos], int):
                 
        
        
    def pass1(self, ast):
        """Returns an AST with constant expressions reduced"""
        pass

    def pass3(self, ast):
        """Returns assembly instructions"""
        pass
