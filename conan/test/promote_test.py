"""Test Conan promote features

"""

import unittest
from conans.test.utils.tools import TestServer, TestClient
from conans.client import conan_api
from conan import conan_promote


CONANFILE = """from conans import ConanFile
class MyPkg(ConanFile):
    name = "Hello"
    version = "0.1.0"
    exports_sources = "*"
    def package(self):
        self.copy("*")
"""


class PromoteTest(unittest.TestCase):
    """Execute Conan promote tests

    """

    def setUp(self):
        self.test_server = TestServer(read_permissions=[("*/*@*/*", "*")],
                                      write_permissions=[("*/*@foobar/stable", "conanuser")], users={"conanuser": "conanpass"})
        self.client = TestClient(servers={"testing": self.test_server}, users={"testing": [("conanuser", "conanpass")]})
        self.client.save({"conanfile.py": CONANFILE})

    def test_promote_run(self):
        """Default Conan Promote flow

        :return:
        """
        self.client.run("create conanuser/testing")
        self.client.run("upload Hello/0.1.0@conanuser/testing --confirm --all")
        self.client.run("search -r testing")
        self.assertIn("Hello/0.1.0@conanuser/testing", self.client.user_io.out)
        self.assertNotIn("Hello/0.1.0@foobar/stable", self.client.user_io.out)

        self.client.run("remove Hello/0.1.0@conanuser/testing --force")
        self.client.run("search")
        self.assertIn("There are no packages", self.client.user_io.out)

        promote = conan_promote.ConanPromote()
        promote.conan_instance = conan_api.Conan(self.client.client_cache, self.client.user_io, self.client.runner,
                                                 self.client.remote_manager, self.client.search_manager, None)
        promote.run(["Hello/0.1.0@conanuser/testing", "-r", "testing", "-s", "testing"])

        self.client.run("search -r testing")
        self.assertIn("Hello/0.1.0@conanuser/testing", self.client.user_io.out)
        self.assertIn("Hello/0.1.0@foobar/stable", self.client.user_io.out)
        self.client.run("search")
        self.assertIn("There are no packages", self.client.user_io.out)
