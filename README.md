# FDI Net Inflow Visualization in Asia (2023)

A data visualization project that creates an interactive choropleth map displaying Foreign Direct Investment (FDI) net inflows across Asian countries for 2023. This project uses Python with Plotly to generate a color-coded geographic visualization that makes it easy to compare FDI levels across different nations.

## Table of Contents

- [Features](#features)
- [Quick Start](#quick-start)
- [Installation](#installation)

## Features

- **Interactive Choropleth Map**: Hover over countries to see exact FDI values
- **Asia-Focused View**: Map automatically zooms to the Asian region for better visibility
- **Color-Coded Visualization**: Uses an orange gradient scale to represent FDI inflow levels
- **Billion-Dollar Scale**: Displays values in billions (B) for easier reading
- **Clean Design**: Minimalist styling with subtle land/ocean colors and thin borders
- **Customizable**: Easy to modify year, colors, and regions

## Quick Start

```python
# Clone the repository
git clone https://github.com/yourusername/fdi-visualization.git
cd fdi-visualization

# Install dependencies
pip install -r requirements.txt

# Run the notebook
jupyter notebook "FDI in 23 years.ipynb"
```

## Installation

### Prerequisites

- Python 3.7 or higher
- Jupyter Notebook or JupyterLab

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/fdi-visualization.git
cd fdi-visualization
```

### Step 2: Install Required Packages

```bash
pip install pandas numpy plotly ipykernel
```

Or use the requirements file (create one):

```bash
pip install -r requirements.txt
```

**requirements.txt:**
```
pandas>=1.3.0
numpy>=1.21.0
plotly>=5.0.0
ipykernel>=6.0.0
```

### Step 3: Prepare Your Data

Ensure you have a CSV file named `FDI_EconGrowth_Data.csv` with the following columns:
- `country`: Country names (e.g., "China", "India", "Viet Nam")
- `year`: Year of the data (numeric)
- `fdi_inflow`: FDI net inflow in USD

