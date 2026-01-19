## 📊 Netflix Customer Engagement & Churn Analysis

### Project Overview** <br>
This project presents an end-to-end customer engagement and churn analysis using Netflix-style data.
The objective is to understand customer behavior, identify churn patterns, and derive actionable insights using a full analytics pipeline — from raw data to an interactive dashboard.

The project simulates a real-world analytics workflow involving Python (ETL), MySQL (data modeling & validation), and Tableau (visual analytics).

**** 

### Interactive Dashboard (Tableau Public) 
🔗 Click the image below to explore the live dashboard

[![Netflix Customer Engagement & Churn Dashboard](https://public.tableau.com/static/images/ne/netflixportfolio/NetflixCustomerEngagementChurnDashboard/1.png)](https://public.tableau.com/views/netflixportfolio/NetflixCustomerEngagementChurnDashboard)


###  Business Objectives

- Measure overall customer engagement and churn

- Identify which subscription plans have higher churn

- Analyze engagement differences between churned and active users

- Understand tenure-based churn patterns

- Compare churn behavior across countries

- Provide actionable insights for customer retention strategies

  *****
### Tools & Technologies Used


### 🔹 Programming & Data Processing

- **Python**
  - pandas
 


### 🔹 Database

- **MySQL**
  - Relational modeling
  - Foreign key constraints
  - Data validation using SQL



### 🔹 Visualization

- **Tableau Public**
  - KPI dashboards
  - Bar charts & comparisons
  - Business storytelling



### 🔹 Version Control

- **Git & GitHub**



*****

## Data Modeling (Star Schema)

The data is modeled using a **star schema**, a best practice in analytics that improves
query performance, clarity, and scalability.

*****

### Dimension Table

#### customers
- `customer_id` (PK)
- `age`
- `gender`
- `country`
- `plan_type`
- `signup_date`
- `tenure_months`

*****

### Fact Tables

#### engagement
- `engagement_id` (PK)
- `customer_id` (FK)
- `month`
- `watch_hours`
- `login_days`
- `num_titles_watched`

*****

#### churn
- `customer_id` (FK)
- `is_churned` (0/1)
- `churn_date`

*****

###  Why This Structure Works

- Prevents duplicate customers
- Ensures accurate aggregations
- Supports scalable analytics and visualization
- Enables clean joins across fact tables


*****

##  ETL Process (Python)


### 1. Customers Table Creation

```python
customers = users[['user_id', 'age', 'gender', 'country',
                   'subscription_plan', 'subscription_start_date']]

customers['tenure_months'] = (
    pd.Timestamp.today() - customers['subscription_start_date']
).dt.days // 30

```
-  Cleans user data
-  Renames columns
-  Calculates customer tenure


### 2. Engagement Table Creation

```python
engagement = watch_history.groupby(
    ['user_id', watch_history['watch_date'].dt.to_period('M')]
).agg(
    watch_hours=('watch_duration_minutes', 'sum'),
    login_days=('watch_date', 'nunique'),
    num_titles_watched=('movie_id', 'nunique')
).reset_index()
```
✔ Aggregates monthly engagement <br>
✔ Prevents row duplication<br>
✔ Enables customer-level analysis<br>

## 3. Churn Table Creation

```python
churn = customers[['customer_id']]
churn['is_churned'] = np.where(customers['is_active'] == 0, 1, 0)
churn['churn_date'] = np.where(
    churn['is_churned'] == 1,
    customers['last_active_date'],
    None
)
```
✔ Identifies churned customers <br>
✔ Handles NULL churn dates correctly

****

## Tableau Dashboard

### 🔹 KPI Cards

- Total Customers

- Churn Rate %

- Avg Watch Hours

- Avg Login Days

### 🔹 Visualizations

- Churn Rate by Plan

- Engagement vs Churn

- Country-wise Churn

- Tenure vs Churn (Monthly)

### 🔹 Design

- Netflix-inspired dark theme

- Red highlights for churn

- Clean & business-focused layout

****

#### Analytical Considerations

- Granularity issues were handled using LOD calculations

- KPI values were validated against MySQL queries

- No artificial manipulation of data was performed

- Insights are based on honest data behavior

****

## Author

<b> Yogesh </b>
<br>
Data Analyst

Tools: Python | SQL | Tableau | Power BI
