from datetime import timedelta
import os

TIME_ZONE_TH = os.getenv("TIME_ZONE_TH", "Asia/Bangkok")
UTC_OFFSET = os.getenv("UTC_OFFSET", "7")

DISCORD_CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID", 0))
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", "")