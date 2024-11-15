from televisores.marca import Marca
from televisores.control import Control
class TV:
    _numTV = 0
    def __init__(self, marca, estado):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        self._control = None
        TV._numTV += 1

    def turnOff(self):
        self._estado == False
    def turnOn(self):
        self._estado == True
    def getCanal(self):
        return self._canal
    def setCanal(self, ncanal):
        if (self._estado == True) and (self._canal >= 0 and self._canal <= 120):
            self._canal = ncanal
    def getMarca(self):
        return self._marca
    def setMarca(self, nmarca):
        self._marca = nmarca
    def getPrecio(self):
        return self._precio
    def setPrecio(self, nprecio):
        self._precio = nprecio
    def getVolumen(self):
        return self._volumen
    def setVolumen(self, nvolumen):
        if (self._estado == True) and (self._volumen <= 7 and self._volumen >= 0):
            self._volumen = nvolumen
    def getControl(self):
        return self._control
    def setControl(self, ncontrol):
        self._control = ncontrol
    @classmethod
    def getNumTV(cls):
        return cls._numTV
    @classmethod 
    def setNumTV(cls, num):
        cls._numTV = num
    def getEstado(self):
        return self._estado
    def canalUp(self):
        if (self._estado == True) and (self._canal >= 0 and self._canal < 120):
            self._canal += 1
    def canalDown(self):
        if (self._estado == True) and (self._canal > 0 and self._canal <= 120):
            self._canal -= 1
    def volumenUp(self):
        if (self._estado == True) and (self._volumen <7 and self._volumen >= 0):
            self._volumen += 1
    def volumenDown(self):
        if (self._estado == True) and (self._volumen <=7 and self._volumen > 0):
            self._volumen -=1 
