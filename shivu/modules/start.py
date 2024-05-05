import random
from html import escape 

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CallbackQueryHandler, CommandHandler

from shivu import application, PHOTO_URL, SUPPORT_CHAT, UPDATE_CHAT, BOT_USERNAME, db, GROUP_ID
from shivu import pm_users as collection 


async def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    first_name = update.effective_user.first_name
    username = update.effective_user.username

    user_data = await collection.find_one({"_id": user_id})

    if user_data is None:
        
        await collection.insert_one({"_id": user_id, "first_name": first_name, "username": username})
        
        await context.bot.send_message(chat_id=GROUP_ID, 
                                       text=f"New user Started The Bot..\n User: <a href='tg://user?id={user_id}'>{escape(first_name)})</a>", 
                                       parse_mode='HTML')
    else:
        
        if user_data['first_name'] != first_name or user_data['username'] != username:
            
            await collection.update_one({"_id": user_id}, {"$set": {"first_name": first_name, "username": username}})

    

    if update.effective_chat.type== "private":
        
        
        caption = f"""
        🌙 ɢʀᴇᴇᴛɪɴɢs ʏᴏᴜ ,
ɪ'ᴍ ˹ᴡᴀɪғᴜ ᴀᴛᴛᴀɪɴᴇʀ ʙᴏᴛ˼🔮 ,
 ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ!
▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰
⌥ ᴡʜᴀᴛ ᴄᴀɴ ɪ ᴅᴏ ?
▸ ɪ ᴄᴀɴ sᴘᴀᴡɴ ᴡᴀɪғᴜs ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴄʜᴀᴛs ғᴏʀ ɢʀᴏᴜᴘ ᴄʜᴀᴛ ᴜsᴇʀs ᴛᴏ ᴀᴛᴛᴀɪɴ ᴛʜᴇᴍ.

⌥ ʜᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ?
▸ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴄʜᴀᴛs ᴀɴᴅ ᴄʟɪᴄᴋ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ғᴏʀ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟs.💍
▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰  """
        
        keyboard = [
            [InlineKeyboardButton("ɪɴᴠɪᴛᴇ ᴍᴇ", url=f'http://t.me/{BOT_USERNAME}?startgroup=new')],
            [InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=f'https://t.me/{SUPPORT_CHAT}'),
            InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url=f'https://t.me/{UPDATE_CHAT}')],
            [InlineKeyboardButton("ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs", callback_data='help')],
            [InlineKeyboardButton("ɢʜᴏsᴛ", url=f'https://t.me/Bang_Brave_Bang_Bravern')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        photo_url = random.choice(PHOTO_URL)

        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url, caption=caption, reply_markup=reply_markup, parse_mode='markdown')

    else:
        photo_url = random.choice(PHOTO_URL)
        keyboard = [
            [InlineKeyboardButton("ɪɴᴠɪᴛᴇ ᴍᴇ", url=f'http://t.me/{BOT_USERNAME}?startgroup=new')],
            [InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=f'https://t.me/{SUPPORT_CHAT}'),
            InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url=f'https://t.me/{UPDATE_CHAT}')],
            [InlineKeyboardButton("ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs", callback_data='help')],
            [InlineKeyboardButton("SOURCE", url=f'https://t.me/Bang_Brave_Bang_Bravern')]
        ]
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url, caption="ᴀʟɪᴠᴇ?🔮 \n ᴄᴏɴɴᴇᴄᴛ ᴛᴏ ᴍʏ ᴘᴍ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ",reply_markup=reply_markup )

async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'help':
        help_text = """
    ***Help Section:***
    
***/attain: ᴛᴏ ᴏʙᴛᴀɪɴ ᴡᴀɪғᴜ*
***/fav: ᴀᴅs ʏᴏᴜʀ ғᴀᴠ ᴡᴀɪғᴜ*
***/trade : ᴛᴏ ᴛʀᴀᴅᴇ ʏᴏᴜʀ ᴡᴀɪғᴜ*
***/gift: ᴛᴏ ɢɪғᴛ ᴀɴʏ ᴡᴀɪғᴜ ᴛᴏ ᴀɴʏʙᴏᴅʏ*
***/harem: ᴛᴏ sᴇᴇ ʏᴏᴜʀ ʜᴀʀᴇᴍs*
***/topgroups : sᴇ ᴛᴏᴘ ɢʀᴏᴜᴘs.. ᴘᴘʟ ᴏʙᴛᴀɪɴs ᴍᴏsᴛ ɪɴ ᴛʜᴀᴛ ɢʀᴏᴜᴘ*
***/top: ᴛᴏᴏ sᴇᴇ ᴛᴏᴘ ᴜsᴇʀs*
***/ctop : ʏᴏᴜʀ ᴄʜᴀᴛᴛᴏᴘ*
***/changetime: ᴛᴏ ᴄʜᴀɴɢᴇ ᴛɪᴍᴇ ᴡʜᴇᴍ ᴡᴀɪғᴜ ᴀᴘᴘᴇᴀʀ*
   """
        help_keyboard = [[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data='back')]]
        reply_markup = InlineKeyboardMarkup(help_keyboard)
        
        await context.bot.edit_message_caption(chat_id=update.effective_chat.id, message_id=query.message.message_id, caption=help_text, reply_markup=reply_markup, parse_mode='markdown')

    elif query.data == 'back':

        caption = f"""
        🌙 ɢʀᴇᴇᴛɪɴɢs ʏᴏᴜ ,
ɪ'ᴍ ˹ᴡᴀɪғᴜ ᴀᴛᴛᴀɪɴᴇʀ ʙᴏᴛ˼🔮 ,
 ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ!
▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰
⌥ ᴡʜᴀᴛ ᴄᴀɴ ɪ ᴅᴏ ?
▸ ɪ ᴄᴀɴ sᴘᴀᴡɴ ᴡᴀɪғᴜs ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴄʜᴀᴛs ғᴏʀ ɢʀᴏᴜᴘ ᴄʜᴀᴛ ᴜsᴇʀs ᴛᴏ ᴀᴛᴛᴀɪɴ ᴛʜᴇᴍ.

⌥ ʜᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ?
▸ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴄʜᴀᴛs ᴀɴᴅ ᴄʟɪᴄᴋ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ғᴏʀ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟs.💍
▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰ """

        
        keyboard = [
            [InlineKeyboardButton("ɪɴᴠɪᴛᴇ ᴍᴇ", url=f'http://t.me/{BOT_USERNAME}?startgroup=new')],
            [InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=f'https://t.me/{SUPPORT_CHAT}'),
            InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇs", url=f'https://t.me/{UPDATE_CHAT}')],
            [InlineKeyboardButton("ʜᴇʟᴘ", callback_data='help')],
            [InlineKeyboardButton("ɢʜᴏsᴛ", url=f'https://t.me/Bang_Brave_Bang_Bravern')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await context.bot.edit_message_caption(chat_id=update.effective_chat.id, message_id=query.message.message_id, caption=caption, reply_markup=reply_markup, parse_mode='markdown')


application.add_handler(CallbackQueryHandler(button, pattern='^help$|^back$', block=False))
start_handler = CommandHandler('start', start, block=False)
application.add_handler(start_handler)
