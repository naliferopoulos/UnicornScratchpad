# We simply need to collect the bytes being out'ed 

from unicorn import *
from unicorn.x86_const import *

CODE = ''

with open("chall.bin", "rb") as f:
    CODE = f.read()

def hook_out(uc, port, size, value, user_data):
    print(chr(value))

try:
    # Initialize a 16 bit Unicorn emulator
    mu = Uc(UC_ARCH_X86, UC_MODE_16)

    # Map 8 KB of memory
    mu.mem_map(0, 8 * 1024)

    # Write the executable code in memory
    mu.mem_write(0, CODE)

    # Hook the 'out' instruction
    mu.hook_add(UC_HOOK_INSN, hook_out, None, 1, 0, UC_X86_INS_OUT)

    # Emulate
    mu.emu_start(0, len(CODE))

except UcError as e:
    print e







