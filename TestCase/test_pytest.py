import allure


@allure.feature("测试功能 二")
class   Test_py:

    @allure.story("测试小功能  二 1")
    def test_demo1(self):
        a=1
        b=1
        assert a == b

    @allure.story("测试小功能 二 2")
    def test_demo2(self):
        a=1
        b=1
        assert a == b