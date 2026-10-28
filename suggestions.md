# Suggestions

Ideas for simplifying or unifying the textbook that came up while converting the scans. They are **not applied** unless the status says so. The scans stay the reference (see practice 1 in `CLAUDE.md`), and the redundancy in them is on purpose. Add new entries at the end, newest last. Status: `open`, `accepted`, `rejected`, `applied`.

Entry format: `## S<n> <chapter>: <title>`, then *Status*, *What*, *Why*, *Cost*.

## S1 Filtre_I: one generic set of filter figures with ω₀
- *Status:* open. Was applied in the first pilot version by mistake, before practice 1 was agreed. `Filtre_I.md` was redone strictly from the scans, so this is not applied now.
- *What:* Instead of a separate figure per filter (RC low-pass, RC high-pass, RL high-pass, RL low-pass), the pilot draws one low-pass and one high-pass figure with `ω₀` (= 1/RC or R/L). Characteristic frequencies and plots appear once per filter type.
- *Why:* The RC and RL filters of the same type have identical transfer functions, so 14 diagrams reduce to 6 and the "same shape, different constant" fact becomes explicit.
- *Cost:* Students lose the repetition of the derivation with the concrete symbols (`1/RC`, `R/L`) in the plots.

## S2 Filtre_I: amplitude and phase plots in one figure
- *Status:* open. Not applied now: the scans draw |H| and φ as two separate plots, so there are two figures per filter.
- *What:* |H| and φ share one SVG with a common ω axis, instead of two separate drawings per filter.
- *Why:* The two curves are read together (the corner frequency lines up in both).

## S3 Filtre_I: HPF magnitude and phase formulas
- *Status:* open. Not applied now: the RC high-pass section has plots without formulas, as in the scan.
- *What:* The RC scan gives only plots for the high-pass |H| and φ, the RL scan gives the formulas (`1/√(1+ω₀²/ω²)`, `arctg(ω₀/ω)`). The first pilot version wrote them once for all four filters.
- *Why:* The formulas are the same and follow from the transfer function.

## S4 Filtre_RL.png: corner value of the low-pass magnitude plot
- *Status:* open (typo in the notes).
- *What:* The RL scan marks the corner value of the low-pass |H| plot as "1/2". The correct value is `1/√2` (the RC scan and the formula agree). Figures use `1/√2`. Fix the handwritten scan if it will be published.

## S5 Repo: `requirements.txt` and the `mkdocs` command
- *Status:* open.
- *What:* `requirements.txt` lists only `mkdocs` and `python-markdown-math`, but the build needs mkdocs-material, pymdown-extensions and mkdocs-encryptcontent-plugin. The `mkdocs` command on PATH is broken (it finds no packages), only `/opt/miniconda3/bin/python -m mkdocs` works. A fresh clone could not build the site.

## S6 Filtre_I: the two empty summary headings
- *Status:* open.
- *What:* The skeleton has two headings at the end, "Dolnopriepustné filtre RC, LR" and "Hornopriepustné filtre CR, RL", with no scan content. They stay empty. A short side-by-side comparison of the four filters could go there (same transfer function with `ω₀ = 1/RC` or `R/L`), or the headings could be removed.

## S7 Filtre_I: order of the RC derivation
- *Status:* open.
- *What:* In the RC scan the first derivation line writes `U = U_C + U_R`, in the RL scan `U = U_R + U_L`. The chapter keeps both orders as in the scans. Using one order (resistor first) would make the two derivations line up.
