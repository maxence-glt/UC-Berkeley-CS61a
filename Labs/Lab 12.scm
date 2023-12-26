; Lab 12 of UC Berkeley's cs61a spring 2020 course
; https://inst.eecs.berkeley.edu/~cs61a/sp20/lab/lab12/

; Q5: Compose All
(define (square x) (* x x))

(define (add-one x) (+ x 1))

(define (double x) (* x 2))

(define composed (compose-all (list double square add-one)))

(define (compose-all funcs)
  (define (helper num)
    (if (null? funcs)
        num
        ((compose-all (cdr funcs))((car funcs) num))))
  helper)


(composed 1)

(composed 2)
