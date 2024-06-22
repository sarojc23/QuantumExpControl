# QuantumLabControl (...under developement)

QuantumLabControl is a Python-based software suite for controlling and automating quantum physics experiments. It supports various hardware devices and provides a user-friendly interface for experiment management.

## Features
- Control galvo mirrors using NI DAQ devices
- Collect and display data from photodiodes
- Modular and extensible design
- User-friendly graphical interface

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/QuantumLabControl.git
   cd QuantumLabControl

2. **Create and activate a conda environment**:
conda create --name quantum_control_env python=3.12
conda activate quantum_control_env

3. **Install dependencies:**
pip install -r requirements.txt

4. **Run the application:**
python -m quantum_control.ui.main_window

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for suggestions.

By following these steps, you will have a conda environment set up for your quantum control software using Python 3.12, making it easier to manage dependencies and maintain a consistent development environment.


## Directory Structure
'''
QuantumLabControl/
├── README.md
├── LICENSE
├── setup.py
├── quantum_control/
│   ├── __init__.py
│   ├── core/
│   ├── hardware/
│   │   ├── __init__.py
│   │   ├── device.py
│   │   ├── ni_daq.py
│   │   └── galvo_mirror.py
│   ├── ui/
│   ├── utils/
└── tests/
