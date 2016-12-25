class Rotor(object):

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self, name, wiring, notches, ring_position, start_position):
        """
        name: Arbitrary rotor name
        wiring: A string of 26 letters indicating the output mapping for letters A-Z in order
        notches: A string with at least 1 letter indicating when the next rotor should turn
        ring_position: The letter next to the rotor's dot
        start_position: The letter initially visible
        If any parameters are invalid an exception will be raised.
        """
        assert len(wiring) == 26 and len(set(wiring)) == 26
        self.name = name
        self.wiring = wiring
        self.ring = ''.join(c if c in notches else c.lower() for c in Rotor.alphabet)
        ring_offset = Rotor.alphabet.index(ring_position)
        self.tyre = Rotor.alphabet[ring_offset:] + Rotor.alphabet[:ring_offset]
        start_offset = self.tyre.index(start_position)
        self.rotate(start_offset)

        
    def rotate(self, n=1):
        ''' Rotates the rotor n notches '''
        def rotate_(s):
            return s[n:] + s[:n]
        
        self.tyre = rotate_(self.tyre)
        self.wiring = rotate_(self.wiring)
        self.ring = rotate_(self.ring)

        

    def process(self, c, rotate, debug=False):
        """
        Simulates the signal being received at the rotor input.
        c: The single character to process
        rotate: If True, the rotor should simulate rotation after processing this character
        returns: tuple(enciphered character, True if notch was present)
        """
        if c in Rotor.alphabet:
            if rotate: self.rotate()
            in_offset = Rotor.alphabet.index(c)
            out_offset = self.ring.upper().index(self.wiring[in_offset])
            if debug: self.print_state(in_offset, out_offset)
            return Rotor.alphabet[out_offset], self.ring[0].isupper()
        else:
            return c, False

    def reprocess(self, c, debug=False):
        """
        Simulates the signal being received at the rotor output.
        c: The single character to process
        returns: re-enciphered character
        """
        
        if c in Rotor.alphabet:
            in_offset = Rotor.alphabet.index(c)
            out_offset = self.wiring.index(self.ring[in_offset].upper())
            if debug: self.print_state(out_offset, in_offset)
            return Rotor.alphabet[out_offset]
        else:
            return c

    
    def print_state(self, in_offset, out_offset):
        print('         %sv' % (' ' * in_offset))
        print('Input:   %s'  % Rotor.alphabet)
        print('         %s|' % (' ' * in_offset))
        print('A. Tyre: %s'  % self.tyre)
        print('Wiring:  %s'  % self.wiring)
        print('Ring:    %s'  % self.ring)
        print('         %s|' % (' ' * out_offset))    
        print('Output:  %s'  % Rotor.alphabet)
        print('         %sv' % (' ' * out_offset))
                          


class Reflector(object):

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    def __init__(self, wiring, valid_positions="A", start_position="A", rotates=False):
        """
        wiring: A 26 character string mapping each pair of connections
        valid_positions: The valid starting positions
        start_position: The starting position
        rotates: If True this class will simulate rotations when process is called with rotate set True
        Raises an exception if the inputs are invalid
        """
        assert start_position in valid_positions
        assert len(wiring) == 26 and len(set(wiring)) == 26
        self.rotates = rotates
        self.contacts = Reflector.alphabet
        f = {wiring[i]:(wiring[i+1] if i % 2 == 0 else wiring[i - 1]) for i in xrange(26)}
        self.wiring = ''.join(f[c] for c in Reflector.alphabet)
        offset = self.contacts.index(start_position)
        self.rotate(offset)
        
    def rotate(self, n=1):
        ''' Rotates the rotor n notches '''
        def rotate_(s):
            return s[n:] + s[:n]
        
        self.contacts = rotate_(self.contacts)
        self.wiring = rotate_(self.wiring)




    def process(self, c, rotate, debug=False):
        """
        c: Character to process
        rotate: Simulates rotation if True and the instance supports rotation
        """
        if not c in Reflector.alphabet: return c
        if rotate and self.rotates: self.rotate()
        in_offset = Reflector.alphabet.index(c)
        out_offset = self.contacts.index(self.wiring[in_offset])
        if debug: self.print_state(in_offset, out_offset)
        return Reflector.alphabet[out_offset]

    def print_state(self, in_offset, out_offset):
        if in_offset < out_offset:
            print('          %sv%s^' % (' ' * in_offset, ' ' * (out_offset - in_offset - 1)))
            print('In/Out:   %s'  % Reflector.alphabet)
            print('          %s|%s|' % (' ' * in_offset, ' ' * (out_offset - in_offset - 1)))
        else:
            print('          %s^%sv' % (' ' * out_offset, ' ' * (in_offset - out_offset - 1)))
            print('In/Out:   %s'  % Reflector.alphabet)
            print('          %s|%s|' % (' ' * out_offset, ' ' * (in_offset - out_offset - 1)))
        print('Contacts: %s'  % self.contacts)
        print('Wiring:   %s'  % self.wiring)                  


        
def knapsack(capacity, items):
    items, ks = list(enumerate(items)), [0] * len(items)
    items.sort(key=lambda (i, (s, v)): float(v) / s, reverse=True)
    for j in xrange(len(items)):
        if capacity <= 0: break
        i, (size, value) = items[j]
        q, capacity = divmod(capacity, size)
        ks[i] = q
    return ks
