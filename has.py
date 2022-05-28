# Coded by Mayank Rajput
# hackelite01
# Mayank Rajput (hackelite01)



import base64, codecs
magic = 'aW1wb3J0IGhhc2hsaWIKaW1wb3J0IHN5cyx0aW1lLG9zLHN5cwoKCiNUZXh0IGNvbG91cgojY3JlYXRlZCBCeSBNYXlhbmsgUmFqcHV0IChoYWNrZWxpdGUwMSkKY29sb3Vyb2ZmPSJceDFiWzAwbSIgI2NvbG91ciBvZmYKCnJlZD0iXHgxYls5MW0iICNyZWQKZ3JlZW49Ilx4MWJbOTJtIiAjZ3JlZW4KeWVsbG93PSJceDFiWzkzbSIgI3llbGxvdwpibHVlPSJceDFiWzk0bSIgI2JsdWUKcm9zeT0iXHgxYls5NW0iICNyb3N5CnBlc3Q9Ilx4MWJbOTZtIiAjcGVzdAoKZGVmIG1haW4oKToKCWltcG9ydCBiYXNlNjQKCWZsPW9wZW4oIi5tZC50eHQiLCJyIikKCWZpbD1mbC5yZWFkKCkKCWZpbGVyPWZpbC5lbmNvZGUoJ3V0Zi04JykKCWZpbGVlPWJhc2U2NC5iNjRkZWNvZGUoZmlsZXIpCglmaWxlPXN0cihmaWxlZS5kZWNvZGUoJ3V0Zi04JykpCglzcD1maWxlLnNwbGl0KCJcbiIpCgkKCSMjIyMjIyMjIyMjIwoJdmNjPTAKCWZvciBoYXMgaW4gc3A6CgkJCgkJZnVuY2VyPWZ1bmNbMF0KCQloYXNoPWhhcy5lbmNvZGUoJ3V0Zi04JykKCQloYXNoZXI9aGFzaGxpYi5uZXcoZnVuY2VyLGhhc2gpCgkJaGFzaGVkPWhhc2hlci5oZXhkaWdlc3QoKQoJCQoJCWlmIGhhc2hlZD09aW5wOgoJCQlwcmludChibHVlKyJcblxuXHRZb3VyIFBhc3N3b3JkIENyYWNrZWQ6IFxuIFx0ICAgIityZWQraGFzKQoJCQlpbnB1dChibHVlKyJcblxuICAgICAgIFByZXNzIEVudGVyIFRvIEJhY2sgUHJldmlvdXMgTWVudSAiKQoJCQljb250aW51ZQoJCQkKCQllbGlmIHZjYz09KGxlbihzcCkpLTE6CgkJCXByaW50KHJlZCsiXG5cblx0WW91ciBQYXNzd29yZCBOb3QgTWF0Y2ggVG8gV29ybGRsaXN0ICIpCgkJCWlucHV0KGJsdWUrIlxuXG4gICAgICAgUHJlc3MgRW50ZXIgVG8gQmFj'
love = 'eVSOlMKMco3ImVR1yoaHtVvxXPDy2L2Z9qzAwXmRXPDxXPDxXPDbXq2ucoTHtIUW1MGbXPJM1ozAlCIfvoJD1Vvjvp2uuZFVfVaAbLGVlAPVfVaAbLGV1AvVfVaAbLGZ4APVfVaAbLGHkZvVfVaAbLGZgZwV0Vvjvp2uuZl0lAGLvYPWmnTRmYGZ4APVfVaAbLGZgAGRlVvjvLzkun2HlLvVfVaWcpTIgMQR2ZPVfVaqbnKWfpT9ioPWqPtxXPJ9mYaA5p3EyoFtaL2kyLKVaXDbWpUWcoaDbLzk1MFgzVvVvPvNtVS9sK18tVPNtVPNtVPNtVPNtVPNtKlNtVPNtVPNtVPNtVPNtVPOsK19sKlNtVPNtVPNtVPNtKjbtVP8tK19ssS8tK18tK18tKlNtK19ssPO8VS9sK19sVS8tK18tVPO8KlNtVS98K18tVPOsK18tsPO8PvNvVvVeLzk1MFfvVvW8VUjtVPO8VPqsKl8tK2NtsP8tK198VUjiVP8tKlOpVPqsK3ksK19ssPO8YlOsVSjtYlOsVSk8VUjXVPVvVvgjMKA0XlVvVajtsS9sK3jtsPO8VPussPO8VPusK3jtVPN8VPOsKl8tsPO8K19sK198VUjtXS8cVUjtXS8cVUjtsNbtVSksK19ssS98VPOpK18fK3kpK19ssS98KS9pK19ssS98VPNtVPNtVUkssSksK18iVSksK18isS98KT5povNvVvVeM3WyMJ4eVvVvVPNtVPNtVPNtVPNtVRAlLJAeVSyiqKVtI29loTDfVRyzVSyiqFOQLJ5poykhKUDtVPNtVPNtVPNvVvVeLzk1MFfvVvWo4cvSKFOVLKZtD3WuL2gypvOo4cvSKFOpovVvVvgapzIyovfvVvVtCG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09CG09VvVvX2AioT91pz9zMvxXPJAbo3AyCKA0pvucoaO1qPujMKA0XlWpoyk0ZF4tD3WuL2ftGHD1VPNtVPNtVPNtZv4tD3WuL2ftH0uOZFNtVSkhKUDmYvOQpzSwnlOGFRRlZwDtVPNtVPN0YvOQpzSwnlOGFRRlAGMpoyk0AF4tD3WuL2ftH0uOZmt0VPNtVP'
god = 'AgNi4gQ3JhY2sgU0hBNTEyXG5cdDcuIENyYWNrIFNIQTMtMjI0ICAgIDguIENyYWNrIFNIQTMtMjU2XG5cdDkuIENyYWNrIFNIQTMtMzg0ICAgIDEwLkNyYWNrIFNIQTMtNTEyXG5cdDExLkNyYWNrIEJMQUtFMkIgICAgIDEyLkNyYWNrIFJJUEVNRDE2MCBcblx0MTMuQ3JhY2sgV0hJUkxQT09MICAgIityZWQrIjAwLiBCYWNrIFRvIEhvbWVcblxuIityb3N5KyJFbnRlciBZb3VyIEhhcyBUeWxlOiAiKSkKCQoJCglmdW5jPVsgXQoJCglpZiBjaG9zZT09IjAwIjoKCQlicmVhawoJCglpZiBjaG9zZT09JzEnOgoJCWlucD1zdHIoaW5wdXQoIlxuRW50ZXIgVGFyZ2V0IEhhc2hlZCBDb2RlOiAiKSkKCQlyZWFsPWZ1bmNyWzBdCgkJZnVuYy5hcHBlbmQocmVhbCkKCQoJaWYgY2hvc2U9PScyJzoKCQlpbnA9c3RyKGlucHV0KCJcbkVudGVyIFRhcmdldCBIYXNoZWQgQ29kZTogIikpCgkJcmVhbD1mdW5jclsxXQoJCWZ1bmMuYXBwZW5kKHJlYWwpCgkKCQoJaWYgY2hvc2U9PSczJzoKCQlpbnA9c3RyKGlucHV0KCJcbkVudGVyIFRhcmdldCBIYXNoZWQgQ29kZTogIikpCgkJcmVhbD1mdW5jclsyXQoJCWZ1bmMuYXBwZW5kKHJlYWwpCgkKCWlmIGNob3NlPT0nNCc6CgkJaW5wPXN0cihpbnB1dCgiXG5FbnRlciBUYXJnZXQgSGFzaGVkIENvZGU6ICIpKQoJCXJlYWw9ZnVuY3JbM10KCQlmdW5jLmFwcGVuZChyZWFsKQoJCglpZiBjaG9zZT09JzUnOgoJCWlucD1zdHIoaW5wdXQoIlxuRW50ZXIgVGFyZ2V0IEhhc2hlZCBDb2RlOiAiKSkKCQlyZWFsPWZ1bmNyWzRdCgkJZnVuYy5hcHBlbmQocmVhbCkKCQoJaWYgY2hvc2U9PSc2JzoKCQlpbnA9c3RyKGlucHV0KCJcbkVudGVyIFRhcmdldCBIYXNoZWQgQ29kZTogIikpCgkJcmVhbD1mdW5jcls1X'
destiny = 'DbWPJM1ozZhLKOjMJ5xXUWyLJjcPtxXPJyzVTAbo3AyCG0aAlp6PtxWnJ5jCKA0pvucoaO1qPtvKT5SoaEypvOHLKWaMKDtFTSmnTIxVRAiMTH6VPVcXDbWPKWyLJj9MaIhL3WoAy0XPDyzqJ5wYzSjpTIhMPulMJSfXDbWPtycMvOwnT9mMG09WmtaBtbWPJyhpQ1mqUVbnJ5jqKDbVykhEJ50MKVtITSlM2I0VRuup2uyMPOQo2EyBvNvXFxXPDylMJSfCJM1ozAlJmqqPtxWMaIhLl5upUOyozDbpzIuoPxXPDbWnJLtL2uip2H9CFp5WmbXPDycoaN9p3ElXTyhpUI0XPWpoxIhqTIlVSEupzqyqPOVLKAbMJDtD29xMGbtVvxcPtxWpzIuoQ1zqJ5wpyf4KDbWPJM1ozZhLKOjMJ5xXUWyLJjcPtxXPJyzVTAbo3AyCG0aZGNaBtbWPJyhpQ1mqUVbnJ5jqKDbVykhEJ50MKVtITSlM2I0VRuup2uyMPOQo2EyBvNvXFxXPDylMJSfCJM1ozAlJmyqPtxWMaIhLl5upUOyozDbpzIuoPxXPDbWnJLtL2uip2H9CFpkZFp6PtxWnJ5jCKA0pvucoaO1qPtvKT5SoaEypvOHLKWaMKDtFTSmnTIxVRAiMTH6VPVcXDbWPKWyLJj9MaIhL3WoZGOqPtxWMaIhLl5upUOyozDbpzIuoPxXPDbWnJLtL2uip2H9CFpkZvp6PtxWnJ5jCKA0pvucoaO1qPtvKT5SoaEypvOHLKWaMKDtFTSmnTIxVRAiMTH6VPVcXDbWPKWyLJj9MaIhL3WoZGSqPtxWMaIhLl5upUOyozDbpzIuoPxXPDbWnJLtL2uip2H9CFpkZlp6PtxWnJ5jCKA0pvucoaO1qPtvKT5SoaEypvOHLKWaMKDtFTSmnTIxVRAiMTH6VPVcXDbWPKWyLJj9MaIhL3WoZGWqPtxWMaIhLl5upUOyozDbpzIuoPxXPDbWPtycMvOwnT9mMG09VwNjVwbXPDyvpzIunjbWPtyyoUAyBtbWPKOup3ZXVjxWpUWcoaDbXDbwPDywo250nJ51MDbWPDbWVlZwVlZwVlZwVlZwVlZwVjbWqUW5BtbWPJ1unJ4bXDbWMKuwMKO0BtbWPKOup3Z='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
