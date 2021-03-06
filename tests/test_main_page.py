# -*- coding: utf-8 -*-
"""Module contains tests for 'src/mypage.py'."""

import sys
sys.path.append('src')

from webtest import TestApp
import mypage


def test_main_page():
    """Test main page."""
    app = TestApp(mypage.app)

    # Check if 'main page' returns '200'
    assert app.get('/').status == '200 OK'

    # Check if we can't access static files from URI
    assert app.get('/static', expect_errors=True).status == '404 Not Found'
