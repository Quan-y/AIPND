# -*- coding: utf-8 -*-
import timeit

cy = timeit.timeit('f1_cy.test(500)', setup = 'import f1_cy', number = 1000)
py = timeit.timeit('f1_py.test(500)', setup = 'import f1_py', number = 1000)
print(cy, py)
print('Cython is {}x faster'.format(py/cy))
