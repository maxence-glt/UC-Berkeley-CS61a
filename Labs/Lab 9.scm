;  Lab 9 of UC Berkeley's cs61a spring 2020 course
; https://inst.eecs.berkeley.edu/~cs61a/sp20/lab/lab09/

; Q2: Over or Under
(define (over-or-under a b)
  (cond ((< a b) -1)
        ((eq? a b) 0)
        (else 1)
  )
)





; Q3: Filter Lst
(define (filter-lst fn lst)
  (cond ((null? lst) nil)
        ((fn (car lst)) (cons (car lst) (filter-lst fn (cdr lst))))
        (else (filter-lst fn (cdr lst)))
  )
)





; Q4: Make Adder
(define (make-adder n)
  (lambda adder (n m) (+ n m))
  adder
)
  