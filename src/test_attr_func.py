def external_function(arg):
    return f"External function called with {arg}"

class MyClass:
    # 1. Standard method (function defined inside class)
    def normal_method(self):
        return "Normal method"
    
    # 2. Class attribute assigned a function
    # NOTE: When accessed on an instance, Python treats this as a bound method!
    class_func_attr = external_function

    def __init__(self):
        # 3. Instance attribute assigned a function
        # NOTE: This remains a plain function, NOT a method.
        self.instance_func_attr = external_function

obj = MyClass()

print("--- Accessing Class Attribute ---")
print(f"Via Class (MyClass.class_func_attr): {MyClass.class_func_attr}")
print(f"Via Instance (obj.class_func_attr): {obj.class_func_attr}")

print("\n--- Accessing Instance Attribute ---")
print(f"Via Instance (obj.instance_func_attr): {obj.instance_func_attr}")

print("\n--- Calling Them ---")
try:
    # This works because it's a bound method, so 'obj' is passed as the first argument 'arg'
    # external_function(obj)
    print(f"Calling obj.class_func_attr(): {obj.class_func_attr()}") 
except Exception as e:
    print(f"Error calling obj.class_func_attr(): {e}")

try:
    # This acts like a normal function. 'obj' is NOT passed automatically.
    # So we must pass the argument manually if we want it to work, or call it with the expected args.
    # external_function("hello")
    print(f"Calling obj.instance_func_attr('hello'): {obj.instance_func_attr('hello')}")
except Exception as e:
    print(f"Error calling obj.instance_func_attr('hello'): {e}")
