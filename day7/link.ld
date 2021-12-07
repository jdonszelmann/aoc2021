OUTPUT_ARCH( "riscv" )
ENTRY(entry)

KERNEL_START = 0x80000000;

SECTIONS {
    __KERNEL_STACK_SIZE = DEFINED(__KERNEL_STACK_SIZE) ? __KERNEL_STACK_SIZE : 2K;

    . = KERNEL_START;

    .boot : AT(KERNEL_START) {
         KEEP (*(SORT_NONE(.boot)))
    }

    .rodata : {
        *(.rdata)
        *(.rodata .rodata.*)
    }

    . = ALIGN(4);

    .data : {
        *(.data)
        PROVIDE( __global_pointer$ = . + 0x800 );
        *(.sdata .sdata.*)
        *(.gnu.linkonce.s.*)
        . = ALIGN(8);
        *(.srodata.cst16)
        *(.srodata.cst8)
        *(.srodata.cst4)
        *(.srodata.cst2)
        *(.srodata .srodata.*)
    }

    . = ALIGN(4);
    .bss : {
        *(.bss)
        *(COMMON)
        . = ALIGN(4);
    }

    . = ALIGN(8);

    PROVIDE(__STACK_START = .);
    .stack : {
        . += __KERNEL_STACK_SIZE;
        PROVIDE( __STACK_POINTER = . );
    }
    PROVIDE(__STACK_END = .);
}