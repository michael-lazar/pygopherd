import io
import unittest

from pygopherd import testutil
from pygopherd.handlers.base import VFS_Real
from pygopherd.handlers.file import FileHandler
from pygopherd.handlers.url import HTMLURLHandler, URLTypeRewriter


class TestHTMLURLHandler(unittest.TestCase):
    def setUp(self):
        self.config = testutil.get_config()
        self.vfs = VFS_Real(self.config)
        self.selector = "URL:http://gopher.quux.org/"
        self.protocol = testutil.get_testing_protocol(self.selector, config=self.config)
        self.stat_result = None

    def test_url_rewriter_handler(self):
        """
        The URL rewriter should drop the "/0" at the beginning of the selector
        and then pass it off to the appropriate handler.
        """
        handler = HTMLURLHandler(
            self.selector, "", self.protocol, self.config, self.stat_result, self.vfs
        )

        self.assertTrue(handler.isrequestforme())

        entry = handler.getentry()
        self.assertEqual(entry.mimetype, "text/html")
        self.assertEqual(entry.type, "h")

        wfile = io.BytesIO()
        handler.write(wfile)

        out = wfile.getvalue()
        self.assertIn(
            b'<A HREF="http://gopher.quux.org/">http://gopher.quux.org/</A>', out
        )

    def test_handler_escape_urls(self):
        """
        URLs should be escaped in the generated HTML.
        """
        handler = HTMLURLHandler(
            'URL:http://gopher.quux.org/"<script>',
            "",
            self.protocol,
            self.config,
            self.stat_result,
            self.vfs,
        )

        entry = handler.getentry()
        self.assertEqual(entry.mimetype, "text/html")
        self.assertEqual(entry.type, "h")

        wfile = io.BytesIO()
        handler.write(wfile)

        out = wfile.getvalue()
        self.assertNotIn(b'http://gopher.quux.org/"<script>', out)
        self.assertIn(b"http://gopher.quux.org/&quot;&lt;script&gt;", out)


class TestURLTypeRewriterHandler(unittest.TestCase):
    def setUp(self):
        self.config = testutil.get_config()
        self.vfs = VFS_Real(self.config)
        self.selector = "/0/README"
        self.protocol = testutil.get_testing_protocol(self.selector, config=self.config)
        self.stat_result = None

    def test_url_rewriter_handler(self):
        """
        The URL rewriter should drop the "/0" at the beginning of the selector
        and then pass it off to the appropriate handler.
        """

        handler = URLTypeRewriter(
            self.selector, "", self.protocol, self.config, self.stat_result, self.vfs
        )

        self.assertTrue(handler.canhandlerequest())

        new_handler = handler.gethandler()
        self.assertIsInstance(new_handler, FileHandler)

        self.assertEqual(new_handler.selector, "/README")
        self.assertTrue(new_handler.canhandlerequest())
