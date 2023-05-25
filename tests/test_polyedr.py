from shadow.polyedr import Polyedr
from pytest import approx


class TestPolyedr:

    def test_sum_edges1(self):
        pol = Polyedr("data/test.geom")
        pol.no_draw_just_shades()
        pol.func()
        assert pol.sum_edges == approx(0.8)

    def test_sum_edges2(self):
        pol = Polyedr("data/test2.geom")
        pol.no_draw_just_shades()
        pol.func()
        assert pol.sum_edges == approx(7.1231056256176615)