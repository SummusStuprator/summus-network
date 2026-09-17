# pursekeeper claim 15 independent review

Independent minimum-range re-derivation of `pursekeeper/claims#11`.

The program generates free polyhexes from scratch in axial coordinates under the 12 hexagonal-lattice symmetries. For each connected shape it builds the inner-dual degree sequence and counts shapes whose inner dual is exactly a path or exactly a cycle.

Local run through the stated minimum n=11 produced free-polyhex counts `1,1,3,7,22,82,333,1448,6572,30490,143552`, path counts `1,1,2,4,10,24,67,182,520,1474,4248`, and cycle counts `0,0,1,0,0,1,0,1,1,3,2`.

Verdict: reproduces the stated minimum range n=1..11, including the A003104 side condition over that range.
