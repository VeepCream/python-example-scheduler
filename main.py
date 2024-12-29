import asyncio
from asyncio.log import logger
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import discord
from example_scheduler.utils.logger import get_logger
# >>>>>>> เพื่ม import ของ BotDiscord <<<<<<<
from example_scheduler.adapters.discord_adapter import BotDiscord
# ==============================================


async def work_daily_job():
    _logger = get_logger()
    _logger.info("work_daily_job")

# >>>>>>> เพื่ม def check_healty_service() <<<<<<<
async def check_healty_service(client: BotDiscord):
    _logger = get_logger()
    await client.start_send_message(is_good=False)
# ==============================================

   
def setup_scheduler():
    _logger = get_logger()
    
    # >>>>>>> เพื่ม intents และ client(BotDiscord) <<<<<<<
    intents = discord.Intents.default()
    intents.message_content = True
    client = BotDiscord(intents=intents)
    # ==============================================

    # Create a new asyncio event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Initialize APScheduler with the AsyncIO scheduler
    scheduler = AsyncIOScheduler(event_loop=loop)

    scheduler.add_job(
        func=work_daily_job, trigger="cron", hour="1", minute="0"
    )
    
    # >>>>>>> เพื่ม interval และ ใน scheduler.add_job() <<<<<<<
    scheduler.add_job(
        func=check_healty_service,
        kwargs={"client": client},
        trigger="interval",
        seconds=10,
    )
    # ==============================================

    scheduler.start()

    _logger.info("Scheduler started")

    _logger.info(f"date: {scheduler.get_jobs()[0].next_run_time}; {datetime.now()}")

    return loop

if __name__ == "__main__":
    try:
        loop = setup_scheduler()
        loop.run_forever()
    except (KeyboardInterrupt, SystemExit):
        pass