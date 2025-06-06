# Stub device for testing the MQTT terminal

import asyncio
import logging
import os
import sys

from amqc.client import MQTTClient, config
from mqterm.terminal import MqttTerminal

# Set up logging
logger = logging.getLogger()
logger.setLevel(getattr(logging, os.getenv("LOG_LEVEL", "WARNING").upper()))
format_str = "%(asctime)s.%(msecs)03.0f - %(levelname)s - %(name)s - %(message)s"
formatter = logging.Formatter(format_str)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
logger.handlers = [handler]

# gc.collect()


def setup_mqtt() -> MQTTClient:
    """Configure the MQTT client"""
    mqtt_settings = config.copy()
    mqtt_settings["server"] = "localhost"
    mqtt_settings["client_id"] = "mqterm_stub"
    return MQTTClient(mqtt_settings, logger=logger)


async def receive_input(client: MQTTClient, term: MqttTerminal):
    """Pass messages to the terminal. Runs forever."""
    async for topic, msg, _retained, properties in client.queue:
        await term.handle_msg(topic, msg, properties)
        await asyncio.sleep(0)  # Any delay here and we can't receive streamed files


async def main():
    # Connect to MQTT broker
    mqtt_client = setup_mqtt()
    await mqtt_client.connect()

    # Create terminal
    term = MqttTerminal(mqtt_client, topic_prefix="test/device")

    # Start processing messages in the input stream
    await term.connect()
    try:
        asyncio.run(receive_input(mqtt_client, term))
    except SystemExit:
        print("Caught SystemExit, restarting...")
        asyncio.new_event_loop()
    except KeyboardInterrupt:
        print("Shutting down...")
    except Exception as e:
        logging.error(f"Error in receive_input: {e}")

    # Clean up
    await term.disconnect()
    await mqtt_client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
