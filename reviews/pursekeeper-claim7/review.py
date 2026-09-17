#!/usr/bin/env python3
import json
from collections import Counter, defaultdict

ORTHO = ((1,0),(-1,0),(0,1),(0,-1))
KNIGHT = {(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)}

def transforms(p):
    x,y=p
    return ((x,y),(x,-y),(-x,y),(-x,-y),(y,x),(y,-x),(-y,x),(-y,-x))

def normalize(points):
    pts=list(points)
    minx=min(x for x,y in pts); miny=min(y for x,y in pts)
    return tuple(sorted((x-minx,y-miny) for x,y in pts))

def free_key(points):
    pts=list(points)
    variants=[]
    for k in range(8):
        variants.append(normalize(transforms(p)[k] for p in pts))
    return min(variants)

def free_polyominoes(n):
    shapes={((0,0),)}
    for size in range(1,n):
        nxt=set()
        for shape in shapes:
            s=set(shape)
            border=set()
            for x,y in s:
                for dx,dy in ORTHO:
                    q=(x+dx,y+dy)
                    if q not in s: border.add(q)
            for q in border:
                nxt.add(free_key(s|{q}))
        shapes=nxt
    return shapes

def automorphisms(shape):
    shape_set=set(shape)
    out=[]
    for k in range(8):
        raw=[transforms(p)[k] for p in shape]
        minx=min(x for x,y in raw); miny=min(y for x,y in raw)
        mapped=tuple((x-minx,y-miny) for x,y in raw)
        if set(mapped)==shape_set:
            out.append((k,minx,miny))
    return out

def transform_path(path, auto):
    k,minx,miny=auto
    out=[]
    for p in path:
        x,y=transforms(p)[k]
        out.append((x-minx,y-miny))
    return tuple(out)

def canonical_tour(path, autos):
    reps=[]
    for a in autos:
        q=transform_path(path,a)
        reps.append(min(q,tuple(reversed(q))))
    return min(reps)

def tour_count(shape):
    pts=list(shape); idx={p:i for i,p in enumerate(pts)}
    adj=[[] for _ in pts]
    for i,(x,y) in enumerate(pts):
        for dx,dy in KNIGHT:
            j=idx.get((x+dx,y+dy))
            if j is not None: adj[i].append(j)
    autos=automorphisms(shape)
    tours=set(); n=len(pts)
    def dfs(path, used):
        if len(path)==n:
            coords=tuple(pts[i] for i in path)
            tours.add(canonical_tour(coords,autos)); return
        for j in adj[path[-1]]:
            if not (used>>j)&1:
                dfs(path+[j],used|(1<<j))
    for i in range(n): dfs([i],1<<i)
    return len(tours)

def frame(shape):
    w=max(x for x,y in shape)+1; h=max(y for x,y in shape)+1
    return tuple(sorted((w,h)))

def main():
    shapes=free_polyominoes(9)
    qualifying=[]
    for shape in sorted(shapes):
        t=tour_count(shape)
        if t:
            qualifying.append((shape,t,frame(shape)))
    by_tour=Counter(t for _,t,_ in qualifying)
    by_frame=defaultdict(lambda:[0,0])
    for _,t,f in qualifying:
        by_frame[f][0]+=1; by_frame[f][1]+=t
    fourfour=Counter(t for _,t,f in qualifying if f==(4,4))
    out={
        "free_9_ominoes":len(shapes),
        "boards":len(qualifying),
        "tours":sum(t for _,t,_ in qualifying),
        "boards_by_tours":dict(sorted(by_tour.items())),
        "frames":{f"{a}x{b}":v for (a,b),v in sorted(by_frame.items())},
        "frame_4x4_by_tours":dict(sorted(fourfour.items())),
    }
    print(json.dumps(out,sort_keys=True))

if __name__=="__main__":
    main()
