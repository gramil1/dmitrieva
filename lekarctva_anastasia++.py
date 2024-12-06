import telebot,os 
from telebot import types 
from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))


# Пример списка доступных лекарств 
medicines = { 
    "парацетамол": 100, 
    "ибупрофен": 150, 
    "анальгин": 80 
} 

# Команда /start 
@bot.message_handler(commands=['start']) 
def welcome(message): 
    bot.send_message(message.chat.id, "Добро пожаловать в аптеку! Используйте команду /medicines для просмотра доступных лекарств.") 

# Команда /medicines для просмотра доступных лекарств 
@bot.message_handler(commands=['medicines']) 
def list_medicines(message): 
    response = "Доступные лекарства:\n" 
    for med, price in medicines.items(): 
        response += f"{med.capitalize()}: {price} руб.\n" 
    response += "Выберите лекарство, чтобы сделать заказ." 
    bot.send_message(message.chat.id, response) 

# Обработка заказов 
@bot.message_handler(func=lambda message: message.text.lower() in medicines.keys()) 
def order_medicine(message): 
    medicine = message.text.lower() 
    price = medicines[medicine] 
    bot.send_message(message.chat.id, f"Вы заказали {medicine}. Цена: {price} руб. Для подтверждения отправьте 'Да', для отмены 'Нет'.") 

# Подтверждение заказа 
@bot.message_handler(func=lambda message: message.text.lower() in ['да', 'нет']) 
def confirm_order(message): 
    if message.text.lower() == 'да': 
        bot.send_message(message.chat.id, "Ваш заказ подтвержден! Спасибо за покупку!") 
    else: 
        bot.send_message(message.chat.id, "Ваш заказ отменен.") 

# Запуск бота 
bot.polling(none_stop=True)