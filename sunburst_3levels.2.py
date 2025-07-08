import pandas as pd
import plotly.express as px
import sys
import re
import os

# Check command-line arguments
if len(sys.argv) < 2:
    print("Usage: python sunburst_fixed.py <input_file> [output_file]")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2] if len(sys.argv) > 2 else "sunburst_grouped.pdf"

# Extract input file base name (e.g., 'ducks' from 'ducks.txt')
input_name = os.path.splitext(os.path.basename(input_file))[0]

# Try to determine the separator and load data
print("Attempting to load and parse data...")

try:
    # First, try reading as tab-separated
    df = pd.read_csv(input_file, sep="\t", names=["Group", "Family", "Subfamily"])
    
    # Check if parsing worked (Family and Subfamily shouldn't be all NaN)
    if df['Family'].isna().all() and df['Subfamily'].isna().all():
        print("Tab separation didn't work, trying space separation...")
        
        # Read the raw data line by line and split on multiple spaces
        data_rows = []
        with open(input_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line:  # Skip empty lines
                    # Split on multiple spaces/tabs (2 or more whitespace characters)
                    parts = re.split(r'\s{2,}', line)
                    if len(parts) >= 3:
                        data_rows.append(parts[:3])  # Take first 3 parts
                    else:
                        # If that doesn't work, try single space split
                        parts = line.split()
                        if len(parts) >= 3:
                            data_rows.append(parts[:3])
        
        # Create DataFrame from parsed data
        if data_rows:
            df = pd.DataFrame(data_rows, columns=["Group", "Family", "Subfamily"])
        else:
            print("Could not parse the data file properly")
            sys.exit(1)
    
    print(f"Successfully loaded {len(df)} rows")
    print("Sample data:")
    print(df.head(), "\n")
    
    # Remove any rows with NaN values
    df = df.dropna()
    print(f"After removing NaN: {len(df)} rows")

    if df.empty:
        print("No valid data after cleaning")
        sys.exit(1)

    # Count occurrences per Group > Family > Subfamily
    counts = df.groupby(["Group", "Family", "Subfamily"]).size().reset_index(name="Count")
    print(f"Created {len(counts)} unique combinations")
    print(f"Total specimens: {counts['Count'].sum()}\n")

    # Show some sample counts
    print("Sample grouped data:")
    print(counts.head(10), "\n")

    # Prepare title for plot
    num_species = len(df)
    plot_title = f"{input_name} – {num_species} species: Group / Family / Subfamily"

    # Create sunburst plot
    fig = px.sunburst(
        counts,
        path=["Group", "Family", "Subfamily"],
        values="Count",
        title=plot_title
    )

    # Update layout
    fig.update_layout(
        title={
            'text': plot_title,
            'x': 0.5,
            'xanchor': 'center',
            'font': dict(size=20)
        }
    )

    # Save plot to image
    fig.write_image(output_file)
    print(f"Sunburst plot saved as: {output_file}")

    # Also save HTML version for easier viewing
    html_file = output_file.replace('.pdf', '.html')
    fig.write_html(html_file)
    print(f"HTML version saved as: {html_file}")

except Exception as e:
    print(f"Error: {e}")
    print(f"Error type: {type(e)}")

    # Print some debug info about the file
    print("\nFile debug info:")
    with open(input_file, 'r') as f:
        lines = f.readlines()[:5]
        for i, line in enumerate(lines):
            print(f"Line {i+1}: '{line.strip()}'")
            print(f"  Length: {len(line.strip())}")
            print(f"  Repr: {repr(line.strip())}")
    sys.exit(1)
