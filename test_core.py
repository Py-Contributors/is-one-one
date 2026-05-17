import is_one_one
import sys
import io

# Fix for Windows console encoding issues with emojis
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def run_verification():
    print("🧪 Starting Automated Quality Check...")
    
    # List of functions to be verified
    try:
        checks = [
            is_one_one.is_one,
            is_one_one.is_one_unicode_distance,
            is_one_one.is_one_using_time_travel,
            is_one_one.is_one_using_interdimensional_tax_fraud,
            is_one_one.is_one_using_binary,
            is_one_one.is_one_using_roman_numerals,
            is_one_one.is_one_under_extreme_pressure
        ]

        if is_one_one.is_one_using_binary.__module__ != "methods.sample_method":
            raise ValueError("Dynamic method loader did not load sample methods!")
        
        for func in checks:
            print(f"Checking: {func.__name__}...")
            if func() is not True:
                # If any function fails, we stop immediately
                raise ValueError(f"{func.__name__} did not return True!")
        
        print("✅ All logic verified. 1 is 1.")
    except Exception as e:
        print(f"❌ Verification Failed: {e}")
        # sys.exit(1) is the 'signal' to GitHub Actions that the build failed
        sys.exit(1) 

def test_dynamic_method_loader_loads_sample_methods():
    assert is_one_one.is_one_using_binary.__module__ == "methods.sample_method"
    assert is_one_one.is_one_using_binary() is True

def test_available_checks_include_dynamic_methods():
    check_names = {
        func.__name__
        for func in is_one_one.get_available_checks(include_meta_check=True)
    }

    assert "is_one_using_binary" in check_names
    assert "is_one_unicode_distance" in check_names

if __name__ == "__main__":
    run_verification()
