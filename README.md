# Python MAC Address Changer

A simple Python script to randomly change the MAC address of a network interface on Linux systems.  
This tool demonstrates basic networking operations and subprocess handling in Python.

> Developed by ExileSec

⚠️ Disclaimer:  
Use this script responsibly. Changing MAC addresses on networks you do not own or without permission may be illegal.

## Features

- Generates a random MAC address
- Retrieves the current MAC address of the interface
- Safely brings the interface down, changes the MAC, and brings it back up
- Lightweight and easy to use

## Requirements

- Linux system
- Python 3.x

## Usage

Run the script as root:

```bash
sudo python3 macChanger.py
