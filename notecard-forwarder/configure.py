import json
import notecard
import os
from periphery import I2C

import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message)

productUID = os.getenv('NC_PRODUCT_UID')

start_server = websockets.serve(echo, "localhost", 8765)

def main():
  print("Connecting to Notecard...")

  port = I2C("/dev/i2c-1")
  card = notecard.OpenI2C(port, 0, 0, debug=True)

  print(f'Configuring Product: {productUID}...')

  req = {"req": "hub.set"}
  req["product"] = productUID
  req["mode"] = "periodic"
  req["outbound"] = 60
  req["inbound"] = 120
  req["align"] = True

  card.Transaction(req)

main()

# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()