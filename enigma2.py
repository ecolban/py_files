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

        ring_offset = (ord('A') - ord(ring_position)) % 26
        self.tyre = Rotor.alphabet
        self.wiring = rotate(wiring, ring_offset)
        self.ring = rotate(''.join(c if c in notches else c.lower() for c in Rotor.alphabet), ring_offset)        start_offset = ord(start_position) - ord('A')
        
        self.rotate(ord(start_position) - ord('A'))

        
     def rotate(self, n):
        def rotate_(s):
            return ''.join(s[(i + n) % len(s)] for i in xrange(len(s)))
        
        rotate_(self.tyre)
        rotate_(self.wiring)
        rotate_(self.ring)

        

    def process(self, c, rotate):
        """
        Simulates the signal being received at the rotor input.
        c: The single character to process
        rotate: If True, the rotor should simulate rotation after processing this character
        returns: tuple(enciphered character, True if notch was present)
        """
        if c in Rotor.alphabet:
            if rotate: self.rotate(1)
            in_idx = Rotor.alphabet.index(c)
            out_idx = self.ring.upper().index(self.wiring[in_idx])
            return Rotor.alphabet[out_idx], ring[0].isupper()
        else:
            return c, self._pos in self._notch_pos

    
    def print_state(in_char):
        in_offset = ord(in_char) - ord('A')
        print('         ' + ' ' * in_offset + 'v')
        print('Input:   %s' % Rotor.alphabet)
        print('         ' + ' ' * in_offset + '|')
        print('A. Tyre: %s' % self.tyre)
        print('Wiring:  %s' % self.wiring)
        print('Ring:    %s' % self.ring)
        out_offset = ring.upper().index(wiring[in_offset])
        print('         ' + ' ' * out_offset + '|')    
        print('Output:  %s' % Rotor.alphabet)
        print('         ' + ' ' * out_offset + 'v')
                          


