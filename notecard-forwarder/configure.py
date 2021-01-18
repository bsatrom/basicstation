import json
import notecard
import os
from periphery import I2C

productUID = os.getenv('NC_PRODUCT_UID')

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