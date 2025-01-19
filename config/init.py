import json
def read_config():
    global port ,baudrate ,timeout,Hand_ID,Angle_address,LAF_ID,CMD_WR_REGISTER
    file_path = 'config/parameter.json'
    with open(file_path, 'r',encoding='utf-8-sig') as f:
        config = json.load(f)
    
    port = config['port']
    baudrate = config['baudrate']
    timeout = config['time_out']
    Hand_ID = config['Hand_ID']
    Angle_address = config['Angle_address']
    LAF_ID = config['LAF_ID']
    CMD_WR_REGISTER = config['CMD_WR_REGISTER']

    print(f"串口端口: {port}")
    print(f"波特率: {baudrate}")
    print(f"超时时间: {timeout} 秒")
    print(f"灵巧手设备ID: {Hand_ID}")
    print(f"角度寄存器地址: {Angle_address}")
    print(f"LAF电机设备ID: {LAF_ID}")
    print(f"CMD_WR_REGISTER 写寄存器命令标志: {CMD_WR_REGISTER}")

read_config()