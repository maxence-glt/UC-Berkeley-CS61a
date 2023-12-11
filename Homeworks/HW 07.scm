; HW07 of UC Berkeley's cs61a spring 2020 course
; https://inst.eecs.berkeley.edu/~cs61a/sp20/hw/hw07/

; Q1: Derive Sum
(define (derive-sum expr var)
  (make-sum (derive (first-operand expr) var) (derive (second-operand expr) var)))





; Q2: Derive Product
(define (derive-product expr var)
  (make-sum (make-product (derive (first-operand expr) var) (second-operand expr))
            (make-product (first-operand expr) (derive (second-operand expr) var))))





; Q3: Make Exp
(define (make-exp base exponent)
  (cond ((= 0 exponent) 1)
        ((= 1 exponent) base)
        ((and (number? base) (number? exponent)) (expt base exponent))
        (else (list '^ base exponent))))

(define (exp? exp)
  (and (list? exp) (eq? (car exp) '^)))





; Q4: Derive Exp
(define (derive-exp exp var)
  (make-product
   (make-exp (first-operand exp) (- (second-operand exp) 1))
   (second-operand exp)))
