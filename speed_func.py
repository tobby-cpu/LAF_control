import time
import config.init as cf
# 函数说明：速度模式函数；参数：id为电缸ID号，speed为设置电缸速度， val为设置电缸位置数据
def speed(ser,speed, val):
    bytes = [0x55, 0xAA]              # 帧头
    bytes.append(0x0D)                # 数据长度
    bytes.append(cf.LAF_ID)                  # ID号
    bytes.append(cf.CMD_WR_REGISTER)  # CMD_WR_REGISTER 写寄存器命令标志
    bytes.append(0x25)                # 控制模式寄存器地址低字节
    bytes.append(0x00)                # 控制模式寄存器地址高字节
    bytes.append(0x02)                # 设置控制模式为速度模式
    bytes.append(0x00)                # 设置控制模式为速度模式
    bytes.append(0x00)                # 电机输出电压寄存器，在定位模式无用
    bytes.append(0x00)                # 电机输出电压寄存器，在定位模式无用
    bytes.append(0x00)                # 力控目标值寄存器，在定位模式无用
    bytes.append(0x00)                # 力控目标值寄存器，在定位模式无用
    bytes.append(speed & 0xff)        # 目标速度寄存器
    bytes.append((speed >> 8) & 0xff) # 目标速度寄存器
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