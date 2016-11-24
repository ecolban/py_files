from collections import Counter

def count_and_print_graph(text, max_units_on_screen):
    count = Counter(c for c in text.lower() if c.isalpha())
    c_max = count.most_common(1)[0][1]
    for c in count:
        print('%s:%s' % (c, '#'*(count[c] * max_units_on_screen // c_max)))
