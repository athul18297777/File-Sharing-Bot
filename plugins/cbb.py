#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ 𝘾𝙧𝙚𝙖𝙩𝙤𝙧 : <a href='tg://user?id={1285659199}'>[𝘼𝙩𝙝𝙪𝙡](https://t.me/athulx80)</a>\n○ 𝙇𝙖𝙣𝙜𝙪𝙖𝙜𝙚 : <code>Python3</code>\n○ 𝙇𝙞𝙗𝙧𝙖𝙧𝙮 : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ 𝙎𝙤𝙪𝙧𝙘𝙚 𝘾𝙤𝙙𝙚 : <a href='https://github.com/athul18297777/File-Sharing-Bot'>𝘾𝙡𝙞𝙘𝙠 𝙃𝙚𝙧𝙚</a>\n○ 𝘾𝙝𝙖𝙣𝙣𝙚𝙡 : @newallmoviesx\n○ 𝙎𝙪𝙥𝙥𝙤𝙧𝙩 𝙂𝙧𝙤𝙪𝙥 : @newallmoviesxgroup</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 𝘾𝙡𝙤𝙨𝙚", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
