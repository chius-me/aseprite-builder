from pathlib import Path
import unittest


WORKFLOW = Path(__file__).resolve().parents[1] / ".github" / "workflows" / "build.yml"


def workflow_text() -> str:
    return WORKFLOW.read_text(encoding="utf-8")


class WorkflowTests(unittest.TestCase):
    def test_windows_build_disables_online_features_that_pull_openssl_runtime(self):
        text = workflow_text()

        self.assertIn("-DENABLE_NEWS=OFF", text)
        self.assertIn("-DENABLE_UPDATER=OFF", text)

    def test_windows_build_disables_libarchive_openssl_autodetection(self):
        text = workflow_text()

        self.assertIn("-DENABLE_OPENSSL=OFF", text)

    def test_windows_build_audits_for_missing_openssl_runtime_dependencies(self):
        text = workflow_text()

        self.assertIn("dumpbin /dependents", text)
        self.assertIn("libcrypto-3-x64.dll", text)
        self.assertIn("libssl-3-x64.dll", text)
        self.assertIn("Git/OpenSSL runtime dependency", text)


if __name__ == "__main__":
    unittest.main()
