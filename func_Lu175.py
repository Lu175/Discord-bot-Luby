except_cmd_list = ['./draw', './draw 1', './draw 0', './dd', './test', './c_test']


async def get_replied_msg(bot, message=None, context=None):
    if message is not None:
        if (message.reference is not None) and (message.content not in except_cmd_list):
            replied_msg = await bot.get_channel(message.reference.channel_id).fetch_message(message.reference.message_id)
            return replied_msg
        else:
            return None
    elif context is not None:
        if context.message.reference is not None:
            replied_msg = await bot.get_channel(context.message.reference.channel_id).fetch_message(context.message.reference.message_id)
            return replied_msg
        else:
            return None
    else:
        print("Replied message is None.")
        return None


async def get_emoji_url(emoji_id: str, mode=None):
    if mode == 1:  # custom animated emoji
        # https://cdn.discordapp.com/emojis/<Emoji_id>.gif?v=1
        return "https://cdn.discordapp.com/emojis/" + emoji_id + ".gif?v=1"
    elif mode == 2:  # custom non-animated emoji
        # https://cdn.discordapp.com/emojis/<Emoji_id>.png
        return "https://cdn.discordapp.com/emojis/" + emoji_id + ".png"
    elif mode == 3:  # unicode emoji
        # https://twemoji.maxcdn.com/v/latest/72x72/<CODE>.png
        return "https://twemoji.maxcdn.com/v/latest/72x72/" + emoji_id + ".png"
    else:
        print("Replied URL is None.")
        return None


def def_get_emoji_url(emoji_id: str, mode=None):
    if mode == 1:  # custom animated emoji
        # https://cdn.discordapp.com/emojis/<Emoji_id>.gif?v=1
        return "https://cdn.discordapp.com/emojis/" + emoji_id + ".gif?v=1"
    elif mode == 2:  # custom non-animated emoji
        # https://cdn.discordapp.com/emojis/<Emoji_id>.png
        return "https://cdn.discordapp.com/emojis/" + emoji_id + ".png"
    elif mode == 3:  # unicode emoji
        # https://twemoji.maxcdn.com/v/latest/72x72/<CODE>.png
        return "https://twemoji.maxcdn.com/v/latest/72x72/" + emoji_id + ".png"
    else:
        print("Replied URL is None.")
        return None
