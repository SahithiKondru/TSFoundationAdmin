import os
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core import driver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver import ActionChains, DesiredCapabilities
import unittest
import time


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        desired_capabilities = DesiredCapabilities().CHROME.copy()
        desired_capabilities['acceptInsecureCerts'] = True
        web_driver = webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=desired_capabilities)

    if request.param == "firefox":
        desired_capabilities = DesiredCapabilities().FIREFOX.copy()
        desired_capabilities['acceptInsecureCerts'] = True
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                                       capabilities=desired_capabilities)

    if request.param == "edge":
        desired_capabilities = DesiredCapabilities().EDGE.copy()
        desired_capabilities['acceptInsecureCerts'] = True
        web_driver = webdriver.Edge(EdgeChromiumDriverManager().install(), capabilities=desired_capabilities)

    request.cls.driver = web_driver
    web_driver.delete_all_cookies()

    yield
    web_driver.close()

# if __name__== '__main__':
#     unittest.main(testRunner=html_test_report.HTMLTestRunner(output='..\\Reports'))

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call":
#         # always add url to report
#         extra.append(pytest_html.extras.url("https://nalb-devts.vip.corp.brassring.com/ibp/core/app/login?tenantId=bws_smoke3"))
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             #report_directory = os.path.dirname(item.config.option.htmlpath)
#             root_directory = os.path.dirname(os.path.dirname(__file__))
#             report_directory = os.path.join(root_directory, 'Reports\\')
#             #file_name = str(int(round(time.time() * 1000))) + ".png"
#             file_name = report.nodeid.replace("::", "_") + ".png"
#             destinationFile = os.path.join(report_directory, file_name)
#             driver.save_screenshot(destinationFile)
#             if file_name:
#                 html = '<div><img src ="%s" alt="screenshot" style="width:300px:height=200px"' \
#                        'onclick ="window.open(this.src)" align="right"/></div>' % file_name
#                 # only add additional html on failure
#             extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
#
# def pytest_html_report_title(report):
#     report.title = "TS Foundation/Admin Report"