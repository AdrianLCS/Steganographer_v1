from PIL import Image
import numpy as np


class Ocultar:
    def __init__(self, mensagem, senha, origem):
        self._path = origem
        self._mensagem = mensagem
        self._senha = senha
        self._im = Image.open(origem)
        self._msglen = len(mensagem)
        self._shlen = len(senha)
        self._w = self._im.size[0]
        self._h = self._im.size[1]
        self._data = np.array(self._im.convert('RGB'))
        self._tambin = format(self._msglen, "b")
        self._chmsgbin = "" #definido quando a função_criaMensagemBinaria é chamada
        self._chshbin = "" #definido quando a função_criaSenhaBinaria é chamada

    def _criaMensagemBinaria(self):
        for c in bytearray(self._mensagem, "utf-8"):
            result = format(c, 'b')
            while len(result) < 8:
                result = "0" + result
            self._chmsgbin = self._chmsgbin + result

    def _criaSenhaBinaria(self):
        for c in bytearray(self._senha, "utf-8"):
            result = format(c, 'b')
            while len(result) < 8:
                result = "0" + result
            self._chshbin = self._chshbin + result

    def _registraTamanho(self): #altera self_data com infromações do tamanho da mensagem
        tamcont=0
        for j in range(self._w):
            if (j < self._w - len(self._tambin)):
                if (self._data[0][j][2] % 2 == 0):
                    continue
                else:
                    self._data[0][j][2] -= 1
            else:
                if ((self._tambin[tamcont] == "0" and self._data[0][j][2] % 2 == 0) or (
                        self._tambin[tamcont] == "1" and self._data[0][j][2] % 2 == 1)):
                    {}
                else:
                    if (self._data[0][j][2] % 2 == 0):
                        self._data[0][j][2] += 1
                    else:
                        self._data[0][j][2] -= 1
            tamcont += 1


    def _registaMensagem(self):
        mcont=0
        scont=0
        for i in range(1, self._h):
            if mcont == 8 * self._msglen:
                break
            else:
                for j in range(self._w):
                    if mcont == 8 * self._msglen:
                        break
                    else:
                        if (self._chshbin[scont] == "0"):
                            if (scont == 8 * self._shlen - 1):
                                scont = 0;
                            else:
                                scont += 1
                            continue
                        else:
                            if ((self._chmsgbin[mcont] == "0" and self._data[i][j][2] % 2 == 0) or (
                                    self._chmsgbin[mcont] == "1" and self._data[i][j][2] % 2 == 1)):
                                pass
                            else:
                                if (self._data[i][j][2] % 2 == 0):
                                    self._data[i][j][2] += 1
                                else:
                                    self._data[i][j][2] -= 1
                        mcont += 1
                        if (scont == 8 * self._shlen - 1):
                            scont = 0
                        else:
                            scont += 1

    def _salvar(self):
        im2 = Image.fromarray(self._data)
        im2.save(self._path[0:str(self._path).rfind(".")]+"v2.png")

    def run(self):
        self._criaMensagemBinaria()
        self._criaSenhaBinaria()
        self._registraTamanho()
        self._registaMensagem()
        self._salvar()

