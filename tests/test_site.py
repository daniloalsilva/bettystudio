import pathlib
import unittest

ROOT = pathlib.Path(__file__).parents[1]


class SiteTest(unittest.TestCase):
    def test_required_content_and_whatsapp(self):
        page = (ROOT / "website/index.html").read_text(encoding="utf-8")
        self.assertIn("Betty Studio", page)
        self.assertGreaterEqual(page.count("https://wa.me/5511937742856"), 3)
        self.assertIn('class="whatsapp"', page)

    def test_assets_exist(self):
        self.assertTrue((ROOT / "website/assets/style.css").is_file())


if __name__ == "__main__":
    unittest.main()
