'''
https://www.codewars.com/kata/577f57d7e555335c0d0003a9/edit/python

Imagine you run a business selling some products. Every evening, you run a program that generates a report on the day's sales.
The products are grouped into product groups and the report tells you the day's revenue for each group. The program takes as
input a sequence of tuples `(product_id, group_id, value)`, where  `value` is the amount sold for each of the given products.
The input is subject to the following constraints:

1. Each product has a unique `product_id` consisting of a string of four digits.
2. Each product belongs to a unique group.
3. Each group has a unique `group_id` consisting of a string of three digits.
4. The input may contain multiple tuples with the same `product_id`.
5. The input is sorted by `group_id` and then by `product_id`
6. The value is given as a non-negative integer.
7. The type of the input is unknown other than that it is  _iterable_.

The output of the program is a string that follows format of the following example:
```
Group: 001
    Product: 0001 Value:     12
    Product: 0012 Value:   1032
    Group total:                  1044

Group: 007                
    Product: 0027 Value:    207
    Product: 0112 Value:  12119
    Product: 1009 Value:    200
    Group total:                 12326

Total:                           13370
```    
Do not use tabs in the output, but make sure to insert the correct amount of spaces. The values (including the totals) may
have up to six digits and a single space separates each column.

Write a function `generate_report(input)` that generates the report for given input `input`.
'''

from itertools import groupby
def generate_report(records):
    output, total = [], 0
    for group_id, group in groupby(records , key=lambda r: r[1]):
        group_total = 0
        output.append('Group: %s' % group_id)
        for prod_id, prods in groupby(group, key=lambda r: r[0]):
            prod_total = sum(t[2] for t in prods)
            group_total += prod_total
            output.append('    Product: %s Value: %6d' % (prod_id, prod_total))
        total += group_total
        output.append('    Group total:                %6d\n' % group_total)
    output.append('Total:                          %6d' % total)
    return '\n'.join(output)

records = [('0001', '001', 12), ('0012', '001', 1000), ('0012', '001', 32), ('0027', '007', 207), ('0112', '007', 12119), ('1009', '007', 200)]

res = generate_report(records)


groups = ['%03d' % randrange(1, 1000) for _ in xrange(20)]
prods = {'%04d' % randrange(1, 10000) for _ in xrange(50)}
grouping = [(choice(groups),p) for p in prods]

records = ((p, g, v) for ((g, p), v) in sorted((choice(grouping), randrange(1, 10000)) for _ in xrange(20)))

print(generate_report(records))
                      
        




    
