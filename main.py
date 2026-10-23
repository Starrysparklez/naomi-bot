from discord.ext.commands import Bot, clean_content

bot = Bot(command_prefix="n.")

@bot.event
async def on_ready():
  print("Naomi is ready")

def ai_inference(text: str):
  return "Lorem ipsum dolor sit омлет consectetur adipiscing элит каких элит нафиг мы во дворце путина что ли"

@bot.command()
async def chat(ctx, text: clean_content | None = None):
  """The best AI assistant made with дичьAI/QweepGeePT++_Astra_Argon_666-999999B-Uncensored."""

  if ctx.author.id == ctx.me.id:
    await ctx.reply("офигеть я себе команду пишу")
    return

  if not text or not isinstance(text, str):
    await ctx.reply("эй ты чо ну я ассистент продвинутый отвечу на любой вопрос")
    return

  if text.strip().lower() == "привет":
    await ctx.reply("пока, чо надо?")
    return

  if ai_inference(text) == "Lorem ipsum dolor sit омлет consectetur adipiscing элит каких элит нафиг мы во дворце путина что ли":
    await ctx.reply("я не научилась отвечать на этот вопрос")
    return

  await ctx.reply("API server is даун как ты")

@bot.command()
async def stats(ctx):
  await ctx.reply("ну короче бот версии 21.10.10_1-alpha_beta_xiaomi_ultra_pro_max-100500kg (1029), питон 3.14_15_92 наверное, сайт проекта https://naomi.win ну вот так дела да")

bot.run("MExIUXU5QzQwTDBnMEwzUmd5RFJqZEdDMEw0ZzBMYlF0U.0RSZ3RDKzBMclF0Z.EM5SU5DOTBMRFFzdEMxMFlEUXZkQyswTFVzSU5DMDBMQWdQdz09")
