import nidaqmx
from nidaqmx.constants import AcquisitionType, Edge

class NIDevice:
    def __init__(self, device_name):
        self.device_name = device_name

    def create_task(self, task_name):
        return nidaqmx.Task(task_name)
    
    def write_analog(self, task, channel, value):
        task.ao_channels.add_ao_voltage_chan(channel)
        task.write(value)

    def read_analog(self, task, channel, samples=1):
        task.ai_channels.add_ai_voltage_chan(channel)
        return task.read(samples)
    
    def start_task(self, task):
        task.start()

    def stop_task(self, task):
        task.stop()

    def close_task(self, task):
        task.close()
