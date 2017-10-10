from unittest import TestCase
from ..device import DeviceInfo

class TestDeviceInfo(TestCase):
    
    def test_init_raw(self):
        data = {
            'ap': {'bssid': 'FF:FF:FF:FF:FF:FF', 'rssi': -68, 'ssid': 'network'},
            'cfg_time': 0,
            'fw_ver': '1.2.4_16',
            'hw_ver': 'MW300',
            'life': 24,
            'mac': '28:FF:FF:FF:FF:FF',
            'mmfree': 30312,
            'model': 'chuangmi.plug.m1',
            'netif': {'gw': '192.168.xxx.x',
                   'localIp': '192.168.xxx.x',
                   'mask': '255.255.255.0'},
            'ot': 'otu',
            'ott_stat': [0, 0, 0, 0],
            'otu_stat': [320, 267, 3, 0, 3, 742],
            'token': '2b00042f7481c7b056c4b410d28f33cf',
            'wifi_fw_ver': 'SD878x-14.76.36.p84-702.1.0-WM'}
        t = DeviceInfo(data)
        self.assertEqual(data, t.raw)
        self.assertEqual(data['netif'], t.network_interface)
        test_str = "chuangmi.plug.m1 v1.2.4_16 (28:FF:FF:FF:FF:FF) @ 192.168.xxx.x - token: 2b00042f7481c7b056c4b410d28f33cf"  #noqa
        self.assertEqual(test_str, repr(t))
        self.assertEqual(data['ap'], t.accesspoint)
        self.assertEqual(data['model'], t.model)
        self.assertEqual(data['fw_ver'], t.firmware_version)
        self.assertEqual(data['hw_ver'], t.hardware_version)
        

    def test_miss_data(self):
        data = {
            'ap': {'bssid': 'FF:FF:FF:FF:FF:FF', 'rssi': -68, 'ssid': 'network'},
            'cfg_time': 0,
            'fw_ver': None,
            'hw_ver': None,
            'life': 24,
            'mac': '28:FF:FF:FF:FF:FF',
            'mmfree': 30312,
            'model': 'chuangmi.plug.m1',
            'netif': {'gw': '192.168.xxx.x',
                   'localIp': '192.168.xxx.x',
                   'mask': '255.255.255.0'},
            'ot': 'otu',
            'ott_stat': [0, 0, 0, 0],
            'otu_stat': [320, 267, 3, 0, 3, 742],
            'token': '2b00042f7481c7b056c4b410d28f33cf',
            'wifi_fw_ver': 'SD878x-14.76.36.p84-702.1.0-WM'}
        t = DeviceInfo(data)
        self.assertIsNone(t.firmware_version)
        self.assertIsNone(t.hardware_version)
