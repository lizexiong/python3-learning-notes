#_*_coding:utf-8_*_
__author__ = 'Alex Li'

from plugins.linux import sysinfo,cpu_mac,memory,network,host_alive



def LinuxSysInfo():
    #print __file__
    return  sysinfo.collect()


def WindowsSysInfo():
    from windows import sysinfo as win_sysinfo
    return win_sysinfo.collect()

def get_linux_cpu():
    return cpu_mac.monitor()


def host_alive_check():
    return host_alive.monitor()

def GetLinuxCpuStatus():
    #return cpu.monitor()
    return cpu_mac.monitor()

def GetLinuxNetworkStatus():
    return network.monitor()

def GetLinuxMemStatus():
    return memory.monitor()


def get_linux_load():
    # return load.monitor()
    pass
