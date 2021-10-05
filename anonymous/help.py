import random
from pyrogram import Client, filters


# Help Message
@Client.on_message(filters.private & filters.command(["help"]))
async def _help(_, msg):
	await msg.reply_message("Send your message i will remove sender tag then u can Forward to others😇")
