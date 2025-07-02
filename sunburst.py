import pandas as pd
import plotly.express as px

# Load your TSV file
data = pd.read_csv("family_subfamily.tsv", sep="\t", names=["Family", "Subfamily"])

# Count species per Family and Subfamily
counts = data.groupby(["Family", "Subfamily"]).size().reset_index(name="Count")

# Create sunburst
fig = px.sunburst(
    counts,
    path=["Family", "Subfamily"],
    values="Count",
    title="Species Counts per Hymenopteran Family/Subfamily"
)

# Save to image
fig.write_image("sunburst_species_counts.pdf")   # or .png, .svg, etc.

# Optional: still show in browser
# fig.show()

