from .ni_daq.py import NIDevice

class GalvoMirror:
    def __init__(self, device_name, x_channel, y_channel):
        self.device = NIDevice(device_name)
        self.x_channel = x_channel
        self.y_channel = y_channel
        self.task = self.device.create_task('GalvoMirrorTask')

    def move_to(self, x_voltage, y_voltage):
        self.device.write_analog(self.task, self.x_channel, x_voltage)
        self.device.write_analog(self.task, self.y_channel, y_voltage)

    def start(self):
        self.device.start_task(self.task)

    def stop(self):
        self.device.stop_task(self.task)

    def close(self):
        self.device.close_task(self.task)
