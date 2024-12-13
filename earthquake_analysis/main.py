import pandas as pd
import matplotlib.pyplot as plt

# Load the earthquake data from CSV file
file_path = 'data/earthquake_1995-2023.csv'  # Ensure the path is correct

# Read the CSV file into a DataFrame
try:
    earthquake_data = pd.read_csv(file_path)
    print("Data loaded successfully.")
except Exception as e:
    print(f"Error loading data: {e}")
    exit()

# Step 1: Display basic statistics
def display_basic_statistics(df):
    print("\n===== Basic Earthquake Statistics =====")
    print(f"Total number of earthquakes: {len(df)}")
    print(f"Maximum magnitude: {df['magnitude'].max()}")
    print(f"Minimum magnitude: {df['magnitude'].min()}")
    print(f"Mean magnitude: {df['magnitude'].mean()}")

# Step 2: Display top 5 largest earthquakes
def display_top_5_earthquakes(df):
    top_5 = df.nlargest(5, 'magnitude')
    print("\n===== Top 5 Largest Earthquakes =====")
    print(top_5[['date_time', 'location', 'magnitude', 'depth']])
    
    # Plotting the top 5 largest earthquakes
    plt.figure(figsize=(10, 6))
    plt.bar(top_5['title'], top_5['magnitude'], color='orange')
    plt.title('Top 5 Largest Earthquakes')
    plt.xlabel('Earthquake Title')
    plt.ylabel('Magnitude')
    plt.xticks(rotation=15, ha='right')
    plt.tight_layout()
    plt.show()

# Step 3: Plot yearly earthquake count
def plot_yearly_earthquake_count(df):
    df['date_time'] = pd.to_datetime(df['date_time'], dayfirst=True, errors='coerce')  # Specify dayfirst=True
    df['Year'] = df['date_time'].dt.year
    yearly_count = df.groupby('Year').size()

    plt.figure(figsize=(10, 6))
    yearly_count.plot(kind='bar')
    plt.title('Yearly Earthquake Count (1995-2023)')
    plt.xlabel('Year')
    plt.ylabel('Number of Earthquakes')
    plt.tight_layout()
    plt.show()

# Step 4: Plot magnitude distribution
def plot_magnitude_distribution(df):
    plt.figure(figsize=(8, 5))
    plt.hist(df['magnitude'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribution of Earthquake Magnitudes (1995-2023)')
    plt.xlabel('Magnitude')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

# Main Menu
def main_menu(df):
    while True:
        print("\n===== Earthquake Analysis Menu =====")
        print("1. Display Basic Statistics")
        print("2. Display Top 5 Largest Earthquakes")
        print("3. Plot Yearly Earthquake Count")
        print("4. Plot Magnitude Distribution")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            display_basic_statistics(df)
        elif choice == '2':
            display_top_5_earthquakes(df)
        elif choice == '3':
            plot_yearly_earthquake_count(df)
        elif choice == '4':
            plot_magnitude_distribution(df)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
        
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the main menu if the data was loaded successfully
if 'earthquake_data' in locals():
    main_menu(earthquake_data)
