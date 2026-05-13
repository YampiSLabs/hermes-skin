import yaml, sys, os

errors = 0
skins_dir = 'skins'
for f in os.listdir(skins_dir):
    if not f.endswith('.yaml'):
        continue
    path = os.path.join(skins_dir, f)
    try:
        with open(path) as fh:
            data = yaml.safe_load(fh)
        assert isinstance(data, dict), 'not a dict'
        assert data.get('name'), 'missing name'
        assert data.get('colors'), 'missing colors'
        required = [
            'banner_border', 'banner_title', 'banner_accent', 'banner_dim',
            'banner_text', 'ui_accent', 'ui_label', 'ui_ok', 'ui_error',
            'ui_warn', 'prompt', 'input_rule', 'response_border',
            'session_label', 'session_border',
        ]
        for k in required:
            assert k in data.get('colors', {}), f'missing color: {k}'
        assert isinstance(data.get('branding', {}).get('agent_name'), str), 'missing agent_name'
        print(f'OK: {f}')
    except Exception as e:
        print(f'FAIL: {f} - {e}')
        errors += 1
sys.exit(errors)