import re

class Compiler(object):
    
    operators = {
            '-': int.__sub__,
            '+': int.__add__,
            '*': int.__mul__,
            '/': int.__div__
          }
    precedence = {'*':1, '/':1, '+':2, '-':2, '(':3}

    def __init__(self):
        pass

    
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
        stack = []
        op_stack = []
        pos = 0
        assert tokens[pos] == '['
        pos += 1
        vs = []
        while tokens[pos] != ']':
            vs.append(tokens[pos])
            pos += 1
        self.vars = {v:n for n, v in enumerate(vs)}
        pos += 1

        while pos < len(tokens):
##            print('stack = %s, op_stack = %s' % (stack, op_stack))
            token = tokens[pos]
            pos += 1
            if type(token) == int:
                stack.append({'op': 'imm', 'n': token})
            elif token in self.vars:
                stack.append({'op': 'arg', 'n': self.vars[token]})
            elif token in Compiler.operators:
                while op_stack and Compiler.precedence[op_stack[-1]] <= Compiler.precedence[token]:
                    op = op_stack.pop()
                    b = stack.pop()
                    a = stack.pop()
                    stack.append({'op':op, 'a':a, 'b':b})
                op_stack.append(token)
            elif token == '(':
                op_stack.append(token)
            elif token == ')':
                op = op_stack.pop()
                while op != '(':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append({'op':op, 'a':a, 'b':b})
                    op = op_stack.pop()
            
        while op_stack:
            op = op_stack.pop()
            b = stack.pop()
            a = stack.pop()
            stack.append({'op':op, 'a':a, 'b':b})
        
        return stack.pop()
            
            
        
                 
        
        
    def pass2(self, ast):
        """Returns an AST with constant expressions reduced"""
        if ast['op'] == 'arg' or ast['op'] == 'imm':
            return ast
        else:
            op = ast['op']
            a = self.pass2(ast['a'])
            b = self.pass2(ast['b'])
            if a['op'] == 'imm' and b['op'] == 'imm':
                return {'op' : 'imm', 'n': Compiler.operators[op](a['n'], b['n'])}
            else:
                return {'op':op, 'a':a, 'b':b}

    def pass3(self, ast):
        """Returns assembly instructions"""
        pass
