# -*- coding: utf-8 -*-

# https://gist.github.com/jacquerie/cfb8a56636e2b9e12f51

import base64

MESSAGE = '''
E0YBBxoXAx8FT0FIUl4TFAkXHEZeUl4XCQAaDQAVBxxTRlZWTwQBBhwRCwkST01SVRwSAAMEHBJV UkNUQQUYCxMXFhAWCglRREFVExocDwkADQwXHA1TRlZWTxQcHhYXDQkST01SVQsVBA4fHBJVUkNU QR8XDgRVXllTAAMZT0FIUl4DDwJXTxw=
'''

KEY = 'harrytflv'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(ord(c) ^ ord(KEY[i % len(KEY)])))

print ''.join(result)
