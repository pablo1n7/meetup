import telebot
from pyspectator.processor import Processor
from pyspectator.computer import Computer
from pyspectator.computer import psutil
from time import sleep

TOKEN = '255936942:AAHKa3FKJcys_dpN7vIin0fJgMGuWzYeRzs'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    
    cid = message.chat.id # id de la conversación
    markup = telebot.types.ReplyKeyboardMarkup(row_width=4)
    markup.add('INFO', 'DISK','CPU','MEMORY')
    msg = bot.send_message(cid, "Choose an Action:", reply_markup=markup)

@bot.message_handler(regexp="^INFO$")
def info(message):
    computer = Computer()
    cid = message.chat.id 
    info = "S.O {} {} \nIP {} \nPython {} \nCPU {}".format(computer.os,computer.architecture,computer.network_interface.ip_address,computer.python_version,computer.processor.name)
    bot.send_message(cid,info)


@bot.message_handler(regexp="^DISK$")
def disk_info(message):
    computer = Computer()
    cid = message.chat.id 
    for memory in computer.nonvolatile_memory:
        size = memory.total/1024/1024
        info = "File System {} \nMount {} \nSize {} \nMB Use {} %".format(memory.fstype,memory.device,int(size),memory.used_percent)
        bot.send_message(cid,info)

@bot.message_handler(regexp="^CPU$")
def cpu_info(message):
    computer = Computer()
    cid = message.chat.id 
    cpu = Processor(monitoring_latency=1)
    with cpu:
     for i in range(cpu.count):
        print(cpu.load, cpu.temperature)
        info = "CPU{} \nUse {} % \nTemp {} C".format(i,cpu.load,cpu.temperature) 
        bot.send_message(cid,info)
        sleep(1.1)

@bot.message_handler(regexp="^MEMORY$")
def memory(message):
    computer = Computer()
    cid = message.chat.id 
    info = "SIZE {} \nUSE {}%".format(computer.virtual_memory.total/1073741824,computer.virtual_memory.used_percent)
    bot.send_message(cid,info)

     
    
if __name__ == '__main__':

    bot.polling()


