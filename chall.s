bits 16

mov ax, 'f'
out 0x0, al
mov bx, 0
add ax, 0x6
out 0x0, al
xor bx, bx
sub ax, 0xb
out 0x0, al
or  bx, bx
add ax, 0x6
out 0x0, al
hlt
