
FIBBOI 1 Emulated in Python.


### INSTRUCTION MAP
```
HLT
00      -           -           -

LDI		DEST		VAL	
01		00		    0000		-

ADD		DEST		READ		READ
10		00		    00		    00

JMP		DEST
11		000		    -		    -
```

- - -

```
; fib

LDI r0 #0           ; 01 00 0000
LDI r1 #1           ; 01 01 0001
ADD r0 r0 r1        ; 10 00 00 01
ADD r1 r0 r1        ; 10 01 00 01
JMP 2               ; 11 010 0 00
```