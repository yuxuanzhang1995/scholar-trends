# Open problems & research directions — quantum computing

Curated open problems, each **verified against the 2024–2026 literature** for whether it is still open (verification pass: 2026-06-15). "Status" is honest: *open* = no demonstrated resolution; *advancing* = major recent progress but the core question stands. "Type" = the kind of work that drives progress (theory / numerical / experiment).

"Type" is **lead-first**: the first tag is the kind of work that would most move the problem now; the rest are secondary.

| # | Problem | Area | Status | Lead · also |
|---|---------|------|--------|------|
| 1 | Low-overhead fault tolerance with quantum LDPC codes | Error correction | advancing | **exp** · the · num |
| 2 | Real-time decoding at utility scale | Error correction | advancing | **num** · exp · the |
| 3 | Useful quantum advantage (a valuable problem, not sampling) | Quantum advantage | open | **exp** · the · num |
| 4 | The boundary of classical simulability for noisy circuits | Quantum advantage | open | **the** · num |
| 5 | Quantum machine-learning advantage on classical data | Quantum ML | open | **the** |
| 6 | End-to-end quantum speedup for combinatorial optimization | Algorithms | advancing | **num** · the |
| 7 | From below-threshold memory to sustained logical computation | Error correction / HW | advancing | **exp** · the · num |
| 8 | Resource theory of magic (non-stabilizerness) | Foundations | advancing | **the** · num |
| 9 | Long-distance quantum repeaters / the quantum internet | Networking | open | **exp** · the · num |
| 10 | Fundamental limits of quantum error mitigation | Near-term methods | open | **the** · num |
| 11 | TLS defects limiting superconducting-qubit coherence | Materials / HW | open | **exp** · the · num |

---

### 1. Low-overhead fault tolerance with quantum LDPC codes — *advancing*
**Why it matters:** qLDPC codes promise ~10× fewer physical qubits than the surface code — the single biggest lever for buildable fault tolerance.
**What's done / still open:** First on-device qLDPC *memory* demonstrations landed in 2025 (e.g. a distance-4 bivariate-bicycle code on a 32-qubit superconducting chip), and IBM's roadmap targets the [[144,12,12]] "gross" code by 2029 — but a hardware-validated, low-overhead **universal logical gate set** is still missing.
**Sources:** arXiv:2505.09684 (first qLDPC hardware demo) · IBM large-scale FTQC roadmap.

### 2. Real-time decoding at utility scale — *advancing*
**Why:** If the decoder can't keep pace with ~1 µs syndrome cycles, error data backs up exponentially (the "backlog problem").
**Done / open:** Real-time decoding now works for a single logical qubit (Google, below-threshold, 2024) and for the gross code on FPGAs (IBM, 2025, ~24 ns/iteration). Million-qubit, lattice-surgery-scale decoding latency remains unsolved.
**Sources:** arXiv:2408.13687 · arXiv:2510.21600 · arXiv:2511.10633.

### 3. Useful quantum advantage — *open*
**Why:** Sampling "supremacy" has no application; a verified advantage on a *useful* problem would be quantum computing's first real payoff.
**Done / open:** The strongest candidate — D-Wave's 2025 spin-glass quench simulation (*Science*) — is being actively challenged by classical tensor-network and t-VMC methods; corporate "advantage" claims (HSBC/IBM bonds, IonQ/Ansys) have not survived scrutiny.
**Sources:** DOI 10.1126/science.ado6285 (D-Wave) · arXiv:2503.08247 (classical challenge).

