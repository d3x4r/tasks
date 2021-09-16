from abc import ABC, abstractmethod


class MacDevice():
    PORT_TYPE = 'usb-c'

    def __init__(self):
        self.currentConnection = None

    def connect(self, macName):
        self.currentConnection = macName

    def checkConnection(self):
        if self.currentConnection is None:
            raise ValueError('Device is not connected to mac')


class KeyBoard(MacDevice):
    def print(self, value):
        self.checkConnection()
        print(f'Text from keyboard: {value}')


class Mouse(MacDevice):
    def mouseMove(self):
        self.checkConnection()
        print('Mouse moved')


class AbstractDisplay(ABC, MacDevice):
    @abstractmethod
    def show(self): pass


class HDDisplay(AbstractDisplay):
    def show(self):
        self.checkConnection()
        print('Broadcast from HDDisplay')


class VGADisplay(AbstractDisplay):
    def show(self):
        self.checkConnection()
        print('Broadcast from VGADisplay')


class AbstractMac(ABC):
    PORT_TYPE = 'usb-c'

    def __init__(self):
        self.ports = {
            'port1': None,
            'port2': None,
            'port3': None,
            'port4': None,
        }

    @abstractmethod
    def connect(self, device: MacDevice): pass


class Macbook(AbstractMac):

    def connect(self, device: MacDevice):
        if device.PORT_TYPE != self.PORT_TYPE:
            raise ValueError('Wrong port type')

        for portName in self.ports.keys():
            if self.ports[portName] is None:
                print(f"connected {device.__class__.__name__} to {portName}")
                self.ports[portName] = device
                device.connect(self.__class__.__name__)
                break
        else:
            raise ValueError('No free slots')

#example
# mac = Macbook()
# first_display = HDDisplay()
# second_display = VGADisplay()
# mouse = Mouse()
# keyboard = KeyBoard()
# mac.connect(first_display)
# mac.connect(second_display)
# mac.connect(mouse)
# mac.connect(keyboard)
# first_display.show()
# second_display.show()
# mouse.mouseMove()
# keyboard.print('text')
