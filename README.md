# Raspberry Pi Pico Playground

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Description

This repository provides a comprehensive toolkit for controlling a Raspberry Pi Pico microcontroller board and managing 8 relay switches via Python and MQTT. It's designed for hobbyists, engineers, and anyone interested in DIY electronics and home automation projects. Using Python scripts, users can interface their Pico with multiple relay switches to control various devices, lights, or motors.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone this repository to your local machine.
2. Install the required Python libraries and MQTT broker.
```sh
pip install -r requirements
```
3. Explore the example scripts to start controlling your devices.

## Usage
1. Edit the main.py or create another python file
2. Please take note the "from core.relay import Relay" in line 1
3. Then see the following functions
```python
from core.relay import Relay

relay = Relay()
relay.turn("on", 8)
relay.turn("off", 8)
relay.on(8)
relay.off(8)
```

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

This project is licensed under the [MIT License](LICENSE).
