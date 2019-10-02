build:
	nasm chall.s -f bin -o chall.bin

clean:
	rm chall.bin

solve:
	python solver.py
