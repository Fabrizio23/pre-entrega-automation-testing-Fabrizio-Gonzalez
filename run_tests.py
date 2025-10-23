import pytest

test_files = [
    "tests/test_login_incorrecto.py",
    "tests/test_login.py",
    "tests/test_inventory.py"
]

pytest_args = test_files + ["--html=report.html", "--self-contained-html", "-v"]

pytest.main(pytest_args)

#Para correr esto, usar el comando: python run_tests.py