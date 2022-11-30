import pytest
from selenium.common import NoSuchElementException, TimeoutException, InvalidSessionIdException

from Src.login_function.login import test_cluster_login


class Test001:

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_Laravel_default_01(self, setup):
        self.driver = setup
        # pytest.skip("Skipping test...later I will implement...")
        # action = ActionChains(self.driver)
        ApplicationName = "laravel-0134"
        print("****************** Test Cluster Login *********************")
        try:
            test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)