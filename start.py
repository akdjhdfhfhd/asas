from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""Hᴇʏ {msg.from_user.mention},

Tʜɪs ɪs {me2},
⌯¦مرحبـاً بـك عزيـزي 📬 
⌯¦في بــوت استـخـراج جلـسـة
⌯¦استـخـراج تيرمـكـس تليثون
⌯¦وبــايــروجـرام للـمـيــوزك🎧
- يعمـل هـذا البـوت لمساعدتـك بطريقـة سهلـه للحصـول على كـود تيرمكـس لتشغيل تلـيثون والبايروجرام لتشغيل سـورس اغــاني
تم انشـاء هـذا البـوت بواسطـة: ʙʏ : [بلاكثون](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="🔱 اضغط لبدا استخراج الكود 🔱", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("سورس بلاكثون", url="https://t.me/gibthon7"),
                    InlineKeyboardButton("⚙️ المطور ⚙️", user_id=OWNER_ID)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
