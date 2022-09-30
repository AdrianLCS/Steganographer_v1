# -*- coding: utf-8 -*-

from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.app import App
import Ocultar
import Revelar

path = ""
aux = 0
Builder.load_file('Maintela.kv')

class TelaSecundaria(Widget):
    def selected(self, filename):
        try:
            self.ids.my_image.source = filename[0]
        except:
            pass
    def salvar(self, filename):
        global path
        path = self.ids.my_image.source = filename[0]
        global aux
        aux = 0
        Steg().stop()
        Builder.load_file('Maintela.kv')
        Steg().run()


class TelaPrincipal(Widget):
    def procurar(self):
        global aux
        aux=1
        Steg().stop()
        Builder.load_file('Tela.kv')
        Steg().run()
        self.ids.selected_image.source=path

    def ocultar(self):
        o=Ocultar.Ocultar(str(self.ids.mensagem.text), str(self.ids.senha.text), path)
        o.run()
    def revelar(self):
        r=Revelar.Revelar(str(self.ids.senha.text), path)
        self.ids.mensagem.text =r.run()

class Steg(App):
    def build(self):
        if aux==0:
            return TelaPrincipal()
        else:
            return TelaSecundaria()

if __name__=='__main__':
    Steg().run()