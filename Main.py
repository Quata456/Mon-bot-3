import os
import discord
from discord.ext import commands
import google.generativeai as genai

# --- CONFIGURATION VIA VARIABLES D'ENVIRONNEMENT ---
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Le reste du code reste le même...
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')
# ...
