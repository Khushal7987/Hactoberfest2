def calculate_simple_interest(principal, rate, time):
    """Calculates simple interest given principal, annual rate (%), and time (years)."""
    
    # Ensure all inputs are treated as numbers
    P = float(principal)
    R = float(rate)
    T = float(time)
    
    # Simple Interest Formula
    interest = (P * R * T) / 100
    
    return interest

# --- Example Usage ---
P = 1000  # Principal ($)
R = 5     # Rate (5%)
T = 3     # Time (3 years)

result = calculate_simple_interest(P, R, T)
print(f"Simple Interest on ${P} at {R}% for {T} years: ${result:.2f}") # Output: $150.00
