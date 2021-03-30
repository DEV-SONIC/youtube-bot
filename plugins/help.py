from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"البوت يدعم الروابط فقط ضع الرابط وسيتم تحميل الاغنية."
    await message.reply_text(helptxt)
