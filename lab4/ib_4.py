class Rotor:
    def __init__(self, wiring, step):
        self.wiring = wiring
        self.step = step
        self.position = 0

    def rotate(self):
        self.position = (self.position + 1) % len(self.wiring)

    def encode_forward(self, char):
        offset = (ord(char) - ord('A') + self.position) % 26
        return self.wiring[offset]

    def encode_backward(self, char):
        offset = (self.wiring.index(char) - self.position) % 26
        return chr(offset + ord('A'))


class Reflector:
    def __init__(self, wiring):
        self.wiring = wiring

    def reflect(self, char):
        return self.wiring[ord(char) - ord('A')]


class EnigmaMachine:
    def __init__(self, rotors, reflector):
        self.rotors = rotors
        self.reflector = reflector

    def encode_letter(self, letter):
        for rotor in self.rotors[::-1]:
            letter = rotor.encode_forward(letter)
        letter = self.reflector.reflect(letter)
        for rotor in self.rotors:
            letter = rotor.encode_backward(letter)
        self.rotate_rotors()
        return letter

    def rotate_rotors(self):
        self.rotors[0].rotate()
        for i in range(len(self.rotors) - 1):
            if self.rotors[i].position == self.rotors[i].step:
                self.rotors[i].rotate()
                self.rotors[i + 1].rotate()


def main():
    rotor_wirings = [
        "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
        "AJDKSIRUXBLHWTMCQGZNPYFVOE",
        "BDFHJLCPRTXVZNYEIWGAKMUSQO"
    ]
    rotor_steps = [17, 5, 22]  # Example steps, you may adjust as needed
    reflector_wiring = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

    rotors = [Rotor(wiring, step) for wiring, step in zip(rotor_wirings, rotor_steps)]
    reflector = Reflector(reflector_wiring)

    enigma_machine = EnigmaMachine(rotors, reflector)

    message = "HELLO"
    encoded_message = ""
    for char in message:
        encoded_message += enigma_machine.encode_letter(char)
    print("Encoded message:", encoded_message)

    decoded_message = ""
    for char in encoded_message:
        decoded_message += enigma_machine.encode_letter(char)
    print("Decoded message:", decoded_message)


if __name__ == "__main__":
    main()
