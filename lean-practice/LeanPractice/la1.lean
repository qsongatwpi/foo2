import Mathlib.Analysis.InnerProductSpace.PiL2

example (v : ℝ × ℝ) : v = (v.1, v.2) := by
  cases v
  rfl

/-- The Pythagorean theorem in `ℝⁿ`. -/
example {n : ℕ} (u v : EuclideanSpace ℝ (Fin n))
    -- This is the dot product `u · v = 0`, i.e. `u` is perpendicular to `v`.
    (h : @inner ℝ _ _ u v = 0) :
    ‖u‖ ^ 2 + ‖v‖ ^ 2 = ‖u + v‖ ^ 2 := by
  simpa [pow_two] using
    (norm_add_sq_eq_norm_sq_add_norm_sq_of_inner_eq_zero u v h).symm
