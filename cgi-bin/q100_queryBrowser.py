#!/usr/bin/python
#coding: utf-8

print 'Content-Type: text/html; charset=UTF-8'
print
print """<html>
<head><title>Tweet Search</title></head>
<body>
<form action='./q099_query.py'>
  <input type='text' value='ジョコ' name='q' />
  <input type='submit' value='Search' />
</form>
</body>
</html>
"""
