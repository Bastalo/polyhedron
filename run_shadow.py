#!/usr/bin/env -S python3 -B

from time import time
from common.tk_drawer import TkDrawer
from shadow.polyedr import Polyedr


tk = TkDrawer()
try:
    for name in ["test", "test2"]:
        print("=============================================================")
        print(f"Начало работы с полиэдром '{name}'")
        start_time = time()
        polyedr = Polyedr(f"data/{name}.geom")
        polyedr.draw(tk)
        delta_time = time() - start_time
        polyedr.func()
        print(f"Изображение полиэдра '{name}' заняло {delta_time} сек.")
        print("Сумма длин проекций рёбер, которые удовлетворятют условиям "
              f"задачи, равно {polyedr.sum_edges}")
        input("Hit 'Return' to continue -> ")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
