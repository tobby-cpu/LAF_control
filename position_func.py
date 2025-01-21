import time    # 调用时间库
import config.init as cf
#LAF电机控制函数
# 函数说明：位置模式函数；参数：id为电缸ID号， val为设置电缸位置数据
def position_LAF(ser,val):
    bytes = [cf.FRAME_LAF1, cf.FRAME_LAF2]              # 帧头
    bytes.append(0x0D)                # 数据长度
    bytes.append(cf.LAF_ID)                  # ID号
    bytes.append(cf.CMD_WR_REGISTER)                # CMD_WR_REGISTER 写寄存器命令标志
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
def position_hand(ser,val1):
    length = 2*6                      #设置了6个角度，每个角度占2B
    bytes = [cf.FRAME_HAND1, cf.FRAME_HAND2]              # 帧头
    bytes.append(cf.Hand_ID)                  # ID
    bytes.append(length + 3)           #6个角度值，每个值占2B，故为12
    bytes.append(cf.CMD_HANDG3_WRITE)  #写3代手寄存器指令
    bytes.append(cf.CMD_FINGER_ANGLE_SET_2B & 0xff)          # 目标寄存器地址
    bytes.append((cf.CMD_FINGER_ANGLE_SET_2B >> 8) & 0xff)   # 目标寄存器地址
    bytes.append(val1 & 0xff)          #设置小拇指角度值
    bytes.append((val1 >> 8) & 0xff)   #设置小拇指角度值
    #计算校验和
    checksum = 0x00                    # 校验和初始化为0
    for i in range(2,len(bytes) ):
        checksum += bytes[i]          # 对数据进行加和处理
    checksum &= 0xFF                  # 对校验和取低八位
    bytes.append(checksum)            # 低八位校验和
    ser.write(bytes)                  # 向串口写入数据
    time.sleep(0.01)                  # 延时10ms
    ser.read_all()                    # 把返回帧读掉，不处理

def position_wrist(ser,val1,val2):
    length = 4                      #设置了6个角度，每个角度占2B
    bytes = [cf.FRAME_HAND1, cf.FRAME_HAND2]              # 帧头
    bytes.append(cf.Hand_ID)                  # ID
    bytes.append(length + 3)           #6个角度值，每个值占2B，故为12
    bytes.append(cf.CMD_WRIST_WRITE)  #写3代手寄存器指令
    bytes.append(cf.CMD_WRIST_ANGLE & 0xff)          # 目标寄存器地址
    bytes.append((cf.CMD_WRIST_ANGLE >> 8) & 0xff)   # 目标寄存器地址
    bytes.append(val1 & 0xFF)          #设置偏转角度
    bytes.append((val1 >> 8) & 0xFF)   #设置偏转角度
    bytes.append(val2 & 0xFF)          #设置俯仰角度
    bytes.append((val2 >> 8) & 0xFF)   #设置俯仰角度
    #计算校验和
    checksum = 0x00                    # 校验和初始化为0
    for i in range(2,len(bytes) ):
        checksum += bytes[i]          # 对数据进行加和处理
    checksum &= 0xFF                  # 对校验和取低八位
    bytes.append(checksum)            # 低八位校验和
    ser.write(bytes)                  # 向串口写入数据
    time.sleep(0.01)                  # 延时10ms
    ser.read_all()                    # 把返回帧读掉，不处理
