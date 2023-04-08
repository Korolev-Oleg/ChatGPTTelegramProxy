
def send_message_to_user_without_access(bot, tg_message, additional_msg=""):
    bot.reply_to(
        tg_message,
        f"Привет! {additional_msg}\n"
        "для доступа к боту напишите @hustncn",
    )
