# -*- coding: utf-8 -*-

import unittest

from starlette.testclient import TestClient

from modsdk_mcp.server import create_sse_app


class SseAppTest(unittest.TestCase):
    def test_health_check(self):
        with TestClient(create_sse_app()) as client:
            response = client.get("/health")

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload["status"], "ok")
        self.assertEqual(payload["server"], "netease-modsdk-mcp")
        self.assertEqual(payload["modsdk_version"], "3.10")
        self.assertEqual(payload["bedrock_version"], "1.21.130")
        self.assertEqual(payload["rule_count"], 61)
        self.assertGreater(payload["detector_count"], 0)
        self.assertGreater(payload["document_count"], 0)
        self.assertTrue(payload["snapshot_time"])
        self.assertEqual(payload["runtime_evidence_status"], "unreviewed")

    def test_message_endpoint_returns_http_error_without_type_error(self):
        with TestClient(create_sse_app(), raise_server_exceptions=True) as client:
            response = client.post("/messages/?session_id=bad", json={})

        self.assertEqual(response.status_code, 400)
        self.assertIn("Invalid session ID", response.text)

    def test_message_endpoint_redirects_to_trailing_slash(self):
        with TestClient(
            create_sse_app(),
            raise_server_exceptions=True,
            follow_redirects=False,
        ) as client:
            response = client.post("/messages?session_id=bad", json={})

        self.assertEqual(response.status_code, 307)
        self.assertTrue(response.headers["location"].endswith("/messages/?session_id=bad"))


if __name__ == "__main__":
    unittest.main()
