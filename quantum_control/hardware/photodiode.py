from .ni_daq import NIDevice

class Photodiode:
    def __init__(self, device_name, channel):
        self.device = NIDevice(device_name)
        self.channel = channel
        self.task = self.device.create_task('PhotodiodeTask')

    def start_measurement(self, samples=1000, rate=1000.0):
        self.task.ai_channels.add_ai_voltage_chan(self.channel)
        self.task.timing.cfg_samp_clk_timing(rate, sample_mode=AcquisitionType.CONTINUOUS)
        self.device.start_task(self.task)

    def read_data(self):
        data = self.device.read_analog(self.task, self.channel)
        return data

    def stop_measurement(self):
        self.device.stop_task(self.task)
        self.device.close_task(self.task)
