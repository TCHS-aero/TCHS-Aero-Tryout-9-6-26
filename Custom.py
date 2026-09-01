import asyncio
from mavsdk import System

async def main():
    drone = System("udpin://0.0.0.0:14540")

if __name__ == "__main__":
    asyncio.run(main)
