import telebot

bot = telebot.TeleBot('5213813270:AAEVa-TVw35X7SprHQ99M72eqF0TTgx35l0')

ourchatid=-1001139329557
idg = 789996181
idd = 719289365
idl = 1359601863
idr = 841463984
nikg = '@freak_sqd03'
nikd = '@artmv_d'
nikl = '@lizk1a1'
nikr = '@r4419'

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привет! Я Морошка - бот, который регулирует общение в чате!  ')

if __name__ == '__main__':
    bot.skip_pending = True
    bot.infinity_polling()