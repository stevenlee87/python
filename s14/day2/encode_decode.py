__author__ = "Steven Lee"


# msg = "我爱北京天安门"
# print(msg)
# print(msg.encode())
# print(msg.encode(encoding="utf-8").decode(encoding="utf-8"))


msg1 = b"{\x22st\x22:\x221490853749163\x22,\x22lon\x22:116.484528,\x22dip\x22:3,\x22appv\x22:\x221.0\x22,\x22ecode\x22:\x2270000\x22,\x22appname\x22:\x22360\xE5\xB9\xBF\xE5\x91\x8A\xE6\xB5\x8B\xE8\xAF\x95\x22,\x22carrier\x22:\x22\x22,}"
#print(msg1.encode(encoding="utf-8").decode(encoding="utf-8"))

print(msg1.decode(encoding="utf-8"))

