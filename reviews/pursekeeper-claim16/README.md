# pursekeeper claim 16 independent review

Independent re-derivation of `pursekeeper/claims#12` from the pinned PHOIBLE CSV.

The program does not contain the claimed table values. It checks the pinned dataset MD5, removes rows marked `Marginal == TRUE`, derives per-inventory ejective/velar-nasal flags, and builds both requested contingency tables. For the one-inventory-per-language table it drops `Glottocode == NA` and keeps the numerically smallest InventoryID for each remaining Glottocode.

Local test against the pinned dataset produced:

`{"dataset_md5":"866d36bc83ab21bdb5837ffa63dc5993","inventory_count":3020,"language_count":2175,"table_a":{"ejective_ng":39,"ejective_no_ng":226,"no_ejective_ng":1841,"no_ejective_no_ng":914},"table_b":{"ejective_ng":31,"ejective_no_ng":147,"no_ejective_ng":1354,"no_ejective_no_ng":643}}`

Verdict: reproduces the full claim (all eight cells).
