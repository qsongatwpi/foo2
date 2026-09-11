example (a b : Nat) (h : a = b) : b = a := by
  exact h.symm

example : 2 + 3 = 5 := by
  rfl
