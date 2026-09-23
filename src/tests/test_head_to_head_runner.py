import sys
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "docs/eval/head-to-head"))
import run_matrix as matrix


class HeadToHeadRunnerTests(unittest.TestCase):
    def test_julie_search_uses_the_opened_workspace(self):
        class FakeMcp:
            def __init__(self):
                self.calls = []

            def call_tool(self, tool, args, timeout):
                self.calls.append((tool, args))
                return 1, {"result": {"content": [{"type": "text", "text": "lib/application.js:1"}]}}

            def close(self):
                pass

        client = FakeMcp()
        row = {
            "id": "express-router.search",
            "repo": "express",
            "task_class": "retrieval.concept",
            "julie": {"tool": "fast_search", "args": {"query": "router", "limit": 5}},
            "miller": {"tool": "search", "args": {}},
            "expected": {"path": "lib/application.js"},
            "scoring": {"mode": "path_top5"},
        }
        with patch.object(
            matrix,
            "open_julie_repo",
            return_value=(client, "express_id", {"workspace_id": "express_id", "symbols": 1, "vectors": 0}),
        ):
            matrix.run_matrix(
                {"repos": {"express": {"path": "/tmp/express"}}},
                [row],
                Path("/fake/julie"),
                Path("/fake/miller"),
                skip_julie=False,
                skip_miller=True,
                require_semantics=False,
            )

        self.assertEqual(client.calls[0][1]["workspace"], "/tmp/express")


if __name__ == "__main__":
    unittest.main()
