from common.r3 import R3
from pytest import approx


class TestR3:

    # Тесты на вычисление середины х-координаты у ребра
    def test_x_center1(self):
        s = R3(1.0, 3.0, 1.0)
        u = R3(4.0, 3.0, 1.0)
        assert s.x_center(u) == approx(2.5)

    def test_x_center2(self):
        s = R3(-2.0, 3.0, 1.0)
        u = R3(4.0, -1.0, 0.0)
        assert s.x_center(u) == approx(1.0)

    # Тесты на вычисление нормы
    def test_norm1(self):
        s = R3(-2.0, 2.0, 1.0)
        assert s.norm() == approx(3.0)

    def test_norm1(self):
        s = R3(0.0, 0.0, 0.0)
        assert s.norm() == approx(0.0)

    # Тесты на вычисление длины проекции ребра на горизонтальной плоскости
    def test_dist1(self):
        s = R3(3.0, 4.0, 1123324.345)
        assert s.dist(R3(0.0, 0.0, 0.0)) == approx(5.0)

    def test_dist2(self):
        s = R3(0.0, 1.0, 15.0)
        assert s.dist(R3(0.0, 0.0, 0.0)) == approx(1.0)
