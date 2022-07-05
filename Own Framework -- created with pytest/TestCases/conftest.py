import logging

import pytest
from GeneralPackage.GeneralActions import GeneralActions

ga = GeneralActions()


@pytest.fixture(autouse=True, scope="class")
def maximize_window_yow():
    ga.open_and_maximize_window()
    yield
    ga.driver.close()


@pytest.fixture
def valid_account_login():
    print("USING FIXTURE -- valid_account_login")
    ga.correct_login()

    yield
    print("\n******** CLOSING FIXTURE ********")
    # ga.driver.close()










