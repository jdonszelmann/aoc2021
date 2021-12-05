
#define GRID_SIZE_BASE 10
#define GRID_SIZE (1 << GRID_SIZE_BASE)

.data
    filename: .asciz "input.txt"
    openflags: .asciz "r"

    line_buf: .zero GRID_SIZE

    format: .asciz "part 2: %d\n"
    
    numbers: 
        .long 0
        .long 0
        .long 0
        .long 0

    file: .quad 0
    done: .byte 0
    part: .byte 1

.bss
    grid: .zero GRID_SIZE*GRID_SIZE

.text
.global main
main:
    call do_part

    movb $2, part
    movb $0, done
    call zero_grid

    call do_part

    mov $0, %rax
    ret

zero_grid:
    mov $grid, %rdi
    mov %rdi, %rsi
    add $GRID_SIZE*GRID_SIZE, %rsi

    2:
        movb $0, (%rdi)
        inc %rdi

        cmp %rdi, %rsi
        jne 2b

    ret

do_part:
    mov $filename, %rdi
    mov $openflags, %rsi
    call fopen
    mov %rax, file

    1:
        call read_line
        call process_line
        cmpb $1, done
        jne 1b
    
    mov file, %rdi
    call fclose

    mov $grid, %rdi
    mov %rdi, %rsi
    mov $0, %rax
    add $GRID_SIZE*GRID_SIZE, %rsi

    2:
        cmpb $1, (%rdi)
        jle 3f

        inc %rax        
    3:
        inc %rdi

        cmp %rdi, %rsi
        jne 2b

    mov $format, %rdi
    mov %rax, %rsi
    mov $0, %rax
    call printf

    ret

process_line:
    mov $numbers, %rdi
    mov 0(%rdi), %r12d
    mov 4(%rdi), %r13d
    mov 8(%rdi), %r14d
    mov 12(%rdi), %r15d

    cmp %r12, %r14
    je start
    cmp %r13, %r15
    je start

    cmpb $2, part
    je start

    ret

start:

    // dx
    mov %r14, %rax
    sub %r12, %rax
    jz 2f
    jns 3f
1:
    mov $-1, %rax 
    jmp 4f
2:
    mov $0, %rax 
    jmp 4f
3:
    mov $1, %rax 
4:

    // dy
    mov %r15, %rbx
    sub %r13, %rbx
    jz 6f
    jns 7f
5:
    mov $-1, %rbx 
    jmp 8f
6:
    mov $0, %rbx 
    jmp 8f
7:
    mov $1, %rbx 
8:

    mov %r13, %rsi
    shl $GRID_SIZE_BASE, %rsi
    add %r12, %rsi

    mov $grid, %rdi
    addb $1, (%rsi, %rdi, 1)

    add %rax, %r12
    add %rbx, %r13

    cmp %r12, %r14
    jne 8b
    cmp %r13, %r15
    jne 8b

    mov %r13, %rsi
    shl $GRID_SIZE_BASE, %rsi
    add %r12, %rsi

    addb $1, (%rsi, %rdi, 1)

    ret

read_line:

    mov $line_buf, %rbx
    mov $numbers, %r15

1:
    mov file, %rdi
    call fgetc

    cmp $',', %al
    je 2f

    cmp $'-', %al
    je 2f

    cmp $'>', %al
    je 1b

    cmp $' ', %al
    je 1b

    cmp $'\n', %al
    je 5f

    cmp $-1, %al
    je 4f

    mov %al, (%rbx)
    inc %rbx

    jmp 1b
2:
    call 3f
    jmp 1b
3:
    movb $0, (%rbx)

    mov $line_buf, %rdi
    call atoi

    mov %eax, (%r15)
    add $4, %r15

    mov $line_buf, %rbx
    ret
4:
    movb $1, done
    jmp 5f

5:
    call 3b
    ret

