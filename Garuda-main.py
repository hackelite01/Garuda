
#######################
#                     #
#      MAIN FILE      # 
#                     #
#######################
# Author: hackelite01 #
#######################
#                     #
# CODER : hackelite01 #
#                     #
#######################



# Coded by Mayank Rajput
# hackelite01
  



import base64, codecs
magic = 'aW1wb3J0IG9zLHRpbWUsc3lzLG1hcnNoYWwsZ2xvYgoKI1RleHQgY29sb3VyCiNjcmVhdGVkIEJ5IGhhY2tlbGl0ZTAxCmNvbG91cm9mZj0iXHgxYlswMG0iICNjb2xvdXIgb2ZmCgpyZWQ9Ilx4MWJbOTFtIiAjcmVkCmdyZWVuPSJceDFiWzkybSIgI2dyZWVuCnllbGxvdz0iXHgxYls5M20iICN5ZWxsb3cKYmx1ZT0iXHgxYls5NG0iICNibHVlCnJvc3k9Ilx4MWJbOTVtIiAjcm9zeQpwZXN0PSJceDFiWzk2bSIgI3Blc3QKCnJlZDE9Ilx4MWJbMTs5MW0iICNyZWQKZ3JlZW4xPSJceDFiWzE7OTJtIiAjZ3JlZW4KeWVsbG93MT0iXHgxYlsxOzkzbSIgI3llbGxvdwpibHVlMT0iXHgxYlsxOzk0bSIgI2JsdWUKcm9zeTE9Ilx4MWJbMTs5NW0iICNyb3N5CnBlc3QxPSJceDFiWzE7OTZtIiAjcGVzdAoKCiMjIyMjIyMjIyMjIyMjIyMjIyMjCgoKdHJ5OgkKCSNleGVjKG9wZW4oIi9kYXRhL2RhdGEvY29tLnRlcm11eC9maWxlcy9ob21lL0dhcnVkYS8udGVzdC9tYWFpaW4ucHkiLCJyIikucmVhZCgpKQoJb3Muc3lzdGVtKCJjaG1vZCAreCAvZGF0YS9kYXRhL2NvbS50ZXJtdXgvZmlsZXMvdXNyL2Jpbi9HYXJ1ZGEiKQpleGNlcHQ6CglwYXNzCgppZiBsZW4oZ2xvYi5nbG9iKCIvZGF0YS9kYXRhL2NvbS50ZXJtdXgvZmlsZXMvaG9tZS9HYXJ1ZGEvLnRlc3QvbWFhaWluLnB5IikpPT0xOgoJb3Muc3lzdGVtKCJybSAtcmYgL2RhdGEvZGF0YS9jb20udGVybXV4L2ZpbGVzL2hvbWUvR2FydWRhLy50ZXN0L21hYWlpbi5weSIpCglzeXMuZXhpdCgpCgoKCgpvcy5zeXN0ZW0oInJtIC1yZiByZXF1aXJlbWVudC5zaCIpCm9zLnN5c3RlbSgicm0gLXJmIF9fcHljYWNoZV9fIikKCiMjIyMjIyMjIyMjIyMjIyMjIyMjIwoKCgpkZWYgY29udCgpOgoJd2hpbGUgVHJ1ZToKCQlvcy5zeXN0ZW0oJ2NsZWFyJykKCQlwcmludChyb3N5MSsiIiIKCQoJICAgICAgICAgICAgICAgICAgICAgMXwgSW5zdGFHcmFtCgkgICAgICAgICAgICAgICAgICAgICAyfCBUZWxlZ3JhbQoJICAgICAgICAgICAgICAgICAgICAgM3wgR2l0SHViCgkgICAgICAgICAgICAgICAgICAgICAiIiIrcmVkMSsiIiI0fCBCYWNrIFRvIEhvbWUKCSIiIikKCQkKCQljaG9zZT1zdHIoaW5wdXQocm9zeSsiXG5cbkVudGVyIFlvdXIgT3B0aW9uOiAiKSkKCQoJCWlmIGNob3NlPT0iMSI6CgkJCXByaW50KCJcbiAgT3BlbmluZyBVUkw6IGh0dHBzOi8vd3d3Lmluc3RhZ3JhbS5jb20vaGFja2VsaXRlMDEiKQoJCQlvcy5zeXN0ZW0oInRlcm11eC1vcGVuIGh0dHBzOi8vd3d3Lmluc3RhZ3JhbS5jb20vaGFja2VsaXRlMDEiKQoJCQl0aW1lLnNsZWVwKDMpCgkJZWxpZiBjaG9zZT09IjIiOgoJCQlwcmludCgiXG4gIE9wZW5pbmcgVVJMOiBodHRwczovL3QubWUvaGFja2VsaXRlMDEiKQoJCQlvcy5zeXN0ZW0oInRlcm11eC1vcGVuIGh0dHBzOi8vdC5tZS9oYWNrZWxpdGUwMSIpCgkJCXRpbWUuc2xlZXAoMykKCQkKCQllbGlmIGNob3NlPT0iMyI6CgkJCXByaW50KCJcbiAgT3BlbmluZyBVUkw6IGh0dHBzOi8vZ2l0aHViLmNvbS9oYWNrZWxpdGUwMSIpCgkJCW9zLnN5c3RlbSgidGVybXV4LW9wZW4gaHR0cHM6Ly9naXRodWIuY29tL2hhY2tlbGl0ZTAxIikKCQkJdGltZS5zbGVlcCgzKQoJCQkKCQll'
love = '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'
god = 'dDErIiIifCB8X19ffCB8IHwgKF98IHwgKF9ffCAgIDwgIF9fLyB8IHxfX19fX3wgfCAoXykgfCAoXykgfCB8CiAgXF9fX198X3wgIFxfXyxffFxfX198X3xcX1xfX198X3wgICAgICAgfF98XF9fXy8gXF9fXy98X3xcblxuICIiIityZWQxKyIiIk1hZGUgYnkgTWF5YW5rIFJhanB1dCAoaGFja2VsaXRlMDEpXG4iIiIrZ3JlZW4xKyIiIiAgICAgICAgICAgICBDcmFjayBZb3VyIFdvcmxkLCBJZiBZb3UgQ2FuXG5cblx0XHQgICAgICAiIiIreWVsbG93MSsiIiJWZXJzaW9uOiIiIityZWQxK3ZlcnNpb24rIiIiIiIiK2NvbG91cm9mZikKCQoJCgljaG9vc2U9c3RyKGlucHV0KHBlc3QxKyIiIlxuClx0fD09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09fApcdHwiIiIreWVsbG93MSsiIiIgMS5Db250YWN0IEluZm8iIiIrcGVzdDErIiIiICAgICAgMi5JUCBUb29sICAgICAgICB8Clx0fCAzLlN1YmRvbWFpbiBTY2FubmVyIDQuRGRvcyBBdHRhY2sgICAgfApcdHwgNS5BZG1pbiBGaW5kZXIgICAgICA2LkhhcyBDcmFja2VyICAgIHwKXHR8IDcuVmlkZW8gRG93bmxvYWRlciAgOC5Bbm9uIFNoYXJlICAgICB8Clx0fCA5LlNRTC1JbmplY3Rpb24gICAgMTAuVGV4dCBUbyBWb2ljZSAgfApcdHwxMS5QeXRob24gT2JmdXNjYXRlIDEyLlRlbGVncmFtIEtpdCAgIHwKXHR8MTMuVGVybXV4IEZyYW1ld29yayAxNC5LYWxpIE5ldGh1bnRlciB8Clx0fDE1LlRlcm11eCBUb29sICAgICAgMTYuVVJMIENoYW5nZXIgICAgfApcdHwxNy5VUkwgU2hvcnRuZXIgICAgIDE4LldFQiBUb29sICAgICAgIHwKXHR8MTkuVGVtcCBNYWlsICAgICAgICAyMC5HZW5hcmF0ZSBHTUFJTCB8Clx0fDIxLkNDVFYgSGFjayAgICAgICAgMjIuR2VuZXJhdGUgSWRlbnQufApcdHwyMy5NdWx0aSBEZG9zICAgICAgICAgICAgICAgICAgICAgICAgIHwKXHR8ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB8Clx0fCIiIitncmVlbjErIiIiIDg4LlVwZGF0ZSBHYXJ1ZGEiIiIrcmVkMSsiIiIgICAgOTkuRXhpdCIiIitwZXN0MSsiIiIgICAgfApcdHw9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PXwKXG4iIiIrcm9zeTErIiIiRW50ZXIgWW91ciBPcHRpb246ICIiIikpCgoJCglpZiBjaG9vc2U9PSI5OSI6CgkJb3Muc3lzdGVtKCJjbGVhciIpCgkJcHJpbnQoeWVsbG93KyJcblxuXG5cblxuXG5cdFx08J+kqVRoYW5rcyBGb3IgVXNpbmcgTXkgVG9vbPCfpKkgICBcblxuXG4iKQoJCXN5cy5leGl0KCkKCQoJCgllbGlmIGNob29zZT09IjEiOgoJCW9zLnN5c3RlbSgiY2xlYXIiKQoJCWNvbnQoKQoJCgllbGlmIGNob29zZT09IjIiOgoJCW9vPW9wZW4oImlwLnB5IiwiciIpCgkJZXhlYyhvby5yZWFkKCkpCgkKCWVsaWYgY2hvb3NlPT0iNCI6CgkJb289b3BlbigiZGRvcy5weSIsInIiKQoJCWV4ZWMob28ucmVhZCgpKQoJCgllbGlmIGNob29zZT09IjMiOgoJCW9vPW9wZW4oInN1YmRtLnB5IiwiciIpCgkJZXhlYyhvby5yZWFkKCkpCgkKCWVsaWYgY2hvb3NlPT0iNSI6CgkJb289b3BlbigiYWRtaW4ucHkiLCJyIikKCQlleGVjKG9vLnJlYWQoKSkKCQoJZWxpZiBjaG9vc2U9PSI2IjoKCQlvbz1vcGVuKCJoYXMucHkiLCJyIikKCQlleGVjKG9vLnJlYWQoKSkKCQoJZWxpZiBjaG9vc2U9PSI3IjoKCQlvbz1vcGVuKCJkb3dubGQucHkiLCJyIikKCQk='
destiny = ''
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
