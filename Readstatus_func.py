import time
import config.init as cf

# 函数说明：读电缸状态信息；参数：id为电缸ID号
def LAF_reedState(ser):
    bytes = [cf.FRAME_LAF1, cf.FRAME_LAF2]  # 帧头
    bytes.append(0x01)                # 数据长度
    bytes.append(cf.LAF_ID)           # ID号
    bytes.append(cf.CMD_RD_STATUS)    # CMD_RD_STATUS 读寄存器命令标志
    checksum = 0x00                   # 校验和初始化为0
    for i in range(2, len(bytes)):
        checksum += bytes[i]          # 对数据进行加和处理
    checksum &= 0xFF                  # 对校验和取低八位
    bytes.append(checksum)            # 低八位校验和
    ser.write(bytes)                  # 向串口写入数据
    time.sleep(0.01)                  # 延时10ms
    recv = ser.read_all()             # 从端口读字节数据(应答帧)
    if len(recv) == 0:                # 如果返回的数据长度为0，直接返回
        return []
    num = (recv[2] & 0xFF) - 3      # 寄存器数据所返回的数量
    val = []
    for i in range(num):
        val.append(recv[7 + i])
    print('读到的寄存器值依次为：', end='')
    for i in range(num):
        print(val[i], end=' ')
    print()

def Hand_readState(ser,address):
    length = 3+1                      
    bytes = [cf.FRAME_HAND1, cf.FRAME_HAND2]              # 帧头
    bytes.append(cf.Hand_ID)                
    bytes.append(length)          
    bytes.append(cf.CMD_HANDG3_READ)      #写3代手寄存器指令
    bytes.append(address & 0xff)          # 目标寄存器地址
    bytes.append((address >> 8) & 0xff) 
    if address == cf.CMD_FINGER_ANGLE_SET_2B or address == cf.CMD_FINGER_SPEED_SET_2B or address == cf.CMD_FINGER_ANGLE_2B:
        bytes.append(12)                   #读取寄存器的长度，6个角度，每个角度占2B
    else:
        bytes.append(6)
    checksum = 0x00                    # 校验和初始化为0
    for i in range(2,len(bytes)):
        checksum += bytes[i]          # 对数据进行加和处理
    checksum &= 0xFF                  # 对校验和取低八位
    bytes.append(checksum)            # 低八位校验和
    ser.write(bytes)                  # 向串口写入数据
    time.sleep(0.01)                  # 延时10ms
    recv = ser.read_all()             # 读取返回帧
    if len(recv) == 0:                # 如果返回的数据长度为0，直接返回
        return []
    num = (recv[3] & 0xFF) - 3      # 寄存器数据所返回的数量
    val = []
    val_act = []
    for i in range(num):
        val.append(recv[7 + i])
    for j in range(num / 2):
        val_act.append((val[2*j] & 0xFF) + (val[1 + 2*j] << 8))   #解析数据，输出十进制数据
    print('读到的手指数据依次为：',end =' ')
    for k in range(num / 2):
        print(f"手指{k+1}: {val_act[k]}", end=' ')
    print()


def wrist_readState(ser,address):
    length = 3+1                      
    bytes = [cf.FRAME_HAND1, cf.FRAME_HAND2]              # 帧头
    bytes.append(cf.Hand_ID)                
    bytes.append(length)          
    bytes.append(cf.CMD_WRIST_READ)      #写手腕电机寄存器指令
    bytes.append(address & 0xff)          # 目标寄存器地址
    bytes.append((address >> 8) & 0xff) 
    if address == cf.CMD_WRIST_ANGLE_SET or address == cf.CMD_WRIST_ANGLE:
        bytes.append(4)                   #读取寄存器的长度，每个值占2B，现在读取位置
    else:
        bytes.append(2)
    checksum = 0x00                    # 校验和初始化为0
    for i in range(2,len(bytes)):
        checksum += bytes[i]          # 对数据进行加和处理
    checksum &= 0xFF                  # 对校验和取低八位
    bytes.append(checksum)            # 低八位校验和
    ser.write(bytes)                  # 向串口写入数据
    time.sleep(0.01)                  # 延时10ms
    recv = ser.read_all()             # 读取返回帧
    if len(recv) == 0:                # 如果返回的数据长度为0，直接返回
        return []
    num = (recv[3] & 0xFF) - 3      # 寄存器数据所返回的数量
    val = []
    val_act = []
    for i in range(num):
        val.append(recv[7 + i])
    for j in range(num / 2):
        val_act.append((val[2*j] & 0xFF) + (val[1 + 2*j] << 8))   #解析数据，输出十进制数据
    print('读到的手腕的值依次为：',end =' ')
    for k in range(num / 2):
        print(f"手腕{k+1}: {val_act[k]}", end=' ')
    print()
