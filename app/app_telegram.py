from vanna_setup import vn
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from config import settings

bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Я помощник по ГИА. Задай мне вопрос. Вот примеры:\n"
                         "«Тут должен быть пример)»")


@dp.message()
async def handle_question(message: types.Message):
    question = message.text
    try:
        # Генерируем SQL с помощью Vanna
        sql = vn.generate_sql(question=question)

        # Выполняем запрос
        results = vn.run_sql(sql=sql)

        # Форматируем ответ
        response = (
            f"🔍 <b>Ваш запрос:</b> <i>{question}</i>\n\n"
            f"📝 <b>SQL:</b>\n<code>{sql}</code>\n\n"
            f"📊 <b>Результат:</b>\n{results}"
        )

        await message.answer(response, parse_mode="HTML")

    except Exception as e:
        await message.answer(f"❌ Ошибка:\n {str(e)}")


if __name__ == "__main__":
    dp.run_polling(bot)
