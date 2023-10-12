import ctypes

def c_ulong_to_python_int(c_ulong):
    """Convert a C unsigned long to a Python integer."""
    return c_ulong.value

# Test
c_value = ctypes.c_ulong(0xFFFFFFFFFFFFFFFF)  # a large unsigned long value
python_int = c_ulong_to_python_int(c_value)
print(python_int)
