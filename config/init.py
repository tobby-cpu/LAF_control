import json
def read_config():
    global port ,baudrate ,timeout,Hand_ID,CMD_FINGER_ANGLE_SET_2B,LAF_ID,CMD_WR_REGISTER,CMD_HANDG3_WRITE
    global CMD_FINGER_SPEED_SET_2B,FRAME_HAND1,FRAME_HAND2,FRAME_LAF1,FRAME_LAF2,CMD_RD_STATUS,CMD_FINGER_ANGLE_2B
    global CMD_HANDG3_READ,CMD_WRIST_ANGLE
    file_path = 'config/parameter.json'
    with open(file_path, 'r',encoding='utf-8-sig') as f:
        config = json.load(f)
    
    port = config['port']
    baudrate = config['baudrate']
    timeout = config['time_out']
    Hand_ID = config['Hand_ID']
    CMD_FINGER_ANGLE_SET_2B = config['CMD_FINGER_ANGLE_SET_2B']
    LAF_ID = config['LAF_ID']
    CMD_WR_REGISTER = int(config['CMD_WR_REGISTER'],16)
    CMD_HANDG3_WRITE = int(config['CMD_HANDG3_WRITE'],16)
    CMD_FINGER_SPEED_SET_2B = config['CMD_FINGER_SPEED_SET_2B']
    FRAME_HAND1 = int(config['FRAME_HAND1'],16)
    FRAME_HAND2 = int(config['FRAME_HAND2'],16)
    FRAME_LAF1 = int(config['FRAME_LAF1'],16)
    FRAME_LAF2 = int(config['FRAME_LAF2'],16)
    CMD_RD_STATUS = int(config['CMD_RD_STATUS'],16)
    CMD_FINGER_ANGLE_2B = config['CMD_FINGER_ANGLE_2B']
    CMD_HANDG3_READ = int(config['CMD_HANDG3_READ'],16)
    CMD_WRIST_ANGLE = config['CMD_WRIST_ANGLE']

    print(f"串口端口: {port}")
    print(f"波特率: {baudrate}")
    print(f"超时时间: {timeout} 秒")
    print(f"灵巧手设备ID: {Hand_ID}")
    print(f"角度寄存器地址: {CMD_FINGER_ANGLE_SET_2B}")
    print(f"角度寄存器命令标志: {CMD_HANDG3_WRITE}")
    print(f"LAF电机设备ID: {LAF_ID}")
    print(f"写LAF电机寄存器命令标志: {CMD_WR_REGISTER}")
    print(f"写三代手寄存器命令标志: {CMD_HANDG3_WRITE}")
    print(f"三代手帧头1: {FRAME_HAND1}")
    print(f"三代手帧头2: {FRAME_HAND2}")
    print(f"LAF电机帧头1: {FRAME_LAF1}")
    print(f"LAF电机帧头2: {FRAME_LAF2}")
    print(f"LAF读寄存器命令标志: {CMD_RD_STATUS}")
    print(f"三代手读寄存器地址: {CMD_FINGER_ANGLE_2B}")
    print(f"三代手读寄存器命令标志: {CMD_HANDG3_READ}")