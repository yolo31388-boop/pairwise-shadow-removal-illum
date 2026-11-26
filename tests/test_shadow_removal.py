import pytest
import imaging.shadow_removal as mod

CASES = [
    ("soft_penumbra_preserve", (1,)),
    ("structure_guided_fill", (1,)),
    ("light_dir_temporal_align", (1,)),
    ("local_temp_constraint", (1,)),
    ("block_light_continuity", (1,)),
    ("cache_key_lightdir", (1,)),
    ("load_shadow_image", (1,)),
    ("detect_shadow", (1,)),
    ("remove_shadow", (1,)),
    ("present_shadow", (1,)),
    ("validate_shadow", (1,)),
    ("metrics_shadow", (1,)),
    ("audit_shadow", (1,)),
    ("fallback_shadow", (1,)),
    ("determinism_shadow", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
