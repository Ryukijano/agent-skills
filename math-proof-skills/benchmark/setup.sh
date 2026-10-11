#!/usr/bin/env bash
# Pins openai/math and writes text-only agent inputs to run/inputs/<id>/.
# Needs git and pdftotext (poppler-utils). The source map lives here, not in cases.yaml.
set -euo pipefail
HERE=$(cd "$(dirname "$0")" && pwd); CORPUS=${CORPUS:-$HERE/run/openai-math}; OUT=$HERE/run/inputs
FIX=fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb; PRE=adc7f1241b42e322a6451854ab7e4b4c146bf78a
[ -d "$CORPUS/.git" ] || git clone -q https://github.com/openai/math "$CORPUS"
git -C "$CORPUS" fetch -q origin "$FIX" "$PRE" 2>/dev/null || true
git -C "$CORPUS" checkout -q "$FIX"
rm -rf "$OUT"; mkdir -p "$OUT"
pdf() { mkdir -p "$OUT/$1"; git -C "$CORPUS" show "$2:$3" > "$OUT/$1/.src.pdf"; pdftotext -layout "$OUT/$1/.src.pdf" "$OUT/$1/paper.txt"; rm "$OUT/$1/.src.pdf"; }
lean() { mkdir -p "$OUT/$1"; git -C "$CORPUS" show "$FIX:lean/ComparatorChallenges/$2" > "$OUT/$1/$3"; }
P=preprints
pdf F1 $FIX $P/An-explicit-noncoordinate-polynomial-with-affine-three-space-zero-fibre-September-24-2026/paper.pdf
lean F1 AbhyankarSathaye.lean challenge.lean
pdf F2 $FIX $P/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/paper.pdf
lean F2 ArnoldCounterexample.lean challenge.lean
pdf F3 $FIX $P/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026.pdf
lean F3 BinPackingGap.lean challenge.lean
pdf C1 $FIX $P/Gaussian-free-field-limits-of-weighted-integer-Lipschitz-heights-September-25-2026/paper.pdf
pdf C2 $FIX $P/Uniform-real-Lipschitz-surfaces-on-the-triangular-lattice-September-25-2026/paper.pdf
pdf C3 $FIX $P/Termination-of-generalized-canonical-flips-on-compact-Kahler-fourfolds-October-5-2026/termination-generalized-terminal-flips-compact-kahler-fourfolds.pdf
pdf W1 $PRE $P/Algebraicity-of-Weil-classes-on-split-abelian-eightfolds-September-18-2026/paper.pdf
pdf W2 $PRE $P/The-rational-Hodge-conjecture-for-products-of-K3-surfaces-October-4-2026/hodge-conjecture-products-k3.pdf
lean R1 ErdosReciprocal.lean statement.lean
lean R2 MahlerConjecture.lean statement.lean
# Strip anything that names the version/withdrawal status from extracted text headers.
echo "Inputs written to $OUT. Give the agent only $OUT/<id>/ (no corpus, no answers/)."
