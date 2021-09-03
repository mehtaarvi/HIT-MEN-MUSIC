
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
import signal
import os
import sys


HOME_TEXT = "<b>Helo, [{}](tg://user?id={})\n\n• Iam A Bot Project by @TGBOTZXD\n• I Can Manage Group VC's\n\n• Hit /help to know about available commands.</b>"
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
[ __@tgbotsXD || @tgbotzXD__ ]
"""



@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
       [
                InlineKeyboardButton('📢 Updates', url='https://t.me/TGBOTZXD'),
                InlineKeyboardButton('💬 Support', url='https://t.me/TGBOTSXD')
                ],[
                InlineKeyboardButton('🤖 Developer', url='https://t.me/piroXpower'),
                InlineKeyboardButton('🎧 Chats', url='https://t.me/frndsXworld')
                ],[
                InlineKeyboardButton('📜 Source Code 📜', url='https://github.com/TEAM-PATRICIA/PatriciaMusic2.0'),
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo="https://telegra.ph/file/33cc1aeaf934f19943bdc.jpg", caption=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await message.delete()


@Client.on_message(filters.command("help"))
async def show_help(client, message):
    buttons = [
        [
                InlineKeyboardButton('📢 Updates', url='https://t.me/TGBOTZXD'),
                InlineKeyboardButton('💬 Support', url='https://t.me/TGBOTSXD')
                ],[
                InlineKeyboardButton('🤖 Developer', url='https://t.me/piroXpower'),
                InlineKeyboardButton('🎧 Chats', url='https://t.me/frndsXworld')
                ],[
                InlineKeyboardButton('📜 Source Code 📜', url='https://github.com/TEAM-PATRICIA/PatriciaMusic2.0'),
       ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo="https://telegra.ph/file/33cc1aeaf934f19943bdc.jpg", caption=HELP, reply_markup=reply_markup)
    await message.delete()
