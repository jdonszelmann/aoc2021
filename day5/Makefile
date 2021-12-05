

compile:
	gcc -no-pie -g day5.S -o a.out

run: compile
	./a.out

debug: compile
	gdb ./a.out -ex "start" # -ex "layout asm"