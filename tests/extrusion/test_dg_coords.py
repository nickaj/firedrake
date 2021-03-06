from __future__ import absolute_import, print_function, division
from firedrake import *
import pytest


def test_extruded_interval_area():
    m = UnitIntervalMesh(10)

    DG = VectorFunctionSpace(m, 'DG', 1)
    new_coords = project(m.coordinates, DG)
    m = Mesh(new_coords)

    V = FunctionSpace(m, 'CG', 1)
    u = Function(V)
    u.assign(1)

    assert abs(assemble(u*dx) - 1.0) < 1e-12

    e = ExtrudedMesh(m, layers=4, layer_height=0.25)

    V = FunctionSpace(e, 'CG', 1)
    u = Function(V)
    u.assign(1)

    assert abs(assemble(u*dx) - 1.0) < 1e-12


def test_extruded_periodic_interval_area():
    m = PeriodicUnitIntervalMesh(10)

    V = FunctionSpace(m, 'CG', 1)
    u = Function(V)
    u.assign(1)
    assert abs(assemble(u*dx) - 1.0) < 1e-12

    e = ExtrudedMesh(m, layers=4, layer_height=0.25)
    V = FunctionSpace(e, 'CG', 1)
    u = Function(V)
    u.assign(1)

    assert abs(assemble(u*dx) - 1.0) < 1e-12


if __name__ == '__main__':
    import os
    pytest.main(os.path.abspath(__file__))
