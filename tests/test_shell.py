from unittest import TestCase

from paho.mqtt.enums import MQTTProtocolVersion

from mqshell import MQTTShell


class TestShell(TestCase):
    def setUp(self):
        self.shell = MQTTShell()

    def test_initialization(self):
        self.assertIsInstance(self.shell, MQTTShell)
        self.assertTrue(hasattr(self.shell, "client_id"))
        self.assertTrue(hasattr(self.shell, "client"))
        self.assertEqual(self.shell.client._protocol, MQTTProtocolVersion.MQTTv5)
