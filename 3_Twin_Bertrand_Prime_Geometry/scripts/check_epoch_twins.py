"""Twin Bertrand §1.5: twin primes in every epoch [p^2, p'^2) below 1e10 (segmented sieve, numpy, ~2 min)."""
import numpy as np, time, sys
N=10**10; SEG=10**7
r=int(N**.5)+2
s=np.ones(r+1,bool); s[:2]=False
for p in range(2,int(r**.5)+1):
    if s[p]: s[p*p::p]=False
P=np.nonzero(s)[0]
SQ=P.astype(np.int64)**2                     # epoch boundaries
SQ=SQ[SQ<=N+2]
cnt=np.zeros(len(SQ),np.int64)               # cnt[i]: twins t with SQ[i]<=t, t+2<SQ[i+1]
small=P[P<=int((N+2)**.5)]
prev=None; t0=time.time()
for lo in range(0,N+2,SEG):
    hi=min(lo+SEG+2,N+3)                     # overlap 2 so twins straddling a boundary are seen once
    seg=np.ones(hi-lo,bool)
    if lo==0: seg[:2]=False
    for p in small:
        if p*p>=hi: break
        st=max(p*p,((lo+p-1)//p)*p)
        seg[st-lo::p]=False
    tw=np.nonzero(seg[:-2]&seg[2:])[0][:min(SEG,hi-lo-2)]+lo
    tw=tw[tw<min(lo+SEG,N)]
    idx=np.searchsorted(SQ,tw,side='right')-1
    ok=(idx>=0)&(idx<len(SQ)-1)
    ok&=(tw+2<SQ[np.minimum(idx+1,len(SQ)-1)])
    np.add.at(cnt,idx[ok],1)
np.save('epoch_cnt.npy',cnt); np.save('epoch_sq.npy',SQ)
print('done',round(time.time()-t0))
C2=0.6601618; c=cnt[:-1]; lo=SQ[:-1].astype(float); hi=SQ[1:].astype(float); p=np.sqrt(lo)
e=2*C2*(hi-lo)/np.log(lo)**2; r=c/e
print('epochs',len(c),' empty',int((c==0).sum()))
for a,b in [(2,100),(100,1000),(1000,10000),(10000,100000)]:
    m=(p>=a)&(p<b); i=np.argmin(r[m])
    print('p in [%d,%d): %d epochs, fewest %d, worst ratio %.2f at p=%d'%(a,b,m.sum(),c[m].min(),r[m][i],p[m][i]))
