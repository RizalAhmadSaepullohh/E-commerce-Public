
```markdown
# E-Commerce Dashboard

This dashboard provides visual insights into key aspects of an e-commerce dataset, including total revenue by quarter, city-specific customer statistics, and product category review scores. It features interactive filters to enhance data exploration.

## Features

- **Total Revenue by Quarter**: Visualize total revenue generated each quarter, with a filter to select specific quarters.
- **City Stats**: Display top cities by total customers and their average order value, with an option to filter by the number of cities shown.
- **Top 10 Product Categories by Average Review Score**: Shows the top 10 product categories by average review score, with the number of reviews annotated.

## Prerequisites

To run this dashboard, you'll need the following installed:

- **Python 3.x**
- Required Python libraries:
  - `pandas`
  - `matplotlib`
  - `streamlit`

## Installation

Follow these steps to set up the project locally:

### 1. Clone the Repository

First, clone the repository and navigate into the project directory:

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Install the Dependencies

Install the necessary dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### 3. Ensure Data Availability

Make sure the following CSV files are in the `Data/` directory:

- `total_revenue_quarterly.csv`
- `city_stats.csv`
- `category_review_scores.csv`

If you don’t have the files, you'll need to generate them by running the provided Python scripts or using your own dataset.

## How to Run the Dashboard

To run the Streamlit app:

1. Open a terminal in the directory where `dashboard.py` is located.
2. Run the following command:

```bash
streamlit run dashboard.py
```

3. The app should open in your web browser automatically. If it doesn’t, navigate to the URL provided in the terminal (usually `http://localhost:8501`).

## Dashboard Usage

### 1. **Total Revenue by Quarter**

- Displays total revenue per quarter.
- Use the **multi-select filter** to select specific quarters to view.

### 2. **City Stats: Total Customers and Average Order Value**

- Visualizes customer statistics for different cities.
- Includes the total number of customers per city and the average order value.
- A **slider filter** allows you to adjust the number of cities displayed (e.g., top 10, top 20).

### 3. **Top 10 Product Categories by Average Review Score**

- Shows the top 10 product categories based on their average review score.
- Each bar represents a category, and the number of reviews is displayed as an annotation.

## Filters

- **Quarter Selection**: Filter the revenue chart by specific quarters.
- **City Count Slider**: Adjust the number of cities shown in the customer stats section.
- **Product Categories**: The top 10 categories are automatically displayed based on average review score.

## Example Output

- **Revenue by Quarter**: A bar chart showing the revenue breakdown for each quarter.
- **City Stats**: A dual-axis chart that shows both the total number of customers and their average order value per city.
- **Product Categories**: A horizontal bar chart with the top 10 categories ranked by review score, with review counts shown next to each bar.

## Data Sources

The data used in this dashboard includes:

- **Order data**: Contains details of orders, including the date, products, and price.
- **Customer data**: Provides information about customers, including their location (city, state, and zip code).
- **Geolocation data**: Links zip codes to geographic locations (latitude and longitude).
- **Product and review data**: Provides information about products and customer reviews.

## Customization

- You can easily modify the dataset or the number of items displayed by adjusting the filter options in the Streamlit app.
- The charts and visualizations are fully customizable by editing the Streamlit script.

## Project Structure

```plaintext
.
├── Data/
│   ├── total_revenue_quarterly.csv      # CSV containing quarterly revenue data
│   ├── city_stats.csv                   # CSV containing city-level customer statistics
│   └── category_review_scores.csv        # CSV containing product category review scores
├── dashboard.py                         # The Streamlit app script
└── README.md                            # This readme file
```

## License

This project is licensed under the MIT License.

## Contact

For any questions or feedback, feel free to reach out to:

- **Rizal Ahmad Saepulloh**
  - Email: [your-email@example.com]
  - LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/)
```

### Instructions:
- Remember to replace `<repository-url>`, `[your-email@example.com]`, and the LinkedIn URL with your actual details.
