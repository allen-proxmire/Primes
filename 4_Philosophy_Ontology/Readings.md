# Readings

### The sieve as a hunt, the primes as interruptions, and numbers counted into existence

Allen Proxmire

These are interpretations, not mathematics. Nothing here changes which numbers are prime or any result in the collection, and nothing here is cited as evidence elsewhere. Tags: **[stance]** a position taken · **[fact]** established · **[open]** an unpaid debt.

---

## 1. The hunt

**The picture.** A reader moves through the integers in order. At each square $p^2$ a wolf $p$ is released; all wolves run at the reader's speed and bite their own multiples as the reader passes. A number already bitten is composite; a number no wolf has bitten is prime.

Three features are exact:

- **Release at $p^2$.** Every multiple $2p, \dots, (p-1)p$ was already bitten by a smaller wolf; $p^2$ is the first a smaller wolf cannot reach. **[fact]** (This is why sieve code starts at $p^2$.)
- **The $\sqrt n$ horizon.** When the reader reaches $n$, only wolves with $p^2 \le n$ have been released, so primality is decided by exactly the primes up to $\sqrt n$. **[fact]**
- **The hunt draws the Factor Skyline.** A bitten number was bitten first by its smallest wolf, so each number is stamped with its least prime factor — the skyline's width. The skyline is a photograph of the hunt; the unbitten numbers escape to the diagonal. **[fact]**

| in the hunt | in the mathematics |
|---|---|
| reader moving in order | counting |
| wolves released at $p^2$ | sieve activation |
| only released wolves can bite | the $\sqrt n$ horizon |
| stamped by the smallest wolf | least prime factor = skyline width |
| the numbers no wolf bites | primes = escapes to the diagonal |

---

## 2. The clock

**[stance]** The primes are not produced by a rule. They are the **reset points of a clock that keeps trying to double** and keeps being interrupted. The window $(P, 2P)$ would complete one octave if it ran out; it never does, because a prime always arrives first:
$$p_{n+1} < 2p_n \qquad\text{(Bertrand)}.$$
Ask that a *twin* always arrives first and it is
$$T_{k+1} < 2T_k \qquad\text{(the Twin-Prime Bertrand Postulate)}.$$

**What can be chased, and what cannot.** As a *generator* the picture is empty: a rule naming the next reset would already contain the primes. As a *statistical renewal* it is real: the reset gaps are not memoryless — they carry the $-0.05$ lag-1 anti-correlation and the offset comb, both the wheel ([Gap Correlations](../2_One_Wheel_Many_Shadows/Gap_Correlations.md), [The Prime Crystal](../2_One_Wheel_Many_Shadows/Prime_Crystal.md)). **[open]** A renewal model in which the sieve drives, the doubling clock is interrupted, Bertrand and TPB are the interruption guarantees, and the wheel is the statistics of the interruptions.

---

## 3. Counting into existence

**[stance]** There are no completed infinities in reality — only as many numbers as there have been events. Numbers are potentially infinite (never a last one) but never actually infinite (never all of them at once). This is Aristotle's potential infinity, held by Gauss, Brouwer and Weyl, and defended as strict finitism by Zeilberger and Nelson.

- **The boundary accrues.** "Where is the last number?" has no answer because the frontier moves with history; there is no stipulated cutoff to defend. **[fact]** It is physically bounded: Lloyd's estimate caps the operations performed since the Big Bang at $\sim 10^{120}$ on $\sim 10^{90}$ bits.
- **Numbers are acts.** A number is an event, not a stored object, so the count needs no ledger: it is a fact about how far history has got.
- **The sieve at a finite speed.** The textbook sieve hides one completed infinity: striking out $\{p^2, p^2+p, \dots\}$ all at once. Let each wolf advance at a finite speed instead and the infinity is gone — at any moment only finitely many bites have happened. Primality becomes an event, settled when every wolf that can reach $n$ has arrived, and the $\sqrt n$ horizon reads as a causal horizon.

**The costs, kept in the same place.**

- **[fact]** It is interpretation: same primes, different account of what a prime is.
- **[open]** The speed is a postulate. "Finite" does all the work; any attempt to give it a value is numerology.
- **[open]** Reading every "for all primes" as a rule over whatever is instantiated (Brouwer–Weyl) costs the law of the excluded middle over infinite domains. TPB becomes a statement about how far the sieve will go.
- **[open]** Infinite mathematics works: assume infinitely many primes, do analysis over the reals, and predict finite facts correctly. The finitist owes an account of why the fiction pays rent. "A lossless-enough compression" is a promissory note.

---

See also: [The Primes in Plain Language](Primes_in_Plain_Language.md) — the plain-language picture of the whole collection.
