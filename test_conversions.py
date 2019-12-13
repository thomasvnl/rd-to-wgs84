import unittest
from conversions import RDWGS84Converter


class TestConversions(unittest.TestCase):

    def setUp(self) -> None:
        self.__converter = RDWGS84Converter()

    def test_convert_center_point(self):
        """
        Test the center point (Onze Lieve Vrouwetoren in Amersfoort). This point should have no approximation!
        """
        rd = (155000, 463000)
        wgs84 = (52.1551744, 5.38720621)

        # First test conversion from RD to WGS84
        lat, long = self.__converter.from_rd(*rd)
        self.assertEqual(lat, wgs84[0])
        self.assertEqual(long, wgs84[1])

        # Second test conversion from WGS84 to RD
        x, y = self.__converter.from_wgs84(*wgs84)
        self.assertEqual(x, rd[0])
        self.assertEqual(y, rd[1])

    def test_convert_edge_point(self):
        """
        Testing further away from the center (approximation becomes more noticeable). Using Station Rotterdam Central.
        """
        rd = (91819, 437802)
        wgs84 = (51.925104730636065, 4.468682340354691)

        # First test conversion from RD to WGS84
        lat, long = self.__converter.from_rd(*rd)
        self.assertEqual(lat, wgs84[0])
        self.assertEqual(long, wgs84[1])

        # Second test the approximation back from WGS84 to RD
        x, y = self.__converter.from_wgs84(*wgs84)
        self.assertAlmostEqual(x, rd[0], delta=0.1)
        self.assertAlmostEqual(y, rd[1], delta=0.1)


