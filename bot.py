import asyncio
from telegram import Bot
from datetime import datetime, timedelta
import pytz

BOT_TOKEN = "8644554852:AAEtSAM-R6Xr4XEdWCCuPH8k7SEMOHh52Zo"
CHANNEL_ID = -1004211199703

OTC_MARKETS = [
    "GBPUSD-OTC", "EURUSD-OTC", "AUDCAD-OTC", "AUDUSD-OTC",
    "USDCAD-OTC", "USDCHF-OTC", "USDJPY-OTC", "NZDUSD-OTC",
    "EURGBP-OTC", "EURJPY-OTC", "GBPJPY-OTC", "AUDJPY-OTC",
    "USDBDT-OTC", "USDINR-OTC", "USDPKR-OTC", "USDMXN-OTC"
]

async def send_signal():
    bot = Bot(token=BOT_TOKEN)
    
    dhaka = pytz.timezone('Asia/Dhaka')
    now = datetime.now(dhaka)
    trade_time = (now + timedelta(minutes=2)).strftime("%H:%M:%S")
    
    # সময়ের ভিত্তিতে মার্কেট বেছে নাও (প্রতি ৫ মিনিটে বদলাবে)
    total_minutes = now.hour * 60 + now.minute
    index = (total_minutes // 5) % len(OTC_MARKETS)
    market = OTC_MARKETS[index]
    
    # UP/DOWN পালাক্রমে
    direction = "UP 🟢 | CALL" if index % 2 == 0 else "DOWN 🔴 | PUT"
    
    message = f"""
🟣 9 🌟 SIGNAL 🌟 9 🟣
~~~~~~~~~~~~~~~~~~~~~~
📊 Market Name ➡ {market}
💰 Payout ➡ 88%
⏰ Trade Time ➡ {trade_time}
⏳ Expiry Candle ➡ M1
🎯 Trade Direction ➡ {direction}
🔍 Mode ➡ OTC Market (Weekend Mode)
~~~~~~~~~~~~~~~~~~~~~~
⚡ Provider: @HM_HIMEL_VIP
📢 Join Channel: https://t.me/quotex_binary94
💎 Create Account & Join VIP: https://broker-qx.pro/sign-up/?lid=2061219
"""
    await bot.send_message(chat_id=CHANNEL_ID, text=message)
    print(f"Signal sent for {market} at {now.strftime('%H:%M:%S')}")

async def main():
    await send_signal()

if __name__ == "__main__":
    asyncio.run(main())