### 4. Boundary of classical simulability for noisy circuits — *open*
**Why:** This boundary defines exactly which experiments could ever show advantage; every near-term claim stands or falls on it.
**Done / open:** Pauli-path and tensor-network methods keep absorbing claimed advantages (IBM's 127-qubit "utility" experiment was reproduced on a laptop). Worst-case, fixed-circuit hardness is not closed, and the simulable region keeps growing.
**Sources:** arXiv:2306.16372 · arXiv:2306.14887 · arXiv:2511.21651.

### 5. Quantum ML advantage on classical data — *open*
**Why:** Decides whether quantum computers can ever beat classical ML on the data businesses and scientists actually have.
**Done / open:** Dequantization (random-Fourier-feature methods) keeps reproducing quantum models on classical data; provable advantages exist only for engineered/quantum-structured tasks, not real-world classical datasets.
**Sources:** arXiv:2505.15902 (dequantization) · arXiv:2203.01340 (Schuld & Killoran critique).

### 6. End-to-end quantum optimization speedup — *advancing*
**Why:** Combinatorial optimization (logistics, scheduling, finance) is the most-pursued near-term commercial case.
**Done / open:** QAOA shows numerical scaling advantage on LABS (*Science Advances* 2024) and DQI claims a superpolynomial speedup on a structured algebraic problem (*Nature* 2025) — but both are structured/contested, with no fault-tolerant, hardware-demonstrated end-to-end win on a practical problem.
**Sources:** arXiv:2308.02342 (QAOA/LABS) · arXiv:2408.08292 (DQI).

### 7. From below-threshold memory to sustained logical computation — *advancing*
**Why:** Crossing from a protected memory to large-scale logical *computation* gates any useful fault-tolerant algorithm.
**Done / open:** Below-threshold memory (Google 2024), logical magic-state distillation (QuEra/Harvard 2024), and 48–96 logical qubits with universal FT gates (Quantinuum/Harvard 2025) are all in; *sustained*, real-time-decoded deep logical circuits at scale are not yet demonstrated.
**Sources:** arXiv:2408.13687 · arXiv:2412.15165 (logical magic distillation).

### 8. Resource theory of magic (non-stabilizerness) — *advancing*
**Why:** Magic sets both the classical-simulation frontier and the dominant fault-tolerant cost (magic-state overhead).
**Done / open:** The stabilizer (Rényi) entropy now has an operational meaning and is measurable; but magic is provably *necessary-not-sufficient* for advantage, and the exact criterion (magic + entanglement/structure) is unsettled.
**Sources:** arXiv:2507.22883 · arXiv:2508.20252.

### 9. Long-distance quantum repeaters / the quantum internet — *open*
**Why:** A working repeater network is the prerequisite for a quantum internet (secure comms, distributed QC, networked sensors).
**Done / open:** A key single-link milestone arrived in 2026 — trapped-ion memory–memory entanglement over 10 km of fibre that survives longer than it takes to establish (USTC, *Nature*). No multi-hop chain with entanglement swapping + purification yet exists.
**Sources:** DOI 10.1038/s41586-026-10177-4 · arXiv:2502.01653 (quantum-internet review).

### 10. Fundamental limits of quantum error mitigation — *open*
**Why:** Mitigation is the bridge before fault tolerance; knowing where it provably breaks dictates which near-term advantage claims are even possible.
**Done / open:** Worst-case exponential/superpolynomial sampling lower bounds are proven (*Nature Physics* 2024); the precise boundary of *useful* regimes and the mitigation→correction crossover remain open.
**Sources:** arXiv:2210.11505 · arXiv:2208.09178.

### 11. TLS defects limiting superconducting-qubit coherence — *open*
**Why:** Two-level-system loss worsens as processors scale, capping reproducible high-coherence devices and inflating QEC overhead.
**Done / open:** Individual TLS can now be localized and imaged on chips (2025) and Ta-on-Si transmons passed T1 > 1 ms, but the microscopic chemical identity of TLS and a systematic suppression route are unsolved.
**Sources:** arXiv:2511.05365 (TLS mapping) · arXiv:2405.09842 (Ta vs Nb TLS).

---

*Each entry was verified by searching 2024–2026 literature for resolutions/breakthroughs before being listed; treat the linked papers as primary sources. Statuses are point-in-time (2026-06-15) and will drift as the field moves.*
