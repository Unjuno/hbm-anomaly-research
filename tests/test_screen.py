import unittest
from tools.screen import screen, read_rows, ROOT

class ScreenTest(unittest.TestCase):
    def row(self, **changes):
        base = dict(id='synthetic', name='Synthetic fixture', nominal_capacity_gb='8',
                    effective_bus_bits='4096', bus_status='vendor', peak_bandwidth_gbps='1496',
                    reference_density_gb='16', reference_basis='synthetic test only')
        base.update(changes)
        return base

    def test_synthetic_low_capacity(self):
        r = screen(self.row())
        self.assertEqual(r['gb_per_1024bit'], 2)
        self.assertAlmostEqual(r['q'], 0.125)
        self.assertAlmostEqual(r['inferred_pin_rate_gbps'], 2.921875)
        self.assertEqual(r['flag'], 'strong_relative_mismatch')

    def test_unknown_width(self):
        r = screen(self.row(bus_status='unknown', effective_bus_bits=''))
        self.assertIsNone(r['gb_per_1024bit'])
        self.assertIsNone(r['q'])
        self.assertEqual(r['nominal_bw_per_gb_s_inv'], 187)

    def test_conditional_width_not_used(self):
        r = screen(self.row(bus_status='hypothesis'))
        self.assertIsNone(r['effective_bus_bits'])
        self.assertEqual(r['flag'], 'missing_width')

    def test_reference_needs_basis(self):
        self.assertIsNone(screen(self.row(reference_basis=''))['q'])

    def test_invalid_numbers(self):
        for value in ('0','-1','nan','inf'):
            with self.subTest(value=value), self.assertRaises(ValueError):
                screen(self.row(nominal_capacity_gb=value))

    def test_same_width_different_capacity(self):
        a = screen(self.row(nominal_capacity_gb='16', reference_density_gb='4', peak_bandwidth_gbps='900'))
        b = screen(self.row(nominal_capacity_gb='32', reference_density_gb='4', peak_bandwidth_gbps='900'))
        self.assertEqual(a['inferred_pin_rate_gbps'], b['inferred_pin_rate_gbps'])
        self.assertEqual(a['gb_per_1024bit'], 4)
        self.assertEqual(b['gb_per_1024bit'], 8)

    def test_seed_a30_and_unknown_cmp(self):
        rows = {r['id']:screen(r) for r in read_rows(ROOT/'data/devices.csv')}
        self.assertEqual(rows['a30']['gb_per_1024bit'], 8)
        self.assertEqual(rows['a30']['q'], 1)
        self.assertEqual(rows['cmp170-8']['q'], 0.25)
        self.assertEqual(rows['cmp170-10']['q'], 0.25)
        self.assertEqual(rows['cmp170-8']['bus_status'], 'community_report')
        self.assertIsNone(rows['cmp100-200']['gb_per_1024bit'])
        self.assertIsNone(rows['a30x']['gb_per_1024bit'])

if __name__ == '__main__':
    unittest.main()
