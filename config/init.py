import json
def read_config():
    global port ,baudrate ,timeout,ID,Angle_address
    file_path = 'config/parameter.json'
    with open(file_path, 'r',encoding='utf-8-sig') as f:
        config = json.load(f)
    
    port = config['port']
    baudrate = config['baudrate']
    timeout = config['time_out']
    ID = config['ID']
    Angle_address = config['Angle_address']
    print(f"串口端口: {port}")
    print(f"波特率: {baudrate}")
    print(f"超时时间: {timeout} 秒")
    print(f"设备ID: {ID}")
    print(f"角度寄存器地址: {Angle_address}")

