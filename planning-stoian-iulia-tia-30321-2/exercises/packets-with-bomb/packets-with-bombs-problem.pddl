(define (problem btnd - 4)
    (:domain btnd)
    (:objects
        b0 b1 - bomb
        p0 p1 p2 p3 - package
        t0 - toilet)
        
    (:init
        (in p0 b0)
        (unknown (in p1 b1))
        (unknown (in p2 b1))
        (unknown (in p3 b1))
        (oneof (in p1 b1) (in p2 b1) (in p3 b1)))
    (:goal (and (defused b0) (defused b1))))
