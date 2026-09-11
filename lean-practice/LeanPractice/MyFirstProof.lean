example (a b : Nat) (h : a = b) : b = a := by
  exact h.symm

example : 2 + 3 = 5 := by
  rfl

example (a b c : Nat) : a + b + c = b + a + c := by
  rw [Nat.add_comm a b]

example (a b c : Nat) : a + b + c = a + c + b := by
  rw [Nat.add_assoc]
  rw [Nat.add_comm b c]
  rw [← Nat.add_assoc]
