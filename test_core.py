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
            is_one_one.is_one_using_roman_numerals,
            is_one_one.is_one_under_extreme_pressure
        ]
        
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

if __name__ == "__main__":
    run_verification()
