import asyncio
import time
from kasa import SmartPlug
from gpiozero import MotionSensor

pir = MotionSensor(4)
time.sleep(60)

async def main():
    p = SmartPlug("192.168.0.115")

    await p.update()
    print(p.alias)
    while True:
        print(pir.value)
        if pir.value == 1:
            await p.turn_on()
            print('yee')
        else:
            await p.turn_off()
            print('na')


if __name__ == "__main__":
    asyncio.run(main())