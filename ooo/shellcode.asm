bits 64

; force page alignment
xor al, al
and ah, 0xf0

xor r8, r8

;decrement by 0x1000 r8 times
loop:
	; check next page
	sub ax, 0xfff
	dec ax

	; loop counter
	inc r8
	cmp r8, {test}
	jle loop
;^--------------------------

	; look for \x7fELF
	mov edx, dword [rax]
	cmp edx, 0x464c457f
	je hang
	int3

hang:
	jmp $

ret
