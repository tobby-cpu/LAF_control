import time
import config.init as cf
# 函数说明：力控模式函数；参数：id为电缸ID号， force为力控目标值
def force(ser, force):
    bytes = [cf.FRAME_LAF1, cf.FRAME_LAF2]              # 帧头
    bytes.append(0x0D)                # 数据长度
    bytes.append(cf.LAF_ID)                  # ID号
    bytes.append(cf.CMD_WR_REGISTER)                # CMD_WR_REGISTER 写寄存器命令标志
    bytes.append(0x25)                # 控制模式寄存器地址低字节
    bytes.append(0x00)                # 控制模式寄存器地址高字节
    bytes.append(0x03)                # 设置控制模式为力控模式
    bytes.append(0x00)                # 设置控制模式为力控模式
    bytes.append(0x00)                # 电机输出电压寄存器，在力控模式无用
    bytes.append(0x00)                # 电机输出电压寄存器，在力控模式无用
    bytes.append(force & 0xff)        # 力控目标值
    bytes.append((force >> 8) & 0xff) # 力控目标值
    checksum = 0x00                   # 校验和初始化为0
    for i in range(2, len(bytes)):
        checksum += bytes[i]          # 对数据进行加和处理
    checksum &= 0xFF                  # 对校验和取低八位
    bytes.append(checksum)            # 低八位校验和
    ser.write(bytes)                  # 向串口写入数据
    time.sleep(0.01)                  # 延时10ms
    ser.read_all()                    # 把返回帧读掉，不处理
#3代手力控函数
    def force_hand(ser,val1,val2,val3,val4,val5,val6):
    length = 12+2+1                     
    bytes = [cf.FRAME_HAND1, cf.FRAME_HAND2]                 # 帧头
    bytes.append(cf.Hand_ID)                                 # ID
    bytes.append(length)
    bytes.append(cf.CMD_HANDG3_WRITE)  #写3代手寄存器指令
    bytes.append(cf.CMD_FINGER_FORCE_SET_2B & 0xff)          # 目标寄存器地址
    bytes.append((cf.CMD_FINGER_FORCE_SET_2B >> 8) & 0xff)   # 目标寄存器地址           
    bytes.append(val1 & 0xff)          
    bytes.append((val1 >> 8) & 0xff)   
    bytes.append(val2 & 0xff)          
    bytes.append((val2 >> 8) & 0xff)   
    bytes.append(val3 & 0xff)          
    bytes.append((val3 >> 8) & 0xff)   
    bytes.append(val4 & 0xff)          
    bytes.append((val4 >> 8) & 0xff)   
    bytes.append(val5 & 0xff)          
    bytes.append((val5 >> 8) & 0xff)   
    bytes.append(val6 & 0xff)          
    bytes.append((val6 >> 8) & 0xff)   
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
