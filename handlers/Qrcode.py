from io import BytesIO

import qrcode
from aiogram import types, Router
from aiogram.types import BufferedInputFile

from keyboard import kb

Qrcode = Router()


@Qrcode.message()
async def menu_handler_qr(message: types.Message):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(message.text)
    qr.make(fit=True)
    image = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    image.save(buffer, "PNG")
    buffer.seek(0)
    input_file = BufferedInputFile(buffer.getvalue(), filename="qrcode.png")
    await message.answer_photo(photo=input_file, reply_markup=kb)