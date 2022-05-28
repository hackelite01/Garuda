# Coded by Mayank Rajput
# hackelite01
# Mayank Rajput (hackelite01)

import base64, codecs
magic = 'I01heWFuayBSYWpwdXQgKGhhY2tlbGl0ZTAxKQojbG9nbygpOgogICAgICAgICNjcmVhdG9yOiBNYXlhbmsgUmFqcHV0IChoYWNrZWxpdGUwMSkKaW1wb3J0IG9zCmltcG9ydCB0aW1lCmltcG9ydCBzeXMKCiN0ZXh0IGNvbG91cigpCiNjcmVhdG9yOiBNYXlhbmsgUmFqcHV0IChoYWNrZWxpdGUwMSkKCiNUZXh0IGNvbG91cgojY3JlYXRlZCBCeSBNYXlhbmsgUmFqcHV0IChoYWNrZWxpdGUwMSkKY29sb3Vyb2ZmPSJceDFiWzAwbSIgI2NvbG91ciBvZmYKCnJlZD0iXHgxYls5MW0iICNyZWQKZ3JlZW49Ilx4MWJbOTJtIiAjZ3JlZW4KeWVsbG93PSJceDFiWzkzbSIgI3llbGxvdwpibHVlPSJceDFiWzk0bSIgI2JsdWUKcm9zeT0iXHgxYls5NW0iICNyb3N5CnBlc3Q9Ilx4MWJbOTZtIiAjcGVzdAoKcmVkMT0iXHgxYls0MW0iICNyZWQxCiMxOAp3aGl0ZSA9ICdcMzNbMDBtJwpyZWQgPSAnXDMzWzkxbScKZ3JlZW4gPSAnXDMzWzkybScKeW9sbG93ID0gJ1wzM1s5M20nCmJsdWUgPSAnXDMzWzk0bScKcm9zeSA9ICdcMzNbOTVtJwpwZXN0ID0gJ1wzM1s5Nm0nCgoKcmVkYiA9ICdcMzNbNDFtJwp5b2xsb3diID0gJ1wzM1s0M20nCmJsdWViID0gJ1wzM1s0NG0nCnJvc3liID0gJ1wzM1s0NW0nCnBlc3RiID0gJ1wzM1s0Nm0nCmdyZWVuYiA9ICdcMzNbNDJtJwojY29sb3VyIGVuZAoKCiMjIyNhbmltYXRpb24jIyMKZGVmIGIoeik6CiAgICBmb3Igd29yZCBpbiB6ICsgJ1xuJzoKICAgICAgICBzeXMuc3Rkb3V0LndyaXRlKHdvcmQpCiAgICAgICAgc3lzLnN0ZG91dC5mbHVzaCgpCiAgICAgICAgdGltZS5zbGVlcCgwLjAxNSkgIAoKCmRlZiBjKHopOgogICAgZm9yIHdvcmQgaW4geiArICdcbic6CiAgICAgICAgc3lzLnN0ZG91dC53cml0ZSh3b3JkKQogICAgICAgIHN5cy5zdGRvdXQuZmx1c2goKQogICAgICAgIHRpbWUuc2xlZXAoMC4wMykgCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIwoKCgoKb3Muc3lzdGVtKCJjbGVhciIpCiNsb2dvIHN0YXJ0CmRlZiBsb2dvKCk6CiAgICAgICAgcHJpbnQocGVzdCsiXHQgICAgICAgICAgICAgfCIrZ3JlZW4rIiBAICAgQCIrcGVzdCsiIHwiKQogICAgICAgIHByaW50KCJcdCAgICAgICAgICAgICAg4oCU4oCU4oCU4oCU4oCU4oCU4oCUIikKICAgICAgICBwcmludCgiXHQgICAgICAgICAgICAgfGNyYWNrZXJ8IikKICAgICAgICBwcmludCh5b2xsb3crIlx0ICAgICAgICAgICAgICDigJTigJTigJTigJTigJTigJTigJQiKQogICAgICAgIHByaW50KCJcdCAgICAgICAgIC9cICB8ICAgICAgIHwgICAvXFxcICIpCiAgICAgICAgcHJpbnQoIlx0ICAgICAgICAvLyBc4oCU4oCUICAgICAgIOKAlOKAlOKAlC8gIFxcXCAiKQogICAgICAgIHByaW50KCJcdCAgIF9fX18vLyBjcmFjayB5b3VyIHdvcmxkICBcXFxfX18iKQogICAgICAgIHByaW50KCIiKQogICAgICAgIHByaW50KCJcdHw9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09fCIpCiAgICAgICAgcHJpbnQoIlx0fCAgICAgICBIYWNrIFJpY2gsIEdpdmUgdG8gUG9vciAgICB8IikKICAgICAgICBwcmludCgiXHR8PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PXwiKQogICAgICAgIAoKbG9nbygpCgoKCnRpbWUuc2xlZXAoMi4zKQpvcy5zeXN0ZW0oJ2NsZWFyJykKCiNsb2FkaW5nLi4KCnByaW50KGdyZWVuKyJcdFx0ICAgIExvYWRpbmcuLi4uLlxuIikKdGltZS5zbGVlcCgxLjQpCgpiKGdyZWVuKyJDcmFja2luZy4uLi5cdCIrcmVkYisiWz09PSAgICAgICAgICAgICAgICAgIF0iK3doaXRlKQp0aW1lLnNsZWVwKDEuMCkKCmIoZ3JlZW4rIkNyYWNraW5nLi4uLlx0Iityb3N5YisiWz09PT09PSAgICAgICAgICAgICAgIF0iK3doaXRlKQp0aW1lLnNsZWVwKDEuMCkKCmIoZ3JlZW4rIkNyYWNraW5nLi4uLlx0Iit5b2xsb3diKyJbPT09PT09PT09ICAgICAgICAgICAgXSIrd2hpdGUpCnRpbWUuc2xlZXAoMS4wKQoKYihncmVlbisiQ3JhY2tpbmcuLi4uXHQiK3Blc3RiKyJbPT09PT09PT09PT09ICAgICAgICAgXSIrd2hpdGUpCnRpbWUuc2xlZXAoMS4wKQpiKGdyZWVuKyJDcmFja2luZy4uLi5cdCIrYmx1ZWIrIls9PT09PT09PT09PT09PT0gICAgICBdIit3aGl0ZSkKdGltZS5zbGVlcCgxLjApCmIoZ3JlZW4rIkNyYWNraW5nLi4uLlx0IitncmVlbmIrIls9PT09PT09PT09PT09PT09PT0gICBdIit3aGl0ZSkKCnRpbWUuc2xlZXAoMS4zKQpvcy5zeXN0ZW0oJ2NsZWFyJykKCgoKCm9zLnN5c3RlbSgiY2xlYXIiKSAKcHJpbnQoZ3JlZW4rZiIiIlxuXG5cblxuXG5cblxuXG4gXHQgICAgICAgICAtbyAgICAgICAgICBvLSAgICAgICAgICAgIAogIFx0ICAgICAgICAgICtoeWROTk5OZHloKyAgICAgICAgICAgICAKICBcdCAgICAgICAgK21NTU1NTU1NTU1NTU1tKyAgICAgICAgICAgCiAgXHQgICAgICBgZE1NbTpOTU1NTU1NTjptTU1kYCAgICAgICAgIAogIFx0ICAgICAgaE1NTU1NTU1NTU1NTU1NTU1NTWggICAgICAgICAKICBcdCAgLi4gIHl5eXl5eXl5eXl5eXl5eXl5eXk='
love = '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'
god = 'ExODEiIiIrY29sb3Vyb2ZmK2dyZWVuKyIiIiBNTS1NTU1NOiAgIAogIFx0Ok1NTU0tTU0gICAgICAgICAgICAgICAgTU0tTU1NTToKICBcdC1NTU1NLU1NTU1NTU1NTU1NTU1NTU1NTU1NLU1NTU0tCiAgXHQgK3l5KyBNTU1NTU1NTU1NTU1NTU1NTU1NTSAreXkrCiAgXHQgICAgICBtTU1NTU1NTU1NTU1NTU1NTU1NbQogIFx0ICAgICAgYC8rK01NTU1oKytoTU1NTSsrL2AKICBcdCAgICAgICAgICBNTU1NbyAgb01NTU0KICBcdCAgICAgICAgICBNTU1NbyAgb01NTU0KICBcdCAgICAgICAgICBvTk1tLSAgLW1NTnMiIiIpCgoKdGltZS5zbGVlcCguMykKb3Muc3lzdGVtKCdjbGVhcicpCnByaW50KGdyZWVuK2YiIiJcblxuXG5cbiBcdCAgICAgICAgIC1vICAgICAgICAgIG8tICAgICAgICAgICAgCiAgXHQgICAgICAgICAgK2h5ZE5OTk5keWgrICAgICAgICAgICAgIAogIFx0ICAgICAgICArbU1NTU1NTU1NTU1NTW0rICAgICAgICAgICAKICBcdCAgICAgIGBkTU1tOk5NTU1NTU1OOm1NTWRgICAgICAgICAgCiAgXHQgICAgICBoTU1NTU1NTU1NTU1NTU1NTU1NaCAgICAgICAgIAogIFx0ICAuLiAgeXl5eXl5eXl5eXl5eXl5eXl5eXkgIC4uICAgICAKICBcdC5tTU1tYE1NTU1NTU1NTU1NTU1NTU1NTU1NYG1NTW0uICAgCiAgXHQ6TU1NTS1NTU1NTU1NTU1NTU1NTU1NTU1NTS1NTU1NOiAgIAogXHQ6TU1NTS1NTSAgICAgICAgICAgICAgICBNTS1NTU1NOiAgIAogICAgICA6TU1NTS1NTSAiIiIgK3JlZDErIiIiIENSQUNLRVI5MTExODEiIiIrY29sb3Vyb2ZmK2dyZWVuKyIiIiBNTS1NTU1NOiAgIAogIFx0Ok1NTU0tTU0gICAgICAgICAgICAgICAgTU0tTU1NTToKICBcdC1NTU1NLU1NTU1NTU1NTU1NTU1NTU1NTU1NLU1NTU0tCiAgXHQgK3l5KyBNTU1NTU1NTU1NTU1NTU1NTU1NTSAreXkrCiAgXHQgICAgICBtTU1NTU1NTU1NTU1NTU1NTU1NbQogIFx0ICAgICAgYC8rK01NTU1oKytoTU1NTSsrL2AKICBcdCAgICAgICAgICBNTU1NbyAgb01NTU0KICBcdCAgICAgICAgICBNTU1NbyAgb01NTU0KICBcdCAgICAgICAgICBvTk1tLSAgLW1NTnMiIiIpCgoKCnRpbWUuc2xlZXAoLjMpCm9zLnN5c3RlbSgnY2xlYXInKQpwcmludChncmVlbitmIiIiXG5cblxuIFx0ICAgICAgICAgLW8gICAgICAgICAgby0gICAgICAgICAgICAKICBcdCAgICAgICAgICAraHlkTk5OTmR5aCsgICAgICAgICAgICAgCiAgXHQgICAgICAgICttTU1NTU1NTU1NTU1NbSsgICAgICAgICAgIAogIFx0ICAgICAgYGRNTW06Tk1NTU1NTU46bU1NZGAgICAgICAgICAKICBcdCAgICAgIGhNTU1NTU1NTU1NTU1NTU1NTU1oICAgICAgICAgCiAgXHQgIC4uICB5eXl5eXl5eXl5eXl5eXl5eXl5eSAgLi4gICAgIAogIFx0Lm1NTW1gTU1NTU1NTU1NTU1NTU1NTU1NTU1gbU1NbS4gICAKICBcdDpNTU1NLU1NTU1NTU1NTU1NTU1NTU1NTU1NLU1NTU06ICAgCiBcdDpNTU1NLU1NICAgICAgICAgICAgICAgIE1NLU1NTU06ICAgCiBcdDpNTU1NLU1NICIiIiArcmVkMSsiIiIgQ1JBQ0tFUjkxMTE4MSIiIitjb2xvdXJvZmYrZ3JlZW4rIiIiIE1NLU1NTU06ICAgCiAgXHQ6TU1NTS1NTSAgICAgICAgICAgICAgICBNTS1NTU1NOgogIFx0LU1NTU0tTU1NTU1NTU1NTU1NTU1NTU1NTU0tTU1NTS0KIFx0ICt5eSsgTU1NTU1NTU1NTU1NTU1NTU1NTU0gK3l5KwogIFx0ICAgICAgbU1NTU1NTU1NTU1NTU1NTU1NTW0KICBcdCAgICAgIGAvKytNTU1NaCsraE1NTU0rKy9gCiAgXHQgICAgICAgICAgTU1NTW8gIG9NTU1NCiAgXHQgICAgICAgICAgTU1NTW8gIG9NTU1NCiAgXHQgICAgICAgICAgb05NbS0gIC1tTU5zIiIiKQoKCgoKdGltZS5zbGVlcCguMykKb3Muc3lzdGVtKCdjbGVhcicpCnByaW50KGdyZWVuK2YiIiJcblxuIFx0ICAgICAgICAgLW8gICAgICAgICAgby0gICAgICAgICAgICAKICBcdCAgICAgICAgICAraHlkTk5OTmR5aCsgICAgICAgICAgICAgCiAgXHQgICAgICAgICttTU1NTU1NTU1NTU1NbSsgICAgICAgICAgIAogIFx0ICAgICAgYGRNTW06Tk1NTU1NTU46bU1NZGAgICAgICAgICAKICBcdCAgICAgIGhNTU1NTU1NTU1NTU1NTU1NTU1oICAgICAgICAgCiAgXHQgIC4uICB5eXl5eXl5eXl5eXl5eXl5eXl5eSAgLi4gICAgIAogIFx0Lm1NTW1gTU1NTU1NTU1NTU1NTU1NTU1NTU1gbU1NbS4gICAKICBcdDpNTU1NLU1NTU1NTU1NTU1NTU1NTU1NTU1NLU1NTU06ICAgCiBcdDpNTU1NLU1NICAgICAgICAgICAgICAgIE1NLU1NTU06ICAgCiAgICAgIDpNTU1NLU1NICIiIiArcmVkMSsiIiIgQ1JBQ0tFUjkxMTE4MSIiIitjb2xvdXJvZmYrZ3JlZW4rIiIiIE1NLU1NTU06ICAgCiAgXHQ6TU1NTS1NTSAgICAgICAgICAgICAgICBNTS1NTU1NOgogIFx0LU1NTU0tTU1NTU1NTU1NTU1NTU1NTU1NTU0tTU1NTS0KICBcdCAreXkrIE1NTU1NTU1NTU1NTU1NTU1NTU1NICt5eSsKICBcdCAgICAgIG1NTU1NTU1NTU1NTU1NTU1NTU1tC'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
