import unittest
from vectoreek.engine import Host, VectoreekModule

class TestVectoreek(unittest.TestCase):
    def test_latching_mechanics(self):
        host = Host("Test-Belt", 1.0, "R1", "Conveyor")
        module = VectoreekModule("V-TEST")
        
        self.assertFalse(module.is_latched)
        module.latch(host)
        self.assertTrue(module.is_latched)
        self.assertEqual(module.attached_to, host)

    def test_energy_harvesting(self):
        fan_host = Host("Test-Fan", 0, "R2", "Fan")
        module = VectoreekModule("V-TEST")
        module.power_level = 50.0
        
        module.latch(fan_host)
        module.harvest_energy()
        self.assertGreater(module.power_level, 50.0)

if __name__ == "__main__":
    unittest.main()
