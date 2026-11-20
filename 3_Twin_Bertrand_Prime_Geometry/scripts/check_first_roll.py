"""Twin Bertrand §1.5: the first-roll rule. For each epoch [p^2, p'^2) below 1e10, roll the largest wheel whose turn fits,
once from p^2, and count the twin primes among its guaranteed twin-open slots. numpy; ~1.5 min, ~1 GB RAM."""
import numpy as np, time
from math import prod
N=10**10; SEG=10**7
r=int(N**.5)+3; s=np.ones(r+1,bool); s[:2]=False
for p in range(2,int(r**.5)+1):
    if s[p]: s[p*p::p]=False
small=np.nonzero(s)[0]
TW=[]
for lo in range(0,N,SEG):
    hi=min(lo+SEG+2,N+3); seg=np.ones(hi-lo,bool)
    if lo==0: seg[:2]=False
    for p in small:
        if p*p>=hi: break
        st=max(p*p,((lo+p-1)//p)*p); seg[st-lo::p]=False
    t=np.nonzero(seg[:-2]&seg[2:])[0]; t=t[t<SEG]+lo; TW.append(t)
TW=np.concatenate(TW)
PR=[2,3,5,7,11,13,17,19,23]; W=[prod(PR[:k]) for k in range(1,len(PR)+1)]
P=small; C2=0.6601618; rows=[]
for a,b in zip(P[:-1],P[1:]):
    lo,hi=int(a)**2,int(b)**2
    if hi>N: break
    L=hi-lo; k=max(i for i in range(len(W)) if W[i]<=L); M=W[k]
    cand=prod(q-2 for q in PR[1:k+1])
    found=np.searchsorted(TW,lo+M)-np.searchsorted(TW,lo)
    exp=2*C2*M/np.log(lo)**2
    rows.append((a,PR[k],M,cand,found,exp))
R=np.array(rows,dtype=float)
print('epochs',len(R),' first rolls with no twin:',int((R[:,4]==0).sum()),'at p =',[int(x) for x in R[R[:,4]==0,0]])
for t in (5,7,11,13,17,19):
    m=R[:,1]==t
    if m.sum():
        f=R[m,4]; e=R[m,5]; i=np.argmin(f/e)
        print('wheel to %2d: %5d epochs (p %d..%d), slots %d, found min %d mean %.0f, hit %.1f%%, worst found/expected %.2f at p=%d'%(t,m.sum(),R[m,0].min(),R[m,0].max(),R[m,3][0],f.min(),f.mean(),100*f.mean()/R[m,3][0],(f/e)[i],R[m,0][i]))
