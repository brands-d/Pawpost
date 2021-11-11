from code_file import foo

class TestCode:

    def setup_method(self):
        print('Runs before each method')

    def test_foo(self):
        assert foo(0) == 0
