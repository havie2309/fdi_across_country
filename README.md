# FDI Net Inflow Visualization in Asia (2023)

A data visualization project that creates an interactive choropleth map displaying Foreign Direct Investment (FDI) net inflows across Asian countries for 2023. This project uses Python with Plotly to generate a color-coded geographic visualization that makes it easy to compare FDI levels across different nations.

## Table of Contents

- [Features](#features)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [How to Use](#how-to-use)

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

## How to Use

### Basic Usage

1. **Open the Jupyter Notebook:**
   ```bash
   jupyter notebook "FDI in 23 years.ipynb"
   ```

2. **Run all cells** by clicking `Cell > Run All` or run them individually

3. **View the interactive map** that appears at the bottom of the notebook

### Customizing the Visualization

You can easily customize the map by editing the configuration variables at the top of the main code cell:

```python
# Change these variables to customize your visualization
COL_COUNTRY = "country"      # Your country column name
COL_YEAR = "year"            # Your year column name
COL_VALUE = "fdi_inflow"     # Your FDI value column name
YEAR_TO_PLOT = 2023          # Change to any year in your dataset
```

### Changing the Color Scheme

To use a different color palette, modify the `color_continuous_scale` parameter:

```python
color_continuous_scale="blues"  # Try: "reds", "greens", "purples", "viridis"
```

### Changing the Geographic Scope

To view a different region:

```python
scope="world"  # Options: "asia", "europe", "africa", "north america", "south america"
```

- Built with [Plotly](https://plotly.com/)
- Inspired by economic data visualization best practices
