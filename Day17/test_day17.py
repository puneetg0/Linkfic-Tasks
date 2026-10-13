import os
from pathlib import Path
import sys
import unittest


PROJECT_ROOT = Path(__file__).resolve().parent.parent
BACKEND_PATH = PROJECT_ROOT / "Day11" / "backend"
sys.path.insert(0, str(BACKEND_PATH))
os.environ["JWT_SECRET_KEY"] = "day-17-local-test-key-not-for-production"
os.environ.setdefault("DATABASE_URL", "sqlite://")

from fastapi import HTTPException

from auth_day13 import Credentials, hash_password, login, verify_password
from dsapractice import binary_search, find_missing_number


class BinarySearchTests(unittest.TestCase):
    def test_finds_item_at_first_middle_and_last_positions(self):
        numbers = [2, 4, 6, 8, 10]

        self.assertEqual(binary_search(numbers, 2), 0)
        self.assertEqual(binary_search(numbers, 6), 2)
        self.assertEqual(binary_search(numbers, 10), 4)

    def test_returns_none_when_item_is_missing(self):
        self.assertIsNone(binary_search([2, 4, 6, 8], 5))

    def test_handles_an_empty_list(self):
        self.assertIsNone(binary_search([], 5))


class MissingNumberTests(unittest.TestCase):
    def test_finds_a_missing_middle_number(self):
        self.assertEqual(find_missing_number([1, 2, 4, 5]), 3)

    def test_finds_missing_first_or_last_number(self):
        self.assertEqual(find_missing_number([2, 3, 4]), 1)
        self.assertEqual(find_missing_number([1, 2, 3]), 4)


class PasswordHashTests(unittest.TestCase):
    def test_password_hash_accepts_the_correct_password(self):
        stored_hash = hash_password("safe-test-password")

        self.assertTrue(verify_password("safe-test-password", stored_hash))
        self.assertFalse(verify_password("wrong-test-password", stored_hash))

    def test_malformed_password_hash_is_rejected_without_crashing(self):
        malformed_hashes = (
            "",
            "not-a-password-hash",
            "pbkdf2_sha256$not-a-number$YQ$YQ",
            "pbkdf2_sha256$600000$$",
        )

        for stored_hash in malformed_hashes:
            with self.subTest(stored_hash=stored_hash):
                self.assertFalse(verify_password("any-password", stored_hash))

    def test_unsupported_hash_algorithm_is_rejected(self):
        self.assertFalse(verify_password("any-password", "unknown$1$YQ$YQ"))

    def test_malformed_hash_is_reported_as_an_invalid_login(self):
        class UserWithBrokenHash:
            password_hash = "not-a-password-hash"

        class FakeDatabase:
            def scalar(self, _statement):
                return UserWithBrokenHash()

        with self.assertRaises(HTTPException) as error:
            login(
                Credentials(email="learner@example.com", password="test-password"),
                FakeDatabase(),
            )

        self.assertEqual(error.exception.status_code, 401)


if __name__ == "__main__":
    unittest.main()
