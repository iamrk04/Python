# test_parameterized_fixture.py
import pytest

class MyTester:
    def __init__(self, x):
        self.x = x

    def dothis(self):
        assert self.x

@pytest.fixture
def new_test():
    return None

@pytest.fixture
def tester(request, new_test):
    """Create tester object"""
    if hasattr(request, "param"):
        return MyTester(request.param)
    else:
        return MyTester(1)


class TestIt:
    @pytest.mark.parametrize('tester', [True, False], indirect=['tester'])
    def test_tc1(self, tester):
       tester.dothis()
       assert 1

    # @pytest.mark.parametrize('tester', [True, False], indirect=['tester'])
    def test_tc2(self, tester):
       tester.dothis()
       assert 1