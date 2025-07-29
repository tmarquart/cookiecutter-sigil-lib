def test_import():
    import {{ cookiecutter.project_slug }}
    assert {{ cookiecutter.project_slug }} is not None
