#!/usr/bin/env python3
"""Local-only static preview, including the site's global Cloudflare headers."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit
import argparse

ROOT = Path(__file__).resolve().parents[1]


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        parts = Path(unquote(urlsplit(self.path).path)).parts
        if any(part.startswith('.') for part in parts):
            self.send_error(404)
            return
        super().do_GET()

    def end_headers(self):
        # This project intentionally uses a single global /* header rule.
        for line in (ROOT / '_headers').read_text(encoding='utf8').splitlines():
            if line.startswith('  ') and ':' in line:
                name, value = line.strip().split(':', 1)
                self.send_header(name, value.strip())
        super().end_headers()

    def list_directory(self, path):
        self.send_error(404)
        return None


class PreviewServer(ThreadingHTTPServer):
    # Browsers and audits can request many static resources at the same time.
    request_queue_size = 64


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8000)
    args = parser.parse_args()
    server = PreviewServer(('127.0.0.1', args.port), partial(Handler, directory=str(ROOT)))
    print(f'KILAT MOTORWORKS preview: http://127.0.0.1:{args.port}/ — Ctrl+C to stop', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nPreview stopped.')
    finally:
        server.server_close()
