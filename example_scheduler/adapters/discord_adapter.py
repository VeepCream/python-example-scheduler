import asyncio
import discord

from example_scheduler.config import DISCORD_CHANNEL_ID, DISCORD_TOKEN

class BotDiscord(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._is_good = False
        self.args = args
        self.kwargs = kwargs

    async def start_send_message(self,is_good=False):
        self.__init__(*self.args, **self.kwargs)
        self._is_good = is_good
        await self.start(DISCORD_TOKEN)

    async def on_ready(self):
        try:
            print('Logged on as', self.user)
            await self.send_message()
        except Exception as e:
            print(e)

    async def on_disconnect(self):
        print("Disconnected")

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        
        print(f"Message from {message.author}: {message.content}")

        if message.content == 'ping':
            await self.send_message()

    async def send_message(self):

    # Wait a moment to ensure the bot is connected
        await asyncio.sleep(1)


        print(DISCORD_CHANNEL_ID)
        # Fetch the channel
        channel = self.get_channel(DISCORD_CHANNEL_ID)
        if channel:
            try:
                # Send the message
                message = "all service is good" if self._is_good else "@everyone , There are propblems with the service"
                await channel.send(message)
                print("Message sent successfully!")
            except Exception as e:
                print(f"Error sending message: {e}")
        else:
            print("Channel not found.")

        # Stop the bot
        await asyncio.sleep(3)
        await self.close()

