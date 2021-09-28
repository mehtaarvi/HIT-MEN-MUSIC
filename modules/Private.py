
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
import signal
import os
import sys

HOME_TEXT = "<b>ʜᴇʏ, [{}](tg://user?id={})\n\n . 𝙃𝙚𝙮 𝙖𝙢 𝙋𝘼𝙍𝙏 𝙤𝙛  ELI MUSICS\n 𝙈𝙚𝙧𝙚 𝙠𝙤 𝙖𝙥𝙣𝙚 𝙜𝙧𝙤𝙪𝙥 𝙢𝙚 𝙖𝙙𝙙 𝙠𝙧𝙤 𝙤𝙧 𝙢𝙪𝙨𝙞𝙘 𝙨𝙪𝙣𝙤. 😜😜\n 👸𝑶𝑾𝑵𝑬𝑹👸=[🇶🆄🄴⃝🄴⃝🇳](https://t.me/ELIANA_072)\n     💗💗❤️❤️❤️💗💗"   


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
                InlineKeyboardButton('⚡𝕮𝖍𝖆𝖓𝖓𝖊𝖑⚡', url='https://t.me/two_birds_one_phone'),
                InlineKeyboardButton('乂❤₲ⱤØɄ₱❤乂', url='https://t.me/two_birds_one_phone')
                ],[
                InlineKeyboardButton('👸🇪🅻🅸👸', url='https://t.me/Eliana_072'),
                InlineKeyboardButton('👸🇦🆁🆅🅸👸', url='https://t.me/FOREVER_ANGEL_0')
                ],[
                InlineKeyboardButton('║█🇦𝑫𝑫 🇲𝑬 🇹𝑶 🇾𝑶𝑼𝑹 🇬𝑹𝑶𝑼𝑷█║', url=f'https://t.me/ELI_MUSIC_BOT?startgroup=true'),
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo="https://telegra.ph/file/423ff17409df6b72ca08a.jpg", caption=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await message.delete()


@Client.on_message(filters.command("help"))
async def show_help(client, message):
    buttons = [
        [
                InlineKeyboardButton('⚡𝕮𝖍𝖆𝖓𝖓𝖊𝖑⚡', url='https://t.me/two_birds_one_phone'),
                InlineKeyboardButton('乂❤₲ⱤØɄ₱❤乂', url='https://t.me/two_birds_one_phone')
                ],[
                InlineKeyboardButton('👸🇪🅻🅸👸', url='https://t.me/Eliana_072'),
                InlineKeyboardButton('👸🇦🆁🆅🅸👸', url='https://t.me/FOREVER_ANGEL_0')
                ],[
                InlineKeyboardButton('║█🇦𝑫𝑫 🇲𝑬 🇹𝑶 🇾𝑶𝑼𝑹 🇬𝑹𝑶𝑼𝑷█║', url=f'https://t.me/ELI_MUSIC_BOT?startgroup=true'),
       ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo="https://telegra.ph/file/423ff17409df6b72ca08a.jpg", caption=HELP, reply_markup=reply_markup)
    await message.delete()
