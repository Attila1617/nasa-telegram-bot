import logging
import requests
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'blablabla'
NASA_API_KEY = 'lolololo'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.answer("I'm Space-Bot, powered by NASA API. Type /help command for instructions.")


@dp.message_handler(commands='help')
async def send_instructions(message: types.Message):
    await message.answer('Here is the list of commands:\n/apod - Each day a different image or photograph of our fascinating universe is featured, along with a brief explanation written by a professional astronomer.')


@dp.message_handler(commands='apod')
async def apod(message: types.Message):
    response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}')
    data = response.json()
    explanation = f"{data['explanation']}"
    title = f"{data['title']}"
    await message.answer_photo(photo=data['url'], caption=title)
    await message.answer(explanation)
    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

