from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Полезная информация"),
            types.BotCommand("info", "О нас"),
            types.BotCommand("quit", "Выход")
        ]
    )