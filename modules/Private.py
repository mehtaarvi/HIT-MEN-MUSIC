
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
import signal
import os
import sys

HOME_TEXT = "<b>ʜᴇʏ, [{}](tg://user?id={})\n\n• ɪ'ᴍ 𓆩ᴀᴍᴀɴ ɢᴜᴊᴊᴀʀ ᴍᴜs̶ɪᴄ𓆪 ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ʏᴏᴜʀ ᴏᴘ ɢʀᴏᴜᴘ ᴅᴇᴠᴇʟᴏᴩᴇᴅ ʙʏ @DARKAMAN\n• ɪ ᴄᴀɴ ᴍᴀɴᴀɢᴇ ᴠᴄ's\n\n• ʜɪᴛ /ʜᴇʟᴘ ᴛᴏ ᴋɴᴏᴡ ᴀʙᴏᴜᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs.</b>"
HELP = """
🎧 <b>I Can Play Musics On VoiceChats 🤪</b>

🎶 **Common Commands**:
• `/song` __Download Song from youtube__
• `/play`  __Play song you requested__
• `/help` __Show help for commands__
• `/dplay` __Play song you requested via deezer__
• `splay` __Play song you requested via jio saavn__
• `/ytplay` __Play song directly from youtube server__
• `/search` __Search video songs links__
• `/current` __Show now playing__
• `/playlist` __Show now playing list__
• `/video` __Downloads video song quickly__
🎶 **Admin Commands**:
• `/player`  __Open music player settings panel__
• `/pause` __Pause song play__
• `/skip` __Skip next song__
• `/resume`  __Resume song play__
• `/userbotjoin`  __Invites assistant to your chat__
• `/end` __Stops music play__
• `/admincache` __Refresh list of admins with vc power__
© Powered By 
[ __@DARKAMANSUPPORT || @DARKAMANSUPPORT__ ]
"""



@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
       [
                InlineKeyboardButton('𓆩ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ𓆪', url='https://t.me/{}'),
                InlineKeyboardButton('𓆩ɢʀᴏᴜᴘ𓆪', url='https://t.me/DARKAMANSUPPORT')
                ],[
                InlineKeyboardButton('𓆩ᴄʜᴀɴɴᴇʟ𓆪', url='https://t.me/DARKAMANCHANNEL'),
                InlineKeyboardButton('𓆩ᴅᴀʀᴋᴀᴍᴀɴ𓆪', url='https://t.me/DARKAMAN')
                ],[
                InlineKeyboardButton('𓆩ᴄᴏᴍᴍᴀɴᴅs𓆪', url='https://telegra.ph/𖣔ᴀᴍᴀɴ-ɢᴜᴊᴊᴀʀ-ᴍᴜsɪᴄ-08-31'),
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo="https://telegra.ph/file/221de501e2f547a6359dd.jpg", caption=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await message.delete()


@Client.on_message(filters.command("help"))
async def show_help(client, message):
    buttons = [
        [
                InlineKeyboardButton('𓆩ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ𓆪', url='{}'),
                InlineKeyboardButton('𓆩ɢʀᴏᴜᴘ𓆪', url='https://t.me/DARKAMANSUPPORT')
                ],[
                InlineKeyboardButton('𓆩ᴄʜᴀɴɴᴇʟ𓆪', url='https://DARKAMANCHANNEL'),
                InlineKeyboardButton('𓆩ᴅᴀʀᴋᴀᴍᴀɴ𓆪', url='https://t.me/DARKAMAN')
                ],[
                InlineKeyboardButton('𓆩ᴄᴏᴍᴍᴀɴᴅs𓆪', url='https://telegra.ph/𖣔ᴀᴍᴀɴ-ɢᴜᴊᴊᴀʀ-ᴍᴜsɪᴄ-08-31'),
       ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo="https://telegra.ph/file/221de501e2f547a6359dd.jpg", caption=HELP, reply_markup=reply_markup)
    await message.delete()
