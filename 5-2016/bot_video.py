import telebot
import cv2
import numpy as np

TOKEN = ''
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    
    cid = message.chat.id # id de la conversacion
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    markup.add('VIDEO')
    msg = bot.send_message(cid, "Choose an Action:", reply_markup=markup)

@bot.message_handler(regexp="^VIDEO$")
def info(message):
    cid = message.chat.id 
    cap = cv2.VideoCapture(1)
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'H264')
    out = cv2.VideoWriter('/tmp/video.mp4',fourcc, 20.0, (640,480))
    nro_frame = 100
    while(nro_frame != 0):
        ret, frame = cap.read()
        if ret==True:
            #frame = cv2.flip(frame,0)
            # write the flipped frame
            out.write(frame)
            nro_frame += -1
            #cv2.imshow('frame',frame)
            #if cv2.waitKey(1) & 0xFF == ord('q'):
                #break
        else:
            break
    # Release everything if job is finished
    cap.release()
    out.release()

    video = open('/tmp/video.mp4', 'rb')
    bot.send_video(cid, video)
    #bot.send_video(chat_id, "FILEID")


     
if __name__ == '__main__':
    bot.polling()
