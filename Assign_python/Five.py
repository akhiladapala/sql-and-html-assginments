def calculate_ticket_price(seats, timing, is_weekend):
    # 1.	Basic prices: 
    prices = {
        "VIP": 500,
        "REGULAR": 300,
        "ECONOMY": 150
    }
    # Timing multiplier: 
    timing_mx = {
        "morning": 0.8,
        "afternoon": 1,
        "evening": 1.2,
        "night": 1.5
    }
    
    base_total = 0
    valid_seats = 0
    
#     9.	Invalid seat types should be ignored 
# 10.	If no valid seats → return "No valid booking" 

    for seat in seats:
        if seat in prices:
            base_total += prices[seat]
            valid_seats += 1
    
    if valid_seats == 0:
        return "No valid booking"
    
    #2. timing wise charges
    timing_total = base_total * timing_mx[timing]
    
    # 3. weekend wise charges
    if is_weekend:
        timing_total += timing_total * 0.10
    
    # 4. Bulk Discount wise charges 
    discount = 0
    if valid_seats >= 5:
        discount = timing_total * 0.15
        timing_total -= discount
    
    # 5. Booking fee
    fee = valid_seats * 50
    total_after_fee = timing_total + fee
    
    #6.Gst tax wise  
    tax = total_after_fee * 0.12
    # 7. Final Amount
    final_amount = total_after_fee + tax
    # 8.	Return: 
    return {
        "base_total": round(base_total),
        "timing_adjustment": round(timing_total),
        "discount": round(discount),
        "tax": round(tax),
        "final_amount": round(final_amount)
    }

# test  case:
result = calculate_ticket_price(
    ["VIP", "REGULAR", "ECONOMY"],
    "night",
    True
)
print(result)