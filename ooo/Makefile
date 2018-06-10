default: run

run: all
	time python shellpl.py

all: clean
	nasm -o shellcode.o -fbin shellcode.asm
	xxd shellcode.o

clean:
	rm -f shellcode.o