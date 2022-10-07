from PIL import Image


class Revelar:
    def __init__(self, senha, origem):
        self.mensagem = ""
        self._senha = senha
        self._im = Image.open(origem)
        self._shlen = len(senha)
        self._w = self._im.size[0]
        self._h = self._im.size[1]
        self._data = self._im.convert('RGB')
        self._chshbin = ""  # definido quando a função_criaSenhaBinaria é chamada
        self._tamanho = ""  # definido quando a função_revelaTamanho é chamada

    def _criasenhabinaria(self):
        for c in bytearray(self._senha, "utf-8"):
            result = format(c, 'b')
            while len(result) < 8:
                result = "0" + result
            self._chshbin = self._chshbin + result

    def _revelatamanho(self):
        tamanhodamensage = ""
        for j in range(self._w):
            if self._data.getpixel((j, 0))[2] % 2 == 0:
                tamanhodamensage = tamanhodamensage + "0"
            else:
                tamanhodamensage = tamanhodamensage + "1"
        self._tamanho = 8 * int(tamanhodamensage, 2)

    def _revelamensagem(self):
        mcont = 0
        scont = 0
        mensagembinaria = ""
        self.mensagem = ""
        for i in range(1, self._h):
            if mcont == self._tamanho:
                break
            else:
                for j in range(self._w):
                    if mcont == self._tamanho:
                        break
                    else:
                        if not (self._chshbin[scont] == "0"):
                            if self._data.getpixel((j, i))[2] % 2 == 0:
                                mensagembinaria = mensagembinaria + "0"
                            else:
                                mensagembinaria = mensagembinaria + "1"
                            mcont += 1
                        if scont == 8 * self._shlen - 1:
                            scont = 0
                        else:
                            scont += 1
        # Converter a msg para caractere
        for i in range(0, len(mensagembinaria), 8):
            self.mensagem = self.mensagem + chr(int(mensagembinaria[i:i + 8], 2))

    def run(self):
        self._criasenhabinaria()
        self._revelatamanho()
        self._revelamensagem()
        return self.mensagem

