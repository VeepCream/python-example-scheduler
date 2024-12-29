import asyncio
from asyncio.log import logger
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import discord
from example_scheduler.utils.logger import get_logger


async def work_daily_job():
    _logger = get_logger()
    _logger.info("work_daily_job")

   
def setup_scheduler():
    _logger = get_logger()

    # Create a new asyncio event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Initialize APScheduler with the AsyncIO scheduler
    scheduler = AsyncIOScheduler(event_loop=loop)

    scheduler.add_job(
        func=work_daily_job, trigger="cron", hour="1", minute="0"
    )

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