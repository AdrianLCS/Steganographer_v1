from PIL import Image
import numpy as np

class Revelar:
    def __init__(self, senha, origem):
        self.mensagem = ""
        self._senha = senha
        self._im = Image.open(origem)
        self._shlen = len(senha)
        self._w = self._im.size[0]
        self._h = self._im.size[1]
        self._data = np.array(self._im.convert('RGB'))
        self._chshbin = "" #definido quando a função_criaSenhaBinaria é chamada
        self._tamanho = ""#definido quando a função_revelaTamanho é chamada

    def _criaSenhaBinaria(self):
        for c in bytearray(self._senha, "utf-8"):
            result = format(c, 'b')
            while len(result) < 8:
                result = "0" + result
            self._chshbin = self._chshbin + result

    def _revelaTamanho(self):
        tamanhoDaMensage = ""
        for j in range(self._w):
            if (self._data[0][j][2] % 2 == 0):
                tamanhoDaMensage = tamanhoDaMensage + "0"
            else:
                tamanhoDaMensage = tamanhoDaMensage + "1"
        self._tamanho = 8 * int(tamanhoDaMensage, 2)

    def _revelaMensagem(self):
        mcont=0
        scont=0
        mensagemBinaria=""
        self.mensagem=""
        for i in range(1, self._h):
            if mcont == self._tamanho:
                break
            else:
                for j in range(self._w):
                    if mcont == self._tamanho:
                        break
                    else:
                        if (self._chshbin[scont] == "0"):
                            if (scont == 8 * self._shlen - 1):
                                scont = 0;
                            else:
                                scont += 1
                            continue
                        else:
                            if (self._data[i][j][2] % 2 == 0):
                                mensagemBinaria = mensagemBinaria+ "0"
                            else:
                                mensagemBinaria = mensagemBinaria + "1"
                        mcont += 1
                        if (scont == 8 * self._shlen - 1):
                            scont = 0;
                        else:
                            scont += 1
        # Converter a msg para caractere
        for i in range(0, len(mensagemBinaria), 8):
            self.mensagem = self.mensagem + chr(int(mensagemBinaria[i:i + 8], 2))


    def run(self):
        self._criaSenhaBinaria()
        self._revelaTamanho()
        self._revelaMensagem()
        return self.mensagem
