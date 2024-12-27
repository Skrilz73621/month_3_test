from bot_config import dispatcher, bot, database
import asyncio

from handlers.start import start_router
from handlers.complain import complain_router

async def on_startup(bot):
    database.create_tables()

async def main():
    dispatcher.include_router(start_router)
    dispatcher.include_router(complain_router)
    dispatcher.startup.register(on_startup)
    await dispatcher.start_polling(bot)
    
    
if __name__ == '__main__':
    asyncio.run(main())