# The Wolves and the Clock

### The sieve as a hunt, the primes as a renewal

Allen Proxmire · July 2026

> **What this is.** A *model / interpretation* note — a faithful picture of the sieve, not a new theorem. Its mechanism is the Sieve of Eratosthenes; its value is that one image holds the finitism, the $p^2$ activation, the $\sqrt n$ horizon, the Factor Skyline, and Bertrand/TPB together without contradiction — and reframes "generating primes" as **a renewal process, not a formula.** Tags: **[fact]** established · **[model]** faithful picture · **[open]** the direction to chase.

---

## 1. The hunt

**[model]** Picture a **slow, steady reader** moving through the integers in order — the arrow of time, counting each number into existence. At every **square** $p^2$, a **wolf** is released: wolf $p$. All the wolves run at **the same speed** — they sit at the reading frontier and claim (bite) their own multiples as the reader passes them. Each number the reader reaches is either **already claimed** by some wolf (composite) or **a crumb the wolves missed** (prime).

Three things make this exact, not just evocative:

- **Why the wolf is released at $p^2$.** Every earlier multiple of $p$ — $2p, 3p, \dots, (p-1)p$ — was already eaten by a *smaller* wolf (whichever prime is its least factor). The first multiple of $p$ no smaller wolf can reach is $p\cdot p = p^2$. So $p^2$ is where wolf $p$ first finds unclaimed prey. **[fact]** (This is exactly why real sieve code starts crossing out at $p^2$.)
- **Same speed = the speed of influence.** The wolves claim in real time as the frontier passes; nothing is struck out instantly across an infinite stretch. At any tick, only finitely many bites have happened — the hunt is always mid-stride, never finished. This is the finitist stance from [`Counting_Into_Existence.md`](Counting_Into_Existence.md): no completed infinities, only an accruing history.
- **The $\sqrt n$ horizon falls out.** When the reader reaches $n$, only the wolves already *released* — those with $p^2 \le n$, i.e. $p \le \sqrt n$ — can claim it. A number's primality is decided by precisely the wolves that have had time to reach it. That is the causal horizon and the parity-barrier wall, in one line.

## 2. The hunt *is* the Factor Skyline

**[fact]** When the reader finds $n$ claimed, *which* wolf got it? The **smallest** prime dividing $n$ — released earliest, arriving first. So every number is stamped with its **least prime factor**, and $\mathrm{lpf}(n)$ is exactly the **width coordinate of the Factor Skyline**. The wolves painting each number with their identity *is the skyline being built, live*; the crumbs are the primes, which in the skyline are the numbers that **escape to the diagonal**. The hunt and the coordinate system are the same object — the skyline is the frozen photograph of the hunt.

| in the hunt | in the mathematics |
|---|---|
| reader moving in order | the arrow of time / counting into existence |
| wolves released at $p^2$ | sieve activation (the squared-prime sweeps) |
| all wolves same speed | finite speed of influence — no completed infinity |
| only released wolves can claim | the $\sqrt n$ horizon / parity-barrier wall |
| each number stamped by its smallest wolf | least prime factor = Factor Skyline width |
| the crumbs | primes = escapes to the diagonal |

## 3. The clock — and the point of the whole thing

Now the reframe that matters, in your words:

> **It is a renewal process, not a generator.** You don't build primes by a rule — the primes are the **reset points of a clock that keeps trying to double and keeps getting interrupted.** That is the constructive/generative view done right: a process of *interruptions*, not a formula.

Here is why that is exactly right and not loose talk. The doubling window $(P, 2P)$ is a clock that *would* tick one full turn — one octave — if it ran to completion. **It never does.** A prime always appears inside it and resets it before $2P$. That is Bertrand's postulate as a dynamical law, and its minimal form is literally

$$p_{n+1} < 2\,p_n \qquad\text{(the next prime always before }2P\text{).}$$

Tighten "a prime resets it" to "a *twin* resets it" and you get $T_{k+1} < 2T_k$ — **the Twin-Prime Bertrand Postulate.** So the primes are not *produced* by a rule; they are the **interruption points** of the doubling clock, and their spacing law is Bertrand (and, in the strong form, TPB). Every failed generator we tried — the mod-10 square, the 1,3,5,7,9 circle, the +5 adjustment — failed because it looked for a *formula*. The honest object was never a formula. It was **this**: a clock that keeps getting interrupted, and the interruptions are what we call primes.

## 4. The direction to chase

**[open]** *This is what should be chased next, if it can be:* make the **renewal process** precise.

The honest scope, so the chase is real and not a wild goose:

- **As a *generator* it is impossible** — the interruptions *are* the primes, so any rule that names the next reset has smuggled the primes in (self-reference). This is the same wall as "sieves survive but never generate." Do not chase a formula.
- **As a *statistical* renewal it is real and half-built.** Model the reset points as a renewal process and ask for the law of the reset-gaps. That law is **not** memoryless — the gaps carry the $-0.05$ one-step memory (the [angle note](Twin%20Bertrand/papers/PG_Angle_Wobble.md)) and the full offset-correlation comb (the [offset note](Twin%20Bertrand/papers/Offset_Correlation_Curve.md)), both of which are **Hardy–Littlewood = the wheel.** So "chasing the renewal" concretely means: **characterize the interruption process** — its gap distribution, its (mild) memory, its scale-collapse — as a wheel-driven renewal. That is the Cramér/Hardy–Littlewood program, seen as a *process of interruptions* rather than a static conjecture, and pieces of it are already measured in this collection.

The target, stated plainly: **a renewal model of the primes in which the wolf-hunt (the sieve, at finite speed) is the driving process, the doubling clock is the thing being interrupted, Bertrand/TPB is the interruption guarantee, and the wheel is the statistics of the interruptions.** If the whole program has a next step that is *constructive without being a formula*, it is this.

---

## Companions

- [`Counting_Into_Existence.md`](Counting_Into_Existence.md) — the finitist ontology (sieve at the speed of influence; primality as event).
- [`One_Wheel_Many_Shadows.md`](One_Wheel_Many_Shadows.md) — the wheel as the single generator behind the shadows.
- *Prime-Triangle Angle* and *Offset-Correlation Curve* (Twin Bertrand) — the measured statistics of the interruptions.
- Twin Bertrand (PG II) — $T_{k+1} < 2T_k$, the strong interruption law.
