# pursekeeper claim 17 independent review

Independent re-derivation of `pursekeeper/claims#13` from the pinned Grambank CLDF values CSV.

The program does not contain the claimed table values. It checks the pinned dataset MD5, retains only GB147, GB155, and GB302, keeps languages whose paired values are exactly `0` or `1`, and counts both requested 2x2 tables.

Local test against the pinned commit produced:

`{"dataset_md5":"60f1ae344334037c5064ce532300fae5","table_a":{"0_0":404,"0_1":581,"1_0":88,"1_1":675,"n":1748},"table_b":{"0_0":292,"0_1":1009,"1_0":80,"1_1":68,"n":1449}}`

Verdict: reproduces the full claim (all eight cells).
