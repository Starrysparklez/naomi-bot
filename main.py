from discord.commands import Bot

bot = Bot(command_prefix="n.")

@bot.event
async def on_ready():
  print("Naomi is ready")

@bot.command()
async def stats(ctx):
  await ctx.reply("ну короче бот версии 21.10.09 (1027), питон 3.9 наверное, точно не знаю, ну вот так как-то")

bot.run("MExIUXU5QzQwTDBnMEwzUmd5RFJqZEdDMEw0ZzBMYlF0U.0RSZ3RDKzBMclF0Z.EM5SU5DOTBMRFFzdEMxMFlEUXZkQyswTFVzSU5DMDBMQWdQdz09")
