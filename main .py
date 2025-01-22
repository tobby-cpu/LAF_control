import time    # 调用时间库
from control_func import openSerial
from position_func import position_wrist,position_hand
from speed_func import speed_hand,speed_wrist
from config.init import read_config
from readstatus_func import Hand_readState,wrist_readState
from force_func import force_LAF,force_HAND
import config.init as cf
# 主函数功能：首先打开串口，设置对应的端口和波特率，依次设置电缸运动位置参数
if __name__ == '__main__':
     
    read_config()
    print('打开串口！') # 打印提示字符“打开串口”
    ser = openSerial(cf.port, cf.baudrate) # 改成自己的串口号和波特率，波特率默认921600
    time.sleep(1)
    
    print('设置电缸速度信息')                     #速度控制函数调试
    speed_hand(ser, 0 , 0 , 0 , 0 , 0 , 0 )
    speed_wrist(ser,0)  
    time.sleep(1)

    print('设置电缸位置信息，-1为不设置该运动速度！')     
    position_hand(ser,500,500,500,500,500,500)
    position_wrist(ser,-10,10)
    time.sleep(1)

    print('设置力控目标值')               #力控函数调试
    force_HAND(ser,10,10,10,10,10,10)
    time.sleep(1)

    print('读取电缸状态信息')
    Hand_readState(ser,cf.CMD_FINGER_ANGLE_2B)      #可以通过改变输入的寄存器地址参数来读取不同的内容
    wrist_readState(ser,cf.CMD_WRIST_SPEED_SET)
'''
    
    print('设置电缸力控目标值，速度以及位置信息')
    force_LAF(ser,10,2000,2000)
    force_HAND(ser,0,0,0,0,0,0)
    time.sleep(1)
    
    print('设置电机输出电压')
  #  voltage(ser,1, 10)
  '''
 

    # time.sleep(10) # 由于力校准时间较长，请不要漏过这个sleep并尝试重新与手通讯，可能导致插件崩溃
