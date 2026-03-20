import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = '8690689893:AAG7rrR0T2ZPwBRjnTgPYVngp5Jn4IUhUw4'
ADMIN_ID = 731814302

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="📩 Написать сообщение")]],
    resize_keyboard=True
)

user_states = {}

@dp.message()
async def handle_message(message: types.Message):
    if message.text == "/start":
        await message.answer(
    "👋 Здравствуйте!\n\n"
    "Вы обратились в анонимный бот\n"
    "Западно-Казахстанского медицинского университета\n"
    "имени Марата Оспанова.\n\n"
    
    "📌 Бот создан профсоюзным комитетом студентов\n"
    "для обратной связи.\n\n"
    
    "Здесь вы можете анонимно отправить:\n"
    "• жалобы\n"
    "• предложения\n"
    "• идеи\n\n"
    
    "🔒 Ваша анонимность полностью сохраняется.\n\n"
    "👇 Нажмите кнопку ниже, чтобы написать сообщение",
    reply_markup=keyboard
)

    elif message.text == "📩 Написать сообщение":
        user_states[message.from_user.id] = True
        await message.answer("Напишите сообщение:")

    elif message.from_user.id == ADMIN_ID:
        if message.reply_to_message:
            user_id = int(message.reply_to_message.text.split("ID:")[1])
            await bot.send_message(user_id, f"📨 Ответ:\n\n{message.text}")

    else:
        if user_states.get(message.from_user.id):
            await bot.send_message(
                ADMIN_ID,
                f"📩 Новое сообщение:\n\n{message.text}\n\nID:{message.from_user.id}"
            )
            await message.answer("✅ Отправлено")
            user_states[message.from_user.id] = False

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
