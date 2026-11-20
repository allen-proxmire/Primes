"""Twin Bertrand §1.5: the epoch share e^{2gamma}/4, the position profile e^{2gamma}/u^2, the 210-wheel and prior-wheel hit rates,
and the quadruplet check. Run check_epoch_twins.py first (it writes epoch_cnt.npy, epoch_sq.npy). numpy; ~1 min."""
import numpy as np
c=np.load('epoch_cnt.npy'); S=np.load('epoch_sq.npy')
p=np.sqrt(S[:-1].astype(float)).round().astype(int); L=(S[1:]-S[:-1]).astype(float); c=c[:-1]
# exact turn-wide twin-open density of the wheel to p: (1/2) prod_{3<=q<=p} (1-2/q)
d=np.cumprod(np.where(p>2,1-2/p,1.0))*0.5
r=c/(L*d)
eg=np.exp(2*np.euler_gamma)
print('A. epoch [p^2,p\'^2): twins found / (turn-wide twin-open density x epoch length)')
for a,b in [(10,100),(100,1000),(1000,10000),(10000,100000)]:
    m=(p>=a)&(p<b); print('   p in [%d,%d): pooled ratio %.3f   (prediction e^{2gamma}/4 = %.3f)'%(a,b,c[m].sum()/(L[m]*d[m]).sum(),eg/4))
# B. the start of the turn (p, 2p] and position by position
N=2_100_000; s=np.ones(N+3,bool); s[:2]=0
for q in range(2,1500):
    if s[q]: s[q*q::q]=0
tw=s[:N+1]&s[2:N+3]; T=np.concatenate([[0],np.cumsum(tw)])
P=np.nonzero(s[:1450])[0]
dd={int(q):x for q,x in zip(P,np.cumprod(np.where(P>2,1-2/P,1.0))*0.5)}
print('\nB. pooled over wheels p in [100,1450): twin-open slots that are twin primes, by position u = log n / log p')
ps=[int(q) for q in P if q>=100]
for u0,u1 in [(1,1.15),(1.15,1.3),(1.3,1.5),(1.5,1.7),(1.7,1.9),(1.9,2.0)]:
    num=0;den=0
    for q in ps:
        a=int(q**u0)+1; b=min(int(q**u1),N-2)
        if b<=a: continue
        num+=T[b]-T[a]; den+=(b-a)*dd[q]
    print('   n in (p^%.2f, p^%.2f]: ratio %.3f   prediction e^{2g}/u^2 at mid = %.3f'%(u0,u1,num/den,eg/((u0+u1)/2)**2))
print('   crossover (ratio 1) predicted at u = e^gamma = %.2f'%np.exp(np.euler_gamma))
# C. prior wheel / 210 wheel hit rates inside epochs
print('\nC. inside epoch of p: share of a smaller wheel\'s twin-open slots that are twin primes')
for q in (101,307,1009):
    i=list(P).index(q); a,b=q*q,P[i+1]**2
    n=np.arange(a,b-2); twp=tw[a:b-2].sum()
    def topen(pr): 
        ok=np.ones(len(n),bool)
        for z in pr: ok&=(n%z!=0)&((n+2)%z!=0)
        return ok.sum()
    prev=topen(P[P<q]); w210=topen([2,3,5,7])
    print('   p=%4d: twin primes %4d | prior wheel (to %d) slots %4d -> hit %.1f%% (1-2/p = %.1f%%) | 210-wheel slots %5d -> hit %.1f%%'%(q,twp,P[i-1],prev,100*twp/prev,100*(1-2/q),w210,100*twp/w210))
# D. quadruplets {0,2,6,8}: open in every turn, yet absent from many epochs
Q=np.nonzero(s[:N-8]&s[2:N-6]&s[6:N-2]&s[8:N])[0]; emp=tot=0
for a,b in zip(P[:-1],P[1:]):
    if b*b>N: break
    tot+=1; emp+= not np.any((Q>=a*a)&(Q+8<b*b))
print('\nD. epochs below %d: %d, with no prime quadruplet: %d'%(N,tot,emp))
