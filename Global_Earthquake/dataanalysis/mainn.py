import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the earthquake data from a specified path
csv_file_path = 'import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the earthquake data from a specified path
csv_file_path = 'path/to/your/earthquakes.csv'  # Update this path
data = pd.read_csv(import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the earthquake data from a specified path
csv_file_path = 'path/to/your/earthquakes.csv'  # Update this path
data = pd.read_csv(csv_file_path)

# Step 2: Clean the data
# Strip spaces from column names
data.columns = data.columns.str.strip()

# Check for and drop any duplicates
data = data.drop_duplicates()

# Check for missing values
data = data.dropna(subset=['magnitude', 'latitude', 'longitude', 'location', 'country'])

# Step 3: Find the highest and lowest earthquake locations
highest_earthquake = data.loc[data['magnitude'].idxmax()]
lowest_earthquake = data.loc[data['magnitude'].idxmin()]

# Step 4: Display results
print("\nHighest Earthquake Location:")
print(f"Location: {highest_earthquake['location']}, "
      f"Country: {highest_earthquake['country']}, "
      f"Latitude: {highest_earthquake['latitude']}, "
      f"Longitude: {highest_earthquake['longitude']}, "
      f"Magnitude: {highest_earthquake['magnitude']}")

print("\nLowest Earthquake Location:")
print(f"Location: {lowest_earthquake['location']}, "
      f"Country: {lowest_earthquake['country']}, "
      f"Latitude: {lowest_earthquake['latitude']}, "
      f"Longitude: {lowest_earthquake['longitude']}, "
      f"Magnitude: {lowest_earthquake['magnitude']}")

# Step 5: Visualize the magnitudes
plt.figure(figsize=(8, 6))
plt.bar(
    [f"Highest: {highest_earthquake['location']}, {highest_earthquake['country']}",
     f"Lowest: {lowest_earthquake['location']}, {lowest_earthquake['country']}"],
    [highest_earthquake['magnitude'], lowest_earthquake['magnitude']],
    color=['red', 'blue']
)
plt.title('Highest and Lowest Earthquake Magnitudes')
plt.ylabel('Magnitude')
plt.ylim(0, max(highest_earthquake['magnitude'] + 1, 10))  # Set y-limit for better visibility
plt.grid(axis='y')
plt.tight_layout()
plt.show()
)

# Step 2: Clean the data
# Strip spaces from column names
data.columns = data.columns.str.strip()

# Check for and drop any duplicates
data = data.drop_duplicates()

# Check for missing values
data = data.dropna(subset=['magnitude', 'latitude', 'longitude', 'location', 'country'])

# Step 3: Find the highest and lowest earthquake locations
highest_earthquake = data.loc[data['magnitude'].idxmax()]
lowest_earthquake = data.loc[data['magnitude'].idxmin()]

# Step 4: Display results
print("\nHighest Earthquake Location:")
print(f"Location: {highest_earthquake['location']}, "
      f"Country: {highest_earthquake['country']}, "
      f"Latitude: {highest_earthquake['latitude']}, "
      f"Longitude: {highest_earthquake['longitude']}, "
      f"Magnitude: {highest_earthquake['magnitude']}")

print("\nLowest Earthquake Location:")
print(f"Location: {lowest_earthquake['location']}, "
      f"Country: {lowest_earthquake['country']}, "
      f"Latitude: {lowest_earthquake['latitude']}, "
      f"Longitude: {lowest_earthquake['longitude']}, "
      f"Magnitude: {lowest_earthquake['magnitude']}")

# Step 5: Visualize the magnitudes
plt.figure(figsize=(8, 6))
plt.bar(
    [f"Highest: {highest_earthquake['location']}, {highest_earthquake['country']}",
     f"Lowest: {lowest_earthquake['location']}, {lowest_earthquake['country']}"],
    [highest_earthquake['magnitude'], lowest_earthquake['magnitude']],
    color=['red', 'blue']
)
plt.title('Highest and Lowest Earthquake Magnitudes')
plt.ylabel('Magnitude')
plt.ylim(0, max(highest_earthquake['magnitude'] + 1, 10))  # Set y-limit for better visibility
plt.grid(axis='y')
plt.tight_layout()
plt.show()
 # Update this path
data = pd.read_csv(csv_file_path)

# Step 2: Clean the data
# Strip spaces from column names
data.columns = data.columns.str.strip()

# Check for and drop any duplicates
data = data.drop_duplicates()

# Check for missing values
data = data.dropna(subset=['magnitude', 'latitude', 'longitude', 'location', 'country'])

# Step 3: Find the highest and lowest earthquake locations
highest_earthquake = data.loc[data['magnitude'].idxmax()]
lowest_earthquake = data.loc[data['magnitude'].idxmin()]

# Step 4: Display results
print("\nHighest Earthquake Location:")
print(f"Location: {highest_earthquake['location']}, "
      f"Country: {highest_earthquake['country']}, "
      f"Latitude: {highest_earthquake['latitude']}, "
      f"Longitude: {highest_earthquake['longitude']}, "
      f"Magnitude: {highest_earthquake['magnitude']}")

print("\nLowest Earthquake Location:")
print(f"Location: {lowest_earthquake['location']}, "
      f"Country: {lowest_earthquake['country']}, "
      f"Latitude: {lowest_earthquake['latitude']}, "
      f"Longitude: {lowest_earthquake['longitude']}, "
      f"Magnitude: {lowest_earthquake['magnitude']}")

# Step 5: Visualize the magnitudes
plt.figure(figsize=(8, 6))
plt.bar(
    [f"Highest: {highest_earthquake['location']}, {highest_earthquake['country']}",
     f"Lowest: {lowest_earthquake['location']}, {lowest_earthquake['country']}"],
    [highest_earthquake['magnitude'], lowest_earthquake['magnitude']],
    color=['red', 'blue']
)
plt.title('Highest and Lowest Earthquake Magnitudes')
plt.ylabel('Magnitude')
plt.ylim(0, max(highest_earthquake['magnitude'] + 1, 10))  # Set y-limit for better visibility
plt.grid(axis='y')
plt.tight_layout()
plt.show()
