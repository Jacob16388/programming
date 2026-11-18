# Constants
FEDERAL_TAX_RATE = 0.10
STATE_TAX_RATE = 0.035
SOCIAL_SECURITY_RATE = 0.062
MEDICARE_RATE = 0.0145
WEEKS_PER_YEAR = 52

# Input
worker = input("Employee name: ")
rate = float(input("Hourly pay rate: "))
hours = float(input("Hours worked this week: "))

gross_pay = rate * hours
federal_tax = gross_pay * FEDERAL_TAX_RATE
state_tax = gross_pay * STATE_TAX_RATE
social_security = gross_pay * SOCIAL_SECURITY_RATE
medicare = gross_pay * MEDICARE_RATE
total_deductions = federal_tax + state_tax + social_security + medicare
net_pay = gross_pay - total_deductions
percent_kept = (net_pay / gross_pay) * 100

yearly_gross = gross_pay * WEEKS_PER_YEAR
yearly_net = net_pay * WEEKS_PER_YEAR

# Output
print()
print("=" * 32)
print(f"PAY STUB: {worker}")
print("=" * 32)
print(f"Hours worked:      {hours:.1f}")
print(f"Hourly rate:       ${rate:.2f}")
print(f"Gross pay:         ${gross_pay:.2f}")
print("-" * 32)
print(f"Federal tax (10%): ${federal_tax:.2f}")
print(f"State tax (3.5%):  ${state_tax:.2f}")
print(f"Social Security:   ${social_security:.2f}")
print(f"Medicare:          ${medicare:.2f}")
print(f"Total taken out:   ${total_deductions:.2f}")
print("-" * 32)
print(f"NET PAY:           ${net_pay:.2f}")
print("=" * 32)
print(f"You keep {percent_kept:.1f}% of what you earn.")
print(f"Yearly gross: ${yearly_gross:.2f}")
print(f"Yearly net:   ${yearly_net:.2f}")