import asyncio
from collections import deque
"""
Есть генератор, который выплёвывает по одному текстовому предложению
раз в 3 секунды. imagine поход в openai API. 
Хотим сделать новый генератор, который читает эти предложения и 
выплёвывает по одному слову раз в полсекунды, чтобы юзер видел как текст
возникает слово за словом — как на сайте ChatGPT.
"""

async def gpt_sentences():
    """Yields a sentence every 3 sec"""
    sentences = [
        "The ideal bedroom temperature for sleep is between 60°F (15°C) and 67°F (19°C).",
        "This range helps the body's core temperature drop, promoting sleep onset and quality.",
        "The body's natural is influenced by temperature.",
        "Cooler environments favoring deep sleep and melatonin release."
    ]
    for s in sentences:
        yield s
        await asyncio.sleep(3)


async def producer(buffer):
    async for sent in gpt_sentences():
        buffer.extend(sent.split())


async def gpt_words(buffer):
    """Should yield a word every 0.5 sec. No 3sec delay between sentences!"""
    while buffer:
        print(buffer.popleft())
        await asyncio.sleep(0.5)


async def main():

    buffer = deque()
    pr = producer(buffer)
    printer = gpt_words(buffer)
    await asyncio.gather(pr, printer)

asyncio.run(main())
