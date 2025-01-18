import time    # 调用时间库
import config.init as cf
#LAF电机控制函数
# 函数说明：位置模式函数；参数：id为电缸ID号， val为设置电缸位置数据
def position_LAF(ser, id, val):
    bytes = [0x55, 0xAA]              # 帧头
    bytes.append(0x0D)                # 数据长度
    bytes.append(id)                  # ID号
    bytes.append(0x32)                # CMD_WR_REGISTER 写寄存器命令标志
    bytes.append(0x25)                # 控制模式寄存器地址低字节
    bytes.append(0x00)                # 控制模式寄存器地址高字节
    bytes.append(0x00)                # 设置控制模式为速度模式
    bytes.append(0x00)                # 设置控制模式为速度模式
    bytes.append(0x00)                # 电机输出电压寄存器，在定位模式无用
    bytes.append(0x00)                # 电机输出电压寄存器，在定位模式无用
    bytes.append(0x00)                # 力控目标值寄存器，在定位模式无用
    bytes.append(0x00)                # 力控目标值寄存器，在定位模式无用
    bytes.append(0x00)                # 目标速度寄存器
    bytes.append(0x00)                # 目标速度寄存器
    bytes.append(val & 0xff)          # 目标位置
    bytes.append((val >> 8) & 0xff)   # 目标位置
    checksum = 0x00                   # 校验和初始化为0
    for i in range(2, len(bytes)):
        checksum += bytes[i]          # 对数据进行加和处理
    checksum &= 0xFF                  # 对校验和取低八位
    bytes.append(checksum)            # 低八位校验和
    ser.write(bytes)                  # 向串口写入数据
    time.sleep(0.01)                  # 延时10ms
    ser.read_all()                    # 把返回帧读掉，不处理

#3代手控制函数,设置了6个连续的角度值
def position_hand(ser,val1,val2,val3,val4,val5,val6):
    id = 1
    length = 2*6
    bytes = [0xEB, 0x90]              # 帧头
    bytes.append(id)                  # ID
    bytes.append(cf.Angle_address & 0xff)          # 目标寄存器地址
    bytes.append((cf.Angle_address >> 8) & 0xff)   # 目标寄存器地址
    bytes.append(length + 3)           #6个角度值，每个值占2B，故为12
    bytes.append(0x12)                 #写3代手寄存器指令
    bytes.append(val1 & 0xff)          #设置小拇指角度值
    bytes.append((val1 >> 8) & 0xff)   #设置小拇指角度值
    bytes.append(val2 & 0xff)          #设置无名指角度值
    bytes.append((val2 >> 8) & 0xff)   #设置无名指角度值
    bytes.append(val3 & 0xff)          #设置中指角度值
    bytes.append((val3 >> 8) & 0xff)   #设置中指角度值
    bytes.append(val4 & 0xff)          #设置食指角度值
    bytes.append((val4 >> 8) & 0xff)   #设置食指角度值
    bytes.append(val5 & 0xff)          #设置大拇指角度值
    bytes.append((val5 >> 8) & 0xff)   #设置大拇指角度值
    bytes.append(val6 & 0xff)          #设置大拇指旋转角度值
    bytes.append((val6 >> 8) & 0xff)   #设置大拇指旋转角度值
    #计算校验和
    checksum = 0x00                    # 校验和初始化为0
    send_len = length + 5
    for i in range(2, send_len - 1):
        checksum += bytes[i]          # 对数据进行加和处理
    checksum &= 0xFF                  # 对校验和取低八位
    bytes.append(checksum)            # 低八位校验和
    ser.write(bytes)                  # 向串口写入数据
    time.sleep(0.01)                  # 延时10ms
    ser.read_all()                    # 把返回帧读掉，不处理
