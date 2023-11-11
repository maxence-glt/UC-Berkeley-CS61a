; HW04 of UC Berkeley's cs61a spring 2020 course
; https://inst.eecs.berkeley.edu/~cs61a/sp20/hw/hw04/

; Q2: Thane of Cadr
(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)





; Q3: Sign
(define (sign x)
  (cond ((< x 0) -1)
      ((= x 0) 0)
      ((> x 0) 1)
  )
)





; Q4: Pow
(define (square x) (* x x))

(define (pow b n)
  (display n) (newline)
  (cond ((= 1 n) b)
        ((even? n) (square (pow b (/ n 2))))
        ((odd? n) (* (square (pow b (/ (- n 1) 2))) b))
  )
)





; Q5: Unique
(define (unique s)
  (if ((<= (length s) 1) s)
      (else (unique (filter (lambda (m) (not (eq? m (car s)))) (cdr s))))
  )
)
