import serial  # 调用串口通信库
import time    # 调用时间库
from control_func import openSerial,speed,speedForce,reedState
from position_func import position_hand,position_LAF
from config.init import read_config
import config.init as cf
# 主函数功能：首先打开串口，设置对应的端口和波特率，依次设置电缸运动位置参数
if __name__ == '__main__':
    
    print('打开串口！') # 打印提示字符“打开串口”
    ser = openSerial('COM7', 921600) # 改成自己的串口号和波特率，波特率默认921600
    time.sleep(1)
    print('设置电缸位置信息，-1为不设置该运动速度！')
                                  
    read_config()   #读取所需参数
    #开始执行控制语句
    #首先进行位置参数的调试
    position_LAF(ser,cf.LAF_ID ,0)
    position_hand(ser, 0 , 0 , 0 , 0 , 0 ,0 )
    time.sleep(1)
    
    print('设置电缸速度以及位置信息')
    speed(ser, 1, 1000,1200)    # ID号改为对应电缸的ID号
    time.sleep(1)
    '''
    print('设置电缸力控目标值，速度以及位置信息')
    speedForce(ser,1, 10, 2000, 2000)
    time.sleep(1)
    print('设置力控目标值')
    #speed(ser,1, 10)
    time.sleep(1)
    print('设置电机输出电压')
  #  voltage(ser,1, 10)
    print('读取电缸状态信息')
    reedState(ser, 1)

    # time.sleep(10) # 由于力校准时间较长，请不要漏过这个sleep并尝试重新与手通讯，可能导致插件崩溃
  '''