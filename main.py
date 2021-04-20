# LESSON: https://thecode.media/python-bot/
#  Congratulations on your new bot. You will find it at t.me/Natalia_tests_bot
# TELEGRAM BOT API DESCRIPTION: https://core.telegram.org/bots/api

# examples: https://codeby.net/threads/proshu-pomoschi-v-napisanii-telegram-bota-na-python.68099/
# examples: https://habr.com/ru/post/442800/

# TO ALLOW OUR CODE TO CONTROL TELEGRAM BOT WE IMPORT THIS PACKAGE:
import telebot
import datetime

# BOT USERNAME:
bot_name = "Natalia_Bot"
bot_username = "Natalia_tests_bot"

# TOKEN FOR BOT CONTROL:
HTTP_API_TOKEN = ""

bot = telebot.TeleBot(HTTP_API_TOKEN)


# VARIABLES FOR ANSWERS:
name = " "
answer_1 = " "
answer_2 = " "
answer_3 = " "

# VARIABLES FOR QUESTIONS:
name_question = "What is your name?"
question_1 = "1. How are you feeling today?"
question_2 = "2. How did you start your day?"
question_3 = "3. Are you happy with your Python code?"

# DEFINING A METHOD FOR TEXT MESSAGES CREATING:
# content_types = what is the type of messages (can be content_types=['text', 'document', 'audio'])
@bot.message_handler(content_types=["text"])
def send_text(message):
    if message.text.lower() == "hello":
        bot.send_message(message.from_user.id, "Hello! I'm a bot and I'm glad to send you TEST questions!")
        bot.send_message(message.from_user.id, "To start TEST please enter: 'start test'")
    elif message.text.lower() == "bye":
        bot.send_message(message.from_user.id, "Bye, thank you for working with me!")

    elif message.text.lower() == "start test":
        bot.send_message(message.from_user.id, name_question)
        bot.register_next_step_handler(message, get_name)

    elif message.text.lower() == "send":
        with open(f"name.txt", mode="w") as new_file:
            new_file.write(f"Today's date is: {datetime.datetime.now()}\n"
                           f"{name_question}: {name}\n"
                           f"{question_1}: {answer_1}\n"
                           f"{question_2}: {answer_2}\n"
                           f"{question_3}: {answer_3}")

        bot.send_message(message.from_user.id, "Thank you for your answers! See you tomorrow!")

    elif message.text.lower() == "repeat test":
        bot.send_message(message.from_user.id, name_question)
        bot.register_next_step_handler(message, get_name)

    else:
        bot.send_message(message.from_user.id, "Enter: 'start test'")


def get_name(message):
    global name
    name = message.text
    print(name)
    bot.send_message(message.from_user.id, question_1)
    bot.register_next_step_handler(message, first_question)


def first_question(message):
    global answer_1
    answer_1 = message.text
    print(answer_1)
    bot.send_message(message.from_user.id, question_2)
    bot.register_next_step_handler(message, second_question)


def second_question(message):
    global answer_2
    answer_2 = message.text
    print(answer_2)
    bot.send_message(message.from_user.id, question_3)
    bot.register_next_step_handler(message, third_question)


def third_question(message):
    global answer_3
    answer_3 = message.text
    print(answer_3)
    bot.send_message(message.from_user.id, f"Let's check your answers:\n Your name: {name}.\n"
                                           f"{question_1} Your answer: {answer_1}. \n"
                                           f"{question_2} Your answer: {answer_2}\n"
                                           f"{question_3} Your answer: {answer_3}")
    bot.send_message(message.from_user.id, "To confirm answers enter: 'send',\n "
                                           "To repeat test again enter: 'repeat test'")


bot.polling(none_stop=True, interval=0)

