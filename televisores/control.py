class Control:
    def __init__(self):
        self._tv = None

    def turnOn(self):
        self._tv.turnOn()
    def turnOff(self):
        self._tv.turnOff()
    def canalUp(self):
        self._tv.canalUp()
    def canalDown(self):
        self._tv.canalUp()
    def volumenUp(self):
        self._tv.volumenUp()
    def volumenDown(self):
        self._tv.volumenDown()
    def setCanal(self, ncanal):
        if self._tv and self._tv.getEstado():
            self._tv.setCanal(ncanal)
    def setVolumen(self, nvol):
        self._tv.setVolumen(nvol)

    def enlazar(self, tele):
        self._tv = tele
        tele._control = self

    def setTv(self, tele):
        self._tv = tele
    def getTv(self):
        return self._tv
