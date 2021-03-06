import json
import logging
from PythonDeviceControlLib.DeviceCommands import DeviceCommandTypes
from model import handler


def decode(res):
    try:
        return json.loads(res.decode())
    except Exception as e:
        raise Exception('plc api return error. {}'.format(res))


def _is_failure(res):
    try:
        fail = False
        for r in res:
            fail = fail or not r['IsSetSuccessful']
        return fail
    except Exception as e:
        logging.error(e)
        return False


def _get_value(res, address):
    res = json.loads(res.decode())
    for r in res:
        if address == r['Address']:
            return r['PreviousValue']
    return None


def reset_prod(values: list):
    for _ in range(5):
        res = handler.RunPLCCommand(DeviceCommandTypes.ML_5K_HS_TB_WD_READ_HMI, [])
        res = decode(res)
        if not _is_failure(res) and int(_get_value(res, "5H.5H.LD5_KL2226_PID042MCVHMI")) == 0:
            res = handler.RunPLCCommand(DeviceCommandTypes.ML_5K_HS_TB_WD_RESET_ALL, values)
            res = decode(res)
            return res
        handler.RunPLCCommand(DeviceCommandTypes.ML_5K_HS_TB_WD_SWITCH_AUTO, [])
    return None


def reset_test(values: list):
    res = handler.RunPLCCommand(DeviceCommandTypes.ML_5H_5H_LD5_TEST_RESET_ALL, values)
    return decode(res)
