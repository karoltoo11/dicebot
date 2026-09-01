import os
import random
import discord
from discord import app_commands
from discord.ext import commands
from typing import Optional, List

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

GUILD_ID = os.getenv("DISCORD_GUILD_ID", "").strip()
if GUILD_ID:
    try:
        GUILD_ID = int(GUILD_ID)
    except ValueError:
        GUILD_ID = None

TOKEN = os.getenv("DISCORD_TOKEN", "").strip()

class diceBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=discord.Intents.default(),
            activity=discord.Game(name="Rolling dice"),
            status=discord.Status.online,
        )

    async def setup_hook(self):
        if GUILD_ID:
            guild = discord.Object(id=GUILD_ID)
            await self.tree.sync(guild=guild)
            print(f"Logged in as {self.user} | Commands synchronized on server {GUILD_ID}.")
        else:
            await self.tree.sync()
            print(f"Logged in as {self.user} | Commands synchronized globally.")

bot = diceBot()

@bot.tree.command(name="help", description="Information about the bot and its creators.")
async def help_command(interaction: discord.Interaction):
    embed = discord.Embed(title="🎲 Information Dicebot", color=discord.Color.red())
    embed.add_field(name="Commands", value=(
        "`/d2` - A roll of a two-sided die..\n"
        "`/d4` - A roll of a four-sided die.\n"
        "`/d6` - A roll of a six-sided die.\n"
        "`/d10` - A roll of a ten-sided die.\n"
        "`/d20` - A roll of a twenty-sided die.\n"
        "`/d100` - A roll of a hundred-sided die.\n"
        "`/roll <number>` - A roll with a custom number of sides.\n"
    ), inline=False)
    embed.add_field(name="Blockades", value="The last command allows only natural numbers to be entered.", inline=False)
    embed.set_footer(text="Version 0.1  | Dice Roll System")

    await interaction.response.send_message(embed=embed)


def rzut20():
    liczba = random.randint(1, 20)
    return liczba


@bot.tree.command(name="d20", description="A roll of a twenty-sided die.")
async def d20_command(interaction: discord.Interaction):
    liczba = rzut20()
    embed = discord.Embed(title="🎲 You rolled a d20", color=discord.Color.red())
    embed.add_field(name="The result is:", value=f"{liczba}", inline=False)
    embed.set_footer(text="Version 0.1  | Dice Roll System")

    await interaction.response.send_message(embed=embed)

def rzut6():
    liczba = random.randint(1, 6)
    return liczba


@bot.tree.command(name="d6", description="A roll of a six-sided die.")
async def d6_command(interaction: discord.Interaction):
    liczba = rzut6()
    embed = discord.Embed(title="🎲 You rolled a d6", color=discord.Color.red())
    embed.add_field(name="The result is:", value=f"{liczba}", inline=False)
    embed.set_footer(text="Version 0.1  | Dice Roll System")

    await interaction.response.send_message(embed=embed)

def rzut4():
    liczba = random.randint(1, 4)
    return liczba


@bot.tree.command(name="d4", description="A roll of a four-sided die.")
async def d4_command(interaction: discord.Interaction):
    liczba = rzut4()
    embed = discord.Embed(title="🎲 You rolled a d4", color=discord.Color.red())
    embed.add_field(name="The result is:", value=f"{liczba}", inline=False)
    embed.set_footer(text="Version 0.1  | Dice Roll System")

    await interaction.response.send_message(embed=embed)


def rzut2():
    liczba = random.randint(1, 2)
    return liczba


@bot.tree.command(name="d2", description="A roll of a two-sided die.")
async def d2_command(interaction: discord.Interaction):
    liczba = rzut2()
    embed = discord.Embed(title="🎲 You rolled a d2", color=discord.Color.red())
    embed.add_field(name="The result is:", value=f"{liczba}", inline=False)
    embed.set_footer(text="Version 0.1  | Dice Roll System")

    await interaction.response.send_message(embed=embed)

def rzut10():
    liczba = random.randint(1, 10)
    return liczba


@bot.tree.command(name="d10", description="A roll of a ten-sided die.")
async def d10_command(interaction: discord.Interaction):
    liczba = rzut10()
    embed = discord.Embed(title="🎲 You rolled a d10", color=discord.Color.red())
    embed.add_field(name="The result is:", value=f"{liczba}", inline=False)
    embed.set_footer(text="Version 0.1  | Dice Roll System")

    await interaction.response.send_message(embed=embed)

def rzut100():
    liczba = random.randint(1, 100)
    return liczba


@bot.tree.command(name="d100", description="A roll of a hundred-sided die.")
async def d100_command(interaction: discord.Interaction):
    liczba = rzut100()
    embed = discord.Embed(title="🎲 You rolled a d100", color=discord.Color.red())
    embed.add_field(name="The result is:", value=f"{liczba}", inline=False)
    embed.set_footer(text="Version 0.1  | Dice Roll System")

    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="roll", description="A roll of a die with a specified number of sides.")
@app_commands.describe(liczba="Number of sides on the die (e.g., 4, 6, 8, 20)")
async def roll_command(interaction: discord.Interaction, liczba: int):
    if liczba <= 0:
        await interaction.response.send_message("❌ The number of sides must be greater than zero.", ephemeral=True)
        return

    wynik = random.randint(1, liczba)
    embed = discord.Embed(title=f"🎲 You rolled a d{liczba}", color=discord.Color.red())
    embed.add_field(name="The result is:", value=f"{wynik}", inline=False)
    embed.set_footer(text="Version 0.1  | Dice Roll System")

    await interaction.response.send_message(embed=embed)











if not TOKEN:
    raise RuntimeError("Missing Discord token. Set the DISCORD_TOKEN environment variable.")

bot.run(TOKEN)