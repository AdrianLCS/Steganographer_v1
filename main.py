# -*- coding: utf-8 -*-
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
import Ocultar
import Revelar

path = ""


# define diferentes telas

class GerenciadorDeTela(ScreenManager):
    pass


class TelaPrincipal(Screen):
    def setImage(self):
        global path
        self.ids.selected.source = path

    def ocultar(self):
        global path
        o = Ocultar.Ocultar(str(self.ids.mensagem.text), str(self.ids.senha.text), path)
        o.run()

    def revelar(self):
        global path
        r = Revelar.Revelar(str(self.ids.senha.text), path)
        self.ids.mensagem.text = r.run()


class TelaSecundaria(Screen):
    def selected(self, filename):
        try:
            self.ids.my_image.source = filename[0]
        except:
            pass

    def salvar(self, filename):
        global path
        path = filename[0]
        TelaPrincipal().setImage()


kv = Builder.load_file('Telas.kv')


class Steg(App):
    def build(self):
        return kv


if __name__ == '__main__':
    Steg().run()
