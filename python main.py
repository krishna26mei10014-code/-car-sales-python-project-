# ==========================================
# Project: Car Sales Analysis (6 Months)
# Author: 1st Year Python Student
# Description: Finds the car company with 
# the maximum sales among selected brands.
# ==========================================

# Dictionary storing total car sales for the past 6 months
car_sales = {
    "Maruti Suzuki": 900000,
    "Tata": 350000,
    "Mahindra": 320000,
    "Toyota": 150000,
    "Kia": 140000,
    "Volkswagen": 45000,
    "Skoda": 40000
}

def display_all_sales(sales_data):
    """Function to display sales of all car brands"""
    print("-" * 45)
    print(f"{'Car Brand':<20} | {'6-Month Sales':<15}")
    print("-" * 45)
    for brand, sales in sales_data.items():
        print(f"{brand:<20} | {sales:,}")
    print("-" * 45)

def find_maximum_sales(sales_data):
    """Function to find the brand with the highest sales"""
    highest_brand = ""
    highest_sales = 0
    
    # Loop through the dictionary to find the maximum
    for brand, sales in sales_data.items():
        if sales > highest_sales:
            highest_sales = sales
            highest_brand = brand
            
    return highest_brand, highest_sales

def main():
    print("=" * 45)
    print("   AUTOMOBILE SALES ANALYSIS PROJECT   ")
    print("=" * 45)
    print("\nFetching 6-month sales report for major brands...\n")
    
    # Display the dataset
    display_all_sales(car_sales)
    
    # Calculate the winner
    top_brand, top_sales = find_maximum_sales(car_sales)
    
    # Display the final output
    print("\n[CONCLUSION]")
    print(f"The car company that sold the MAXIMUM cars in 6 months is:")
    print(f">>> {top_brand.upper()} with a total of {top_sales:,} units! <<<")
    print("=" * 45)

# Entry point of the program
if __name__ == "__main__":
    main()
	
	