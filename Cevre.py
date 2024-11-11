import discord
from discord.ext import commands

# Bot için gerekli olan tüm yetkileri içeren intents ayarını oluşturuyoruz
intents = discord.Intents.default()
intents.message_content = True  # Mesaj içeriğine erişim izni

# Bot komutlar için ! öneki ile çalışacak
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} olarak giriş yaptım!')

@bot.command(name="su_tasarrufu")
async def su_tasarrufu(ctx):
    """Su tasarrufu hakkında bilgi verir."""
    await ctx.send(
        "💧 Su tasarrufu için bazı öneriler:\n"
        "- Dişlerinizi fırçalarken musluğu kapatın.\n"
        "- Kısa duşlar alın ve duş sürenizi 5 dakikayla sınırlayın.\n"
        "- Sızdıran muslukları ve boruları hemen tamir ettirin."
    )

@bot.command(name="geri_donusum")
async def geri_donusum(ctx):
    """Geri dönüşüm hakkında bilgi verir."""
    await ctx.send(
        "♻️ Geri dönüşüm yaparken dikkat etmeniz gerekenler:\n"
        "- Plastik, cam, kağıt ve metal atıkları ayrı ayrı geri dönüşüm kutularına atın.\n"
        "- Atık elektronik cihazları geri dönüşüm merkezlerine götürün.\n"
        "- Organik atıkları kompost yaparak doğaya geri kazandırın."
    )

@bot.command(name="enerji_tasarrufu")
async def enerji_tasarrufu(ctx):
    """Enerji tasarrufu hakkında bilgi verir."""
    await ctx.send(
        "💡 Enerji tasarrufu için bazı öneriler:\n"
        "- Gereksiz lambaları kapatın ve enerji tasarruflu ampuller kullanın.\n"
        "- Elektronik cihazları kullanılmadığında prizden çekin.\n"
        "- Evinizi yalıtım malzemeleriyle izole ederek enerji kaybını azaltın."
    )
