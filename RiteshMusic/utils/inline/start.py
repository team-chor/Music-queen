#⟶̽ जय श्री ༢།म >𝟑🙏🚩
from pyrogram.types import InlineKeyboardButton, WebAppInfo
import config
from RiteshMusic import app

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?startgroup=true"
            ), 
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT)
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url="https://t.me/TEAM_CHOR"
            )
        ]
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true"
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_10"], user_id=config.OWNER_ID), 
            InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")
        ],

        [
            InlineKeyboardButton(text=_["S_B_9"], url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text=_["S_B_7"], url=config.SUPPORT_CHANNEL)
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], web_app=WebAppInfo(url="https://t.me/DCO_TEAM_1")), 
            InlineKeyboardButton(text=_["S_B_5"], url="https://t.me/TEAM_CHOR")
        ]
    ]
    return buttons
