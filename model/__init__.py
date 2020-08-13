import json
import logging

from PythonDeviceControlLib.CommandHandler import CommandHandler
from PythonDeviceControlLib.DeviceCommands import DeviceCommandTypes

from config import CONTROL_URL

handler = CommandHandler(CONTROL_URL)
