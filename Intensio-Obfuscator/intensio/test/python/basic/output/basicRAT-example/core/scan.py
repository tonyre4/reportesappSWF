# -*- coding: utf-8 -*-
import socket
yYxudvlLhtmQwRMZlxMVkuZzsTYvDTcG = [ 
            21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 179, 443, 445,
            514, 993, 995, 1723, 3306, 3389, 5900, 8000, 8080, 8443, 8888
]
def lxpHoRVQHmZlAmDEjqZZhfmtRDctbLaW(ip):
    try:
        socket.inet_aton(ip)
    except socket.error:
        return 'Error: Invalid IP address.'
    hTHEiuCIZGZSbKRssLNLpfrQaMYerPyt = ''
    for jWOhPeWyYiAMZGeISnknzYlvOIKdtTqh in yYxudvlLhtmQwRMZlxMVkuZzsTYvDTcG:
        cfVfTzUSlYOIdEbVStOBAaeUNJdepWJu = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        xSQpmyINTvpmGsETqSvOlKRYiEgmKGNz = cfVfTzUSlYOIdEbVStOBAaeUNJdepWJu.connect_ex((ip, jWOhPeWyYiAMZGeISnknzYlvOIKdtTqh))
        socket.setdefaulttimeout(0.5)
        hdAsvQFjtqifMrwkWKdvjaPZZeitgfAe = 'open' if not xSQpmyINTvpmGsETqSvOlKRYiEgmKGNz else 'closed'
        hTHEiuCIZGZSbKRssLNLpfrQaMYerPyt += '{:>5}/tcp {:>7}\n'.format(jWOhPeWyYiAMZGeISnknzYlvOIKdtTqh, hdAsvQFjtqifMrwkWKdvjaPZZeitgfAe)
    return hTHEiuCIZGZSbKRssLNLpfrQaMYerPyt.rstrip()
