from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Telegram username"),
            KeyboardButton(text="QRcode")
        ]
    ],resize_keyboard=True
)
kb2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Orqaga")
        ]
    ],resize_keyboard=True
)