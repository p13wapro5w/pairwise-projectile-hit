import pytest
from game import projectile_hit as mod

CASES = [
    ("layers_list", "m.ray_layers(['world', 'actor']) == ['world', 'actor']"),
    ("wood_depth", "m.penetration(1.0, 'wood') == approx(0.5)"),
    ("steel_depth", "m.penetration(1.0, 'steel') == approx(0.1)"),
    ("interp_mid", "m.interpolate_position((0.0, 0.0), (2.0, 2.0), 0.5) == approx((1.0, 1.0))"),
    ("drop_mid", "m.ballistic_drop(10.0, 1.0, 9.8) == approx(4.9)"),
    ("batch_three", "m.batch_query(3) == 3"),
    ("swept_two", "m.swept_bounds(1.0, 2.0, 0.5) == approx(2.0)"),
    ("recoil_half", "m.recoil_predict((0.0, 0.0), (1.0, 0.0), 0.5) == approx((0.5, 0.0))"),
    ("rewind_eight", "m.server_rewind(10, 2) == 8"),
    ("falloff_eight", "m.damage_falloff(10.0, 2.0) == approx(8.0)"),
    ("ccd_true", "m.ccd_needed(10.0, 1.0, 0.1) is True"),
    ("ccd_false", "m.ccd_needed(1.0, 1.0, 0.1) is False"),
    ("wood_greater", "m.penetration(1.0, 'wood') > m.penetration(1.0, 'steel')"),
    ("batch_zero", "m.batch_query(0) == 0"),
    ("interp_start", "m.interpolate_position((0.0, 0.0), (2.0, 2.0), 0.0) == approx((0.0, 0.0))")
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
