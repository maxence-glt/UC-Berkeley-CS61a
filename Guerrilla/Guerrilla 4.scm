; Guerilla 4 of UC Berkeley's cs61a spring 2020 course
; https://inst.eecs.berkeley.edu/~cs61a/sp20/disc/guer04.pdf

; 1.1
; multiplies x by y is not tail recursion, since it adds the result of a
; future recursive return, making the space complexity grow with each iteration
(define (mult x y)
    (define )
    (if (eq? y 1)
        x
        (mult (+ x x) )))

; true1 is tail recursive, since no extra work needs to be done when the function
; reaches the return statement

; true2 isn't tail recursive, since the or function just needs to recieve one
; truthy value
(define (true2 n)
  (if (= n 0)
      #t
      (true2 (- n 1))))

; contains isn't tail recursive since after the recursion is executed, we still
; need to go through the else clause
(define (contains lst x)
  (cond
    ((null? lst) #f)
    ((equal? (car lst) x) #t)
    (else (contains (cdr lst) x))))





; 1.2
(define (sum-satisfied-k lst f k)
 (define (iter lst f k total)
   (cond ((null? lst) 0)
         ((= k 0) total)
         ((f (car lst)) (iter (cdr lst) f (- k 1) (+ total (car lst))))
         (else (iter (cdr lst) f k total))))
 (iter lst f k 0))





 ; 1.3
 (define (remove-range lst i j)
  (define (iter lst index new-lst)
    (if (null? lst)
        new-lst
        (if (and (<= index j) (>= index i))
            (iter (cdr lst) (+ index 1) new-lst)
            (iter (cdr lst) (+ index 1) (append new-lst (list (car lst)))))))
  
  (iter lst 0 '()))





; All subexpressions aren't tail-recursive since for an expression to be tail-
; recursive, it must be the end of the recursion and return without the function needing to evaulate more
; (+ 4 5) isn't tail recursive in that example since the expression still needs to evaulate
; the result of that + 1

; you could have a helper iter function that appends over and over but that defeats 
; the purpose of functional programmiing / Scheme / Lisp
