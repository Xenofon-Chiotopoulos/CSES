import numba

@numba.njit
def foo(x):
    if x < 3:
        return x + 1
    return x + 2

foo(10)

#print(foo.inspect_disasm_cfg(signature=foo.signatures[0]))
#print(foo.inspect_llvm)
#print(foo.inspect_asm)