digit_to_binary = { # my numbers are 32 bit long 
    '0':'00000000000000000000000000000000', 
    '1':'00000000000000000000000000000001', 
    '2':'00000000000000000000000000000010', 
    '3':'00000000000000000000000000000011', 
    '4':'00000000000000000000000000000100', 
    '5':'00000000000000000000000000000101', 
    '6':'00000000000000000000000000000110', 
    '7':'00000000000000000000000000000111', 
    '8':'00000000000000000000000000001000', 
    '9':'00000000000000000000000000001001'}

binary_to_digit = {b:d for d, b in digit_to_binary.items()}

zero = digit_to_binary['0']
one = digit_to_binary['1']
ten = '00000000000000000000000000001010'

def add(s1, s2):
    s = zip(s1, s2)
    result = ''
    carry = '0'
    for x in reversed(s):
        if x == ('0', '0'):
            result = carry + result
            carry = '0'
        elif x == ('1', '1'):
            result = carry + result
            carry = '1'
        elif carry == '1':
            result = '0' + result
        else:
            result = '1' + result
    return result



def left_shift(s):
    #return s[1:] + '0'
    return add(s, s)

def right_shift(s):
    #return '0' + s[:-1]
    r = zip('0' + s, zero)
    a, _ = zip(*r)
    return ''.join(a)

def negate(s):
    result = ''.join('1' if c == '0' else '0' for c in s)
    return add(result, one)

def is_negative(s):
    return next(iter(s)) == '1'

def subtract(s1, s2):
    return add(s1, negate(s2))

def gt(s1, s2):
    return is_negative(subtract(s2, s1))

def ge(s1, s2):
    return s1 == s2 or gt(s1, s2)

def multiply(s1, s2):
    b = one
    result = zero
    while ge(s1, b):
        b = left_shift(b)
    while gt(b, one):
        b = right_shift(b)
        result = left_shift(result)
        if ge(s1, b):
            s1 = subtract(s1, b)
            result = add(result, s2)
    return result

def divide(s1, s2):
    b = one
    q, r = zero, zero
    while ge(s1, b):
        b = left_shift(b)
    while gt(b, one):
        b = right_shift(b)
        q, r = left_shift(q), left_shift(r)
        if ge(s1, b):
            s1 = subtract(s1, b)
            r = add(r, one)
        if ge(r, s2):
            r = subtract(r, s2)
            q = add(q, one)
    return (q, r)

def dec_to_bin(s):
     result = zero
     for d in s:
         result = multiply(ten, result)
         result = add(result, digit_to_binary[d])
     return result

def bin_to_dec(s):
    if s == zero: return '0'
    result = ""
    while gt(s, zero):
        s, r = divide(s, ten)
        result = binary_to_digit[r] + result
    return result

def multiplyMyNumbers(n1, n2):
    return bin_to_dec(multiply(*map(dec_to_bin, (n1, n2))))

def divideMyNumbers(n1, n2):
    return map(bin_to_dec, divide(*map(dec_to_bin, (n1, n2))))


    

                  
    
    


        


    
    
                
    
