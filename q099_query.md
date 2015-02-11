Question No.99: Query strings
=============================

> 90で作ったプログラムをCGIに改変し，「q」というパラメータで検索クエリを受け取り，検索結果をHTMLで出力せよ．

codes
-----

See directory `cgi-bin`.

- `start_cgiServer.py`: Starting a CGI server
- `clock.cgi`: Showing a clock (q098)
- `cgi_test.py`: Showing queries
- `q099_query.py`: Showing tweets includes query strings

use
---

1. Start a cgi server using `python start_cgiServer.py` command.
2. Access `http://localhost/8000:cgi-bin/q099_query.py` using browsers like Chrome, Safari and so on.
3. Query using `q=`. For example, if you want to search tweets includes **soccor**, you may access like `http://localhost/8000:cgi-bin/q099_query.py?q=soccor`
