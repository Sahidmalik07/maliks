#sahid malik
from info import MAINTENANCE_MODE, AUTH_USERS
from pyrogram import Client, filters, enums 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton





@Client.on_message(filters.text & filters.private & filters.incoming)
async def give_filter(client, message):
    if MAINTENANCE_MODE:
        if AUTH_USERS and message.from_user and message.from_user.id in AUTH_USERS:
            k = await manual_filters(client, message)
            if k == False:
                await auto_filter(client, message)
        else:
            await message.reply_text(f"ð°ð¡ð¢ð§ðððð°\n\nService is ððð ð¤ðð for ð® ðð²ð²ð¸ð.\nwill start again by <u>next month.</u>.\n\nð¡ð ðððð ðððð¾, ð¬ðºðð¾ ðððð¾ <b>you have ððð»ðð¼ððð»ð¾ð½ CINEMA HUB groupðð»</b>", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("ð¶ Back to Group ð¶",url="https://t.me/+FAgX05kGByNkZjJl"),]]),parse_mode=enums.ParseMode.HTML)#"You are now verified for next 24 hours. Continue asking movies")      

    else:
        k = await manual_filters(client, message)
        if k == False:
            await auto_filter(client, message)

