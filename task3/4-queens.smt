(declare-fun p (Int Int) Bool)
(assert (and
(or (p 1 1) (p 1 2) (p 1 3) (p 1 4))
(or (p 2 1) (p 2 2) (p 2 3) (p 2 4))
(or (p 3 1) (p 3 2) (p 3 3) (p 3 4))
(or (p 4 1) (p 4 2) (p 4 3) (p 4 4))
(or (not (p 1 1)) (not (p 1 2)))
(or (not (p 1 1)) (not (p 1 3)))
(or (not (p 1 1)) (not (p 1 4)))
(or (not (p 1 2)) (not (p 1 3)))
(or (not (p 1 2)) (not (p 1 4)))
(or (not (p 1 3)) (not (p 1 4)))
(or (not (p 2 1)) (not (p 2 2)))
(or (not (p 2 1)) (not (p 2 3)))
(or (not (p 2 1)) (not (p 2 4)))
(or (not (p 2 2)) (not (p 2 3)))
(or (not (p 2 2)) (not (p 2 4)))
(or (not (p 2 3)) (not (p 2 4)))
(or (not (p 3 1)) (not (p 3 2)))
(or (not (p 3 1)) (not (p 3 3)))
(or (not (p 3 1)) (not (p 3 4)))
(or (not (p 3 2)) (not (p 3 3)))
(or (not (p 3 2)) (not (p 3 4)))
(or (not (p 3 3)) (not (p 3 4)))
(or (not (p 4 1)) (not (p 4 2)))
(or (not (p 4 1)) (not (p 4 3)))
(or (not (p 4 1)) (not (p 4 4)))
(or (not (p 4 2)) (not (p 4 3)))
(or (not (p 4 2)) (not (p 4 4)))
(or (not (p 4 3)) (not (p 4 4)))
(or (p 1 1) (p 2 1) (p 3 1) (p 4 1))
(or (p 1 2) (p 2 2) (p 3 2) (p 4 2))
(or (p 1 3) (p 2 3) (p 3 3) (p 4 3))
(or (p 1 4) (p 2 4) (p 3 4) (p 4 4))
(or (not (p 1 1)) (not (p 2 1)))
(or (not (p 1 1)) (not (p 3 1)))
(or (not (p 1 1)) (not (p 4 1)))
(or (not (p 2 1)) (not (p 3 1)))
(or (not (p 2 1)) (not (p 4 1)))
(or (not (p 3 1)) (not (p 4 1)))
(or (not (p 1 2)) (not (p 2 2)))
(or (not (p 1 2)) (not (p 3 2)))
(or (not (p 1 2)) (not (p 4 2)))
(or (not (p 2 2)) (not (p 3 2)))
(or (not (p 2 2)) (not (p 4 2)))
(or (not (p 3 2)) (not (p 4 2)))
(or (not (p 1 3)) (not (p 2 3)))
(or (not (p 1 3)) (not (p 3 3)))
(or (not (p 1 3)) (not (p 4 3)))
(or (not (p 2 3)) (not (p 3 3)))
(or (not (p 2 3)) (not (p 4 3)))
(or (not (p 3 3)) (not (p 4 3)))
(or (not (p 1 4)) (not (p 2 4)))
(or (not (p 1 4)) (not (p 3 4)))
(or (not (p 1 4)) (not (p 4 4)))
(or (not (p 2 4)) (not (p 3 4)))
(or (not (p 2 4)) (not (p 4 4)))
(or (not (p 3 4)) (not (p 4 4)))
;-------------------------------
(or (not (p 1 1)) (not (p 2 2)))
(or (not (p 1 2)) (not (p 2 1)))
(or (not (p 1 2)) (not (p 2 3)))
(or (not (p 1 3)) (not (p 2 2)))
(or (not (p 1 3)) (not (p 2 4)))
(or (not (p 1 4)) (not (p 2 3)))
(or (not (p 1 1)) (not (p 3 3)))
(or (not (p 1 2)) (not (p 3 4)))
(or (not (p 1 3)) (not (p 3 1)))
(or (not (p 1 4)) (not (p 3 2)))
(or (not (p 1 1)) (not (p 4 4)))
(or (not (p 1 4)) (not (p 4 1)))
(or (not (p 2 1)) (not (p 3 2)))
(or (not (p 2 2)) (not (p 3 1)))
(or (not (p 2 2)) (not (p 3 3)))
(or (not (p 2 3)) (not (p 3 2)))
(or (not (p 2 3)) (not (p 3 4)))
(or (not (p 2 4)) (not (p 3 3)))
(or (not (p 2 1)) (not (p 4 3)))
(or (not (p 2 2)) (not (p 4 4)))
(or (not (p 2 3)) (not (p 4 1)))
(or (not (p 2 4)) (not (p 4 2)))
(or (not (p 3 1)) (not (p 4 2)))
(or (not (p 3 2)) (not (p 4 1)))
(or (not (p 3 2)) (not (p 4 3)))
(or (not (p 3 3)) (not (p 4 2)))
(or (not (p 3 3)) (not (p 4 4)))
(or (not (p 3 4)) (not (p 4 3)))
))
(check-sat)
(get-model)