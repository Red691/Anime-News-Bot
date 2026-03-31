import os

API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
OWNER_ID = int(os.environ.get("OWNER_ID", "5770911041"))
ADMIN_ID = int(os.environ.get("ADMIN_ID", "5770911041"))
LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1003209904648")
UPDATE_INTERVAL = int(os.environ.get("UPDATE_INTERVAL", "5")) # minutes
PORT = int(os.environ.get("PORT", "8080")) # for web health checks
DB_NAME = "anime_news"
DB_URL = os.environ.get("DB_URL")

if not DB_URL:
    raise ValueError("DB_URL missing in environment")
START_MSG = os.environ.get("START_MSG", "Bᴀᴋᴀᴀᴀᴀ {mention}... \n<blockquote><b>Iᴀᴍ ᴀ ᴀᴅᴠᴀɴᴄᴇ Aᴜᴛᴏ ᴀɴɪᴍᴇ ɴᴇᴡs Bᴏᴛ ᴡʜɪᴄʜ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴜᴘʟᴏᴀᴅs ᴛʜᴇ ʟᴀᴛᴇsᴛ ᴀɴɪᴍᴇ ɴᴇᴡs ɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ.</b></blockquote>")
HELP_MSG = os.environ.get("HELP_MSG", "<b><u>Hᴇʀᴇ ᴍʏ Cᴏᴍᴍᴀɴᴅs</u></b>:- \n\n<blockquote>• /add_rss - ᴛᴏ ᴀᴅᴅ ɴᴇᴡ ғᴇᴇᴅ (Mᴀx 2 ᴀᴛ ᴏɴᴄᴇ) \n• /rem_rss - ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴀɴʏ ʀss ғᴇᴇᴅ. \n• /view_rss - ᴛᴏ ᴠɪᴇᴡ ᴀᴅᴅᴇᴅ ʀss ғᴇᴇᴅs. \n• /add_chnl - ʀᴏᴜᴛᴇ ɴᴇᴡs ᴛᴏ ᴄʜᴀɴɴᴇʟ. \n• /rem_chnl  : Rᴇᴍᴏᴠᴇ ᴄʜᴀɴɴᴇʟ ʀᴏᴜᴛᴇ. \n•/view_chnl : ᴛᴏ ᴠɪᴇᴡ ᴀᴄᴛɪᴠᴇ ᴄʜᴀɴɴᴇʟ ʀᴏᴜᴛᴇs. \n•/status : ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ʙᴏᴛ sᴛᴀᴛᴜs.</blockquote>")
ABOUT_MSG = os.environ.get("ABOUT_MSG", "<i><b><blockquote>◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/Anime_sensei_officia>Anime sensei officia</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/Anime_sensei_officia>Anime sensei official</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href='https://t.me/about'>Nova</a>\n◈ ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>ᴍᴏɴɢᴏ ᴅʙ</a>\n» ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href='https://t.me/about'>Nova</a></blockquote></b></i>")
START_PIC = os.environ.get("START_PIC", "https://ibb.co/mVkSySr7")
HELP_PIC = os.environ.get("HELP_PIC", "https://ibb.co/mVkSySr7")
ABOUT_PIC = os.environ.get("ABOUT_PIC", "https://ibb.co/mVkSySr7")
CHNL_USERNAME = "@Anime_News_india_official"
