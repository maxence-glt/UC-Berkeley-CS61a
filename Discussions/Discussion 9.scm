; Discussion 9 of UC Berkeley's cs61a spring 2020 course
; https://inst.eecs.berkeley.edu/~cs61a/sp20/disc/disc09.pdf

; 3.1
; a

; 3

; b

; 28

; #t

; #f





; 4.1 
; (if (or #t (/ 1 0)) 1 (/ 1 0)) is 1

; (if (> 4 3) (+ 1 2 3 4) (+ 3 4 (* 3 2))) is 10

; ((if (< 4 3) + -) 4 100) is -96

; (if 0 1 2) is 1





; 4.1
(define (factorial x)
  (if (eq? x 0)
      1
      (* x (factorial (- x 1)))
  )
)





; 4.2
(define (fib n)
  (cond ((= n 1) 1)
        ((= n 0) 0)
        (else (+ (fib (- n 1))
                 (fib (- n 2))))))





; 5.1
(define (my-append a b)
  (if (null? a)
      b
      (cons (car a) (my-append (cdr a) b))))
