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
  (define (make-adder-helper m) (+ n m))
  make-adder-helper
)





; Q5: Make a List
(define lst
  (cons (cons 1 nil)
       (cons 2 (cons
                (cons 3
                      (cons 4 nil))
                (cons 5 nil))))
)





; Q6: Compose
(define (composed f g)
  (define (output x) (f (g x)))
  output
)





; Q7: Remove
(define (remove item lst)
  (cond ((eq? lst nil) nil)
        ((eq? (car lst) item) (remove item (cdr lst)))
        (else (cons (car lst) (remove item (cdr lst))))
  )
)





; Q8: No Repeats
(define (no-repeats s)
  (if (eq? nil s)
      s
      (cons (car s) (no-repeats (filter-lst (lambda (x) (not (eq? x (car s)))) (cdr s))))
  )
)





; Q9: Substitute
(define (substitute s old new)
  (cond ((eq? s nil) nil)
        ((eq? (car s) old) (cons new (substitute (cdr s) old new)))
        (else (cons (car s) (substitute (cdr s) old new)))
  )
)





; Q10: Sub All
(define (sub-all s olds news)
  (cond ((null? s) nil)
        ((null? olds) s)
        ((eq? (car s) (car olds)) (cons (car news) (sub-all (cdr s) (cdr olds) (cdr news))))
        (else (sub-all s (cdr olds) (cdr news)))
  )
)
