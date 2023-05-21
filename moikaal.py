import random

class Cislovka:
    def __init__(self, nomer):
        self._nomer = nomer
        self._result = None

    def _encode(self):
        self._result = self._nomer * random.randint(1, 10)

    def get_result(self):
        self._encode()
        return self._result

class Deshifrator(Cislovka):
    def __init__(self, number):
        super().__init__(number)

    def _decode(self):
        self._result = self._nomer // random.randint(1, 10)
        # S ODNOU / POLUCHAETSA KASHA

    def get_result(self):
        self._decode()
        return self._result

# я забил на str ну и ладно)
encoder = Cislovka(5)
encoded_result = encoder.get_result()
print(encoded_result)

decoder = Deshifrator(50)
decoded_result = decoder.get_result()
print(decoded_result)
