# type: ignore
import matplotlib.pyplot as plt 
import seaborn as sns


# Set the style for seaborn
sns.set(style="whitegrid")
# Univariate analysis for numerical variables
numerical_variables = ['housing_median_age', 'total_rooms', 'total_bedrooms', 
                        'population', 'households', 'median_income', 'median_house_value']



def longitude_latitude_distribution(df):
    # Scatter plot of longitude and latitude
    plt.figure(figsize=(10, 8))
    plt.scatter(df['longitude'], df['latitude'], alpha=0.5, c='b', edgecolors='k')
    plt.title('Spatial Distribution of Housing')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid(True)
    return plt

def generate_correlation_heatmap(df):
    # Calculate correlation matrix
    # Heatmap for correlation matrix
    correlation_matrix = df[numerical_variables].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", annot_kws={"size": 10})
    plt.title('Correlation Matrix')
    return plt

def pairwise_scatter_plots(df):
    # Pairwise scatter plots for numerical attributes
    sns.pairplot(df[numerical_variables])
    plt.title('Pairwise Scatter Plots')
    return plt



def numerical_attribute_histograms(df):
    # Create histograms for numerical attributes
    num_plots = len(numerical_variables)
    num_cols = 3  # Number of columns in the grid
    num_rows = (num_plots + num_cols - 1) // num_cols  # Number of rows in the grid

    fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, num_rows * 5))

    for i, attribute in enumerate(numerical_variables):
        row = i // num_cols
        col = i % num_cols
        ax = axes[row, col] if num_rows > 1 else axes[col]
        sns.histplot(data=df, x=attribute, bins=20, edgecolor='k', alpha=0.7, ax=ax)
        ax.set_title(f"Histogram of {attribute}")

    plt.suptitle('Histograms of Numerical Attributes', y=1.02)  # Title for the entire grid
    plt.tight_layout()
    return plt


# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/YOUNGGOAT34/Housing-Dashoboard.git
# git push -u origin main







