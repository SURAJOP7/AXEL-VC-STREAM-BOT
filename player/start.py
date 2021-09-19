from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup 

@Client.on_message(filters.command("start"))
async def start(client, m: Message):
   if m.chat.type == 'private':
       await m.reply(f"**Hey, I'm a VC Video Player developed by Developers of** @suraj_o_p_ \n\n**To use it:-** __ \n1) Add this Bot to your Group and Make it Admin \n2) Add__ @SURAJ_O_P_MUSICBOT __to your Group__ \n3) **Commands** : \n`/stream` (IN REPLY TO A VIDEO) \n`/stop`",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                     InlineKeyboardButton(
                                            "Support", url="t.me/AXEL_SUPPORT")
                                    ]]
                            ))
   else:
      await m.reply("**AXEL-VCSTREAM BOT is Alive! ✨**")
