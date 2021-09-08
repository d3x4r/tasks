class Macbook():
    PORT_COUNT = 4
    PORT_TYPE = 'usb-c'

    def __init__(self):
        self.device_list = []
        self.connected_port_count = 0

    def connect(self, device):
        device_name = device['name']
        port_type = device['port_type']

        if self.connected_port_count == self.PORT_COUNT:
            raise ValueError(
                'The maximum number of connections has been reached')
        elif device_name not in self.device_list:
            raise ValueError('This device is not supported by this mac')
        elif port_type != self.PORT_TYPE:
            raise ValueError(
                f"Port {port_type} is not supported by this mac")

        self.connected_port_count += 1
        print('connected')

    def disconnect(self):
        if self.connected_port_count == 0:
            raise AttributeError('This device has no connections')
        self.connected_port_count -= 1
        print('disconnected')

    def add_device(self, device_name):
        if device_name in self.device_list:
            print(f'device {device_name} already added')
        self.device_list.append(device_name)
        print(f'device added {device_name}')


mac1 = Macbook()
mac1.add_device('device_name')
mac1.connect({'name': 'device_name', 'port_type': 'usb-c'})
print(mac1.connected_port_count)
mac2 = Macbook()
mac2.add_device('device_name')
mac2.connect({'name': 'device_name', 'port_type': 'usb-c'})
print(mac2.connected_port_count)
