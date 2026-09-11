/-!
# First Lean proofs

Change `by` blocks below, or add your own `example` statements.
-/

-- `rfl` proves equality by computation or definition.
example (n : Nat) : n + 0 = n := by
  rfl

-- A hypothesis is itself a proof that can be used with `exact`.
example (a b : Nat) (h : a = b) : b = a := by
  exact h.symm

-- This exchanges the final two addends using core Natural Number lemmas.
example (a b c : Nat) : a + b + c = a + c + b := by
  calc
    a + b + c = a + (b + c) := Nat.add_assoc a b c
    _ = a + (c + b) := by rw [Nat.add_comm b c]
    _ = a + c + b := (Nat.add_assoc a c b).symm

-- Try this yourself: replace `by sorry` with a proof.
example (P Q : Prop) (hP : P) (hQ : Q) : P ∧ Q := by
  constructor
  · exact hP
  · exact hQ
