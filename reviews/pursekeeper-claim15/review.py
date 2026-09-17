#!/usr/bin/env python3
import json

NEIGHBORS=((1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1))

def rotate(p):
    q,r=p
    return (-r,q+r)

def reflect(p):
    q,r=p
    return (q,-q-r)

def normalize(points):
    pts=list(points)
    minq=min(q for q,r in pts); minr=min(r for q,r in pts)
    return tuple(sorted((q-minq,r-minr) for q,r in pts))

def free_key(points):
    pts=list(points); variants=[]
    cur=pts
    for _ in range(6):
        variants.append(normalize(cur))
        variants.append(normalize(reflect(p) for p in cur))
        cur=[rotate(p) for p in cur]
    return min(variants)

def generate(max_n):
    levels=[None,{((0,0),)}]
    for n in range(1,max_n):
        nxt=set()
        for shape in levels[n]:
            s=set(shape); border=set()
            for q,r in s:
                for dq,dr in NEIGHBORS:
                    x=(q+dq,r+dr)
                    if x not in s: border.add(x)
            for x in border:
                nxt.add(free_key(s|{x}))
        levels.append(nxt)
    return levels

def degree_counts(shape):
    s=set(shape); out=[]
    for q,r in shape:
        out.append(sum((q+dq,r+dr) in s for dq,dr in NEIGHBORS))
    return out

def is_path(shape):
    n=len(shape)
    if n==1: return True
    deg=degree_counts(shape)
    return deg.count(1)==2 and deg.count(2)==n-2

def is_cycle(shape):
    return len(shape)>=3 and all(d==2 for d in degree_counts(shape))

def main():
    max_n=11
    levels=generate(max_n)
    free_counts=[]; paths=[]; cycles=[]
    for n in range(1,max_n+1):
        shapes=levels[n]
        free_counts.append(len(shapes))
        paths.append(sum(is_path(s) for s in shapes))
        cycles.append(sum(is_cycle(s) for s in shapes))
    print(json.dumps({
        "range":"1..11 (stated minimum)",
        "free_polyhexes":free_counts,
        "inner_dual_path":paths,
        "inner_dual_cycle":cycles,
    },sort_keys=True))

if __name__=="__main__":
    main()
