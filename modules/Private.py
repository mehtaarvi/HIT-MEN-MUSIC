
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
import signal
import os
import sys

HOME_TEXT = "<b>ʜᴇʏ, [{}](tg://user?id={})\n\n• 𝙃𝙚𝙮 𝙖𝙢 𝙋𝘼𝙍𝙏 𝙤𝙛  𝑨𝑹𝑽𝑰 𝑴𝑼𝑺𝑰𝑪 𝑩𝑶𝑻.🇮 🇨𝙖𝙣  🇵𝙡𝙖𝙮  🇲𝙪𝙨𝙞𝙘 𝙄𝙣  🇾𝙤𝙪𝙧  🇬𝙧𝙤𝙪𝙥 ["𝙊𝙬𝙣𝙚𝙧 𝙌𝙪𝙚𝙚𝙣"]("https://t.me/FOREVER_ANGEL_0")• '𝙸 𝙲𝙰𝙽 𝙼𝙰𝙽𝙰𝙶𝙴 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿'𝚜 𝚅𝙲 ʜɪᴛ s/n/n. ᎫϴᏆΝ  ϴᏔᎡ  ᏀᎡϴႮᏢ  ҒϴᎡ ᏟᎻᎪͲ {

["𝗟𝗜𝗡𝗞"]("https://t.me/world_wide_chattt")s.</b>"
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
[ __@world_wide_chattt || @world_wide_chattt__ ]
"""



@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
       [
                InlineKeyboardButton('𓆩ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ𓆪', url='https://t.me/HITmenMusicBot?startgroup=true'),
                InlineKeyboardButton('𓆩ɢʀᴏᴜᴘ𓆪', url='https://t.me/mnvvcxz123456777')
                ],[
                InlineKeyboardButton('𓆩ᴄʜᴀɴɴᴇʟ𓆪', url='https://t.me/DARKAMANCHANNEL'),
                InlineKeyboardButton('𓆩ʜɪᴛ ᴍᴀɴ𓆪', url='https://t.me/VICTOR_2K21')
                ],[
                InlineKeyboardButton('𓆩ᴄᴏᴍᴍᴀɴᴅs𓆪', url='http://telegra.ph/𝕄𝔼ℕ-09-18'),
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo="https://telegra.ph/file/3bbc2fa668424bdb7c894.jpg", caption=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await message.delete()


@Client.on_message(filters.command("help"))
async def show_help(client, message):
    buttons = [
        [
                InlineKeyboardButton('𓆩ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ𓆪', url='https://t.me/HITmenMusicBot?startgroup=true'),
                InlineKeyboardButton('𓆩ɢʀᴏᴜᴘ𓆪', url='https://t.me/mnvvcxz123456777')
                ],[
                InlineKeyboardButton('𓆩ᴄʜᴀɴɴᴇʟ𓆪', url='https://DARKAMANCHANNEL'),
                InlineKeyboardButton('𓆩ʜɪᴛ ᴍᴀɴ𓆪', url='https://t.me/VICTOR_2K21')
                ],[
                InlineKeyboardButton('𓆩ᴄᴏᴍᴍᴀɴᴅs𓆪', url='http://telegra.ph/𝕄𝔼ℕ-09-18'),
       ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo="https://telegra.ph/file/3bbc2fa668424bdb7c894.jpg", caption=HELP, reply_markup=reply_markup)
    await message.delete()
