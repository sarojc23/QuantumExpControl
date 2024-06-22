from setuptools import setup, find_packages

setup(
    name='QuantumLabControl',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'pyqt5',
        'nidaqmx',
    ],
    entry_points={
        'console_scripts': [
            'quantumlabcontrol=quantum_control.ui.main_window:main',
        ],
    },
)
