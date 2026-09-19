8644554852:AAGTZX1MNtWKr-IUO_umwy_QYZJDDFuXfFE
import asyncio
from telegram import Bot
from datetime import datetime, timedelta
import pytz

# ⚠️ এখানে তোমার নতুন টোকেন বসানো আছে
BOT_TOKEN = "8644554852:AAGTZX1MNtWKr-IUO_umwy_QYZJDDFuXfFE"
CHANNEL_ID = -1004211199703

async def send_signal():
    bot = Bot(token=BOT_TOKEN)
    
    dhaka = pytz.timezone('Asia/Dhaka')
    now = datetime.now(dhaka)
    trade_time = (now + timedelta(minutes=2)).strftime("%H:%M:%S")
    
    message = f"""
🟣 9 🌟 SIGNAL 🌟 9 🟣
~~~~~~~~~~~~~~~~~~~~~~
📊 Market Name ➡ GBPUSD-OTC
💰 Payout ➡ 88%
⏰ Trade Time ➡ {trade_time}
⏳ Expiry Candle ➡ M1
🎯 Trade Direction ➡ UP 🟢 | CALL
🔍 Mode ➡ OTC Market (Weekend Mode)
~~~~~~~~~~~~~~~~~~~~~~
⚡ Provider: @HM_HIMEL_VIP
📢 Join Channel: Quotex Binary 94
💎 Create Account & Join VIP Channel
"""
    await bot.send_message(chat_id=CHANNEL_ID, text=message)
    print(f"Signal sent at {now.strftime('%H:%M:%S')}")

async def main():
    await send_signal()

if __name__ == "__main__":
    asyncio.run(main())
  
