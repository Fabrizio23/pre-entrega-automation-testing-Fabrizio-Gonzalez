import pytest

test_files = [
    "tests/test_login.py",
    "tests/test_login_faker.py",
    "tests/test_inventory.py",
    "tests/test_cart.py",
    "tests/test_carrito.py",
    "tests/test_cart_json.py",
    "tests/test_api.py"
]

pytest_args = test_files + ["--html=report.html", "--self-contained-html", "-v"]

pytest.main(pytest_args)