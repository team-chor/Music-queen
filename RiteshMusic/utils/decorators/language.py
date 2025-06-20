#⟶̽ जय श्री ༢།म >𝟑🙏🚩
import logging
from RiteshMusic.misc import SUDOERS
from RiteshMusic.utils.database import get_lang, is_maintenance
from config import SUPPORT_CHAT
from strings import get_string
from RiteshMusic import app

# Setup logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Safe fallback to English
def safe_get_string(lang_code):
    try:
        return get_string(lang_code)
    except Exception as e:
        logger.warning(f"Failed to load language string for {lang_code}: {e}")
        return get_string("en")


def language(mystic):
    async def wrapper(_, message, **kwargs):
        try:
            if await is_maintenance() is False and message.from_user.id not in SUDOERS:
                return await message.reply_text(
                    text=f"{app.mention} ɪs ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ, ᴠɪsɪᴛ <a href={SUPPORT_CHAT}>sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ</a> ғᴏʀ ᴋɴᴏᴡɪɴɢ ᴛʜᴇ ʀᴇᴀsᴏɴ.",
                    disable_web_page_preview=True,
                )
        except Exception as e:
            logger.error(f"Maintenance check failed: {e}")

        try:
            await message.delete()
        except Exception as e:
            logger.debug(f"Failed to delete user message: {e}")

        try:
            lang_code = await get_lang(message.chat.id)
        except Exception as e:
            logger.warning(f"Failed to fetch language from DB: {e}")
            lang_code = "en"

        language = safe_get_string(lang_code)

        try:
            return await mystic(_, message, language)
        except Exception as e:
            logger.exception(f"Error in wrapped language function: {e}")
            return await message.reply_text("⚠️ Something went wrong. Please try again later.")

    return wrapper


def languageCB(mystic):
    async def wrapper(_, CallbackQuery, **kwargs):
        try:
            if await is_maintenance() is False and CallbackQuery.from_user.id not in SUDOERS:
                return await CallbackQuery.answer(
                    f"{app.mention} ɪs ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ. ᴘʟᴇᴀsᴇ ᴄʜᴇᴄᴋ {SUPPORT_CHAT}.",
                    show_alert=True,
                )
        except Exception as e:
            logger.error(f"Maintenance check failed in callback: {e}")

        try:
            lang_code = await get_lang(CallbackQuery.message.chat.id)
        except Exception as e:
            logger.warning(f"Failed to fetch language from DB (CB): {e}")
            lang_code = "en"

        language = safe_get_string(lang_code)

        try:
            return await mystic(_, CallbackQuery, language)
        except Exception as e:
            logger.exception(f"Error in wrapped languageCB function: {e}")
            return await CallbackQuery.answer("⚠️ Something went wrong. Please try again later.", show_alert=True)

    return wrapper


def LanguageStart(mystic):
    async def wrapper(_, message, **kwargs):
        try:
            lang_code = await get_lang(message.chat.id)
        except Exception as e:
            logger.warning(f"Failed to fetch language from DB (start): {e}")
            lang_code = "en"

        language = safe_get_string(lang_code)

        try:
            return await mystic(_, message, language)
        except Exception as e:
            logger.exception(f"Error in wrapped LanguageStart function: {e}")
            return await message.reply_text("⚠️ An unexpected error occurred during startup.")

    return wrapper
