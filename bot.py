import telebot 

Token = "6537693621:AAFCpiER3j2vABzqU6Seuack-e1EkKhWYxA"

bot = telebot.TeleBot(Token) 

@bot.message_handler(commands=['start'])
def start(message): 
    bot.reply_to(message, "Greetings, " + message.from_user.first_name + """!
Type '/help' to get the list of all commands""")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, """/start - Start the bot
/help - Gives the list of all commands
I am a calculator bot. Type in any expression and I will evaluate it for you.""")

@bot.message_handler()
def calc(message):
    try:
        msg = eval(message.text.strip())
    except Exception as e:
        msg = "This cant be evaluated"
    bot.reply_to(message, "The answer is : " + str(msg))

bot.polling()