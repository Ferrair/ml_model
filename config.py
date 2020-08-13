class Environment:
    TEST = 'test'  # 输出到物理测试点位
    PROD = 'prod'  # 输出到生产环境点位
    NONE = 'none'  # 不输出到任何点位


CONTROL_URL = 'http://10.100.100.210/api/PLC/SetPLC'
ROOT_PATH = '.'
