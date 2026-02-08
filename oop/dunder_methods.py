import asyncio

class UniversalContainer:
    """
    An exhaustive demonstration of Python Dunder Methods.
    """

    # --- 1. Lifecycle & Construction ---
    def __new__(cls, *args, **kwargs):
        print("1. __new__: Creating the raw instance memory")
        return super().__new__(cls)

    def __init__(self, name, data_list):
        print("2. __init__: Initializing the instance attributes")
        self.name = name
        self.data = data_list
        self._internal_id = 999

    def __del__(self):
        print(f"X. __del__: {self.name} is being garbage collected")

    # --- 2. String Representation ---
    def __str__(self):
        # Used by print() and str()
        return f"Container Name: {self.name}"

    def __repr__(self):
        # Used by developers/console
        return f"UniversalContainer('{self.name}', {self.data})"

    # --- 3. Arithmetic & Math ---
    def __add__(self, other):
        # Handles self + other
        return self.data + other.data

    def __sub__(self, other):
        # Handles self - other
        return [item for item in self.data if item not in other.data]

    def __abs__(self):
        # Handles abs(obj)
        return len(self.data)

    # --- 4. Comparison Operators ---
    def __eq__(self, other):
        # Handles ==
        return self.data == other.data

    def __lt__(self, other):
        # Handles <
        return len(self.data) < len(other.data)

    # --- 5. Boolean & Truthiness ---
    def __bool__(self):
        # Handles 'if obj:'
        return len(self.data) > 0

    # --- 6. Attribute Access (Reflection) ---
    def __getattr__(self, name):
        # Called ONLY if attribute doesn't exist
        return f"Attribute '{name}' not found, but I caught the error!"

    def __setattr__(self, name, value):
        # Called EVERY time you do self.x = y
        print(f"Setting {name} to {value}")
        super().__setattr__(name, value)

    # --- 7. Container / Collection Protocol ---
    def __len__(self):
        # Handles len(obj)
        return len(self.data)

    def __getitem__(self, index):
        # Handles obj[index]
        return self.data[index]

    def __setitem__(self, index, value):
        # Handles obj[index] = value
        self.data[index] = value

    def __contains__(self, item):
        # Handles 'item in obj'
        return item in self.data

    def __iter__(self):
        # Handles 'for x in obj:'
        self._iter_index = 0
        return self

    def __next__(self):
        # Part of the iterator protocol
        if self._iter_index < len(self.data):
            val = self.data[self._iter_index]
            self._iter_index += 1
            return val
        else:
            raise StopIteration

    # --- 8. Callable & Context Management ---
    def __call__(self, *args):
        # Handles obj()
        return f"You called the object itself with args: {args}"

    def __enter__(self):
        # Handles 'with obj as x:'
        print("Entering the context...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Handles exiting the 'with' block
        print("Exiting the context...")

    # --- 9. Async Protocol ---
    async def __aenter__(self):
        await asyncio.sleep(0.1)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await asyncio.sleep(0.1)

# ==========================================
# EXECUTION DEMONSTRATION
# ==========================================

# Construction
c1 = UniversalContainer("Alpha", [1, 2, 3])
c2 = UniversalContainer("Beta", [4, 5])

# String Rep
print(f"STR: {c1}")
print(f"REPR: {repr(c1)}")

# Math & Comparison
print(f"Addition: {c1 + c2}")
print(f"Is c1 < c2? {c1 < c2}")

# Container logic
print(f"Length: {len(c1)}")
print(f"Index 0: {c1[0]}")
print(f"Check 2 in c1: {2 in c1}")

# Iteration
print("Looping through c1:")
for item in c1:
    print(f" - {item}")

# Callable
print(c1("hello", 42))

# Context Manager
with c1 as context:
    print("Inside the 'with' block!")

# Reflection/Attribute handling
print(c1.some_random_attribute)