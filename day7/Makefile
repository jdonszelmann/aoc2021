

compile:
	riscv64-unknown-elf-gcc -T link.ld -g day7.S -o a.out -nostdlib -march=rv64gc -mno-fdiv -mabi=lp64


run: compile
	qemu-system-riscv64 -machine sifive_u -bios none -nographic -kernel a.out &
	@sleep 1
	@killall qemu-system-riscv64

run-debug: compile
	qemu-system-riscv64 -machine sifive_u -bios none -nographic -s -S -kernel a.out

debug:
	riscv64-unknown-elf-gdb ./a.out -ex "target remote localhost:1234" -ex "b entry"  -ex "c"