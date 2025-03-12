from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from config import CHANNEL_LINK
main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Main mune")]
],
        resize_keyboard=True,
        input_field_placeholder="Write smth...")

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="History", callback_data="history_callback")],
    [InlineKeyboardButton(text="Profile", callback_data="profile")],
])

back_to_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Back🔙", callback_data="back")]
])

history_text = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="send it as file", callback_data="send_as_file_history")],
    [InlineKeyboardButton(text="Back🔙", callback_data="back")]
])



profile_settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Show my profile", callback_data="show_users_profliee"), InlineKeyboardButton(text="Create/change profile", callback_data="create_update_profile")],
    [InlineKeyboardButton(text="Back🔙", callback_data="back")]

])

profile_creating = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Create your profile", callback_data="create_update_profile")]
])
def create_markap_kb(name, url):
    if name == "none" or url== "none":
        return None
    ads_channel = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=name, url=url)]
    ])
    return ads_channel