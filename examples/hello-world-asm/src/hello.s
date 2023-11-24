.global _start

.section .text
# STDIN - 0
# STDOUT - 1
# STDERR - 2


_start:
    mov r7, #0x4
    mov r0, #1
    ldr r1, =message
    mov r2, #13
    swi 0

.section .data
    message:
    .ascii "Hello World\n"
