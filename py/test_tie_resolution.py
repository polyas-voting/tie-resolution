import unittest

from tie_resolution import tie_resolution

class TestTieResolution(unittest.TestCase):

    def test_tie_resolution_against_a_fixture(self):
        resolution = tie_resolution(
            s_seed = "systemSeed",
            u_seed = "userSeed",
            ballot_id = "ballot-A",
            list_id = "list-23",
            tied_candidates = 20,
        )
        self.assertEqual([12, 4, 14, 5, 2, 3, 8, 10, 18, 11, 15, 0, 9, 19, 13, 16, 7, 17, 6, 1], resolution)
