import telebot
from config import keys, TOKEN
from extensions import APIException, get_price

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])  # обработчик показывает инструкции
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате: \n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты>\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])  # обработчик показывает все доступные валюты
def values(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

    @bot.message_handler(content_types=['text', ])
    def convert(message: telebot.types.Message):
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('слишком много параментров')

    quote, base, amount = values
    total_base = CryptoConvertor.convert(quote, base,amount)
    text = f'Цена {amount} {quote} в {base} - {total_base}'
    bot.send_message(message.chat.id, text)


bot.polling()
