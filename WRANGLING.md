# Data Preparation Process

This section documents the full data preparation workflow, beginning with downloading raw files from Statistics Canada and ending with the creation of finalized Tableau `.hyper` files used for visualization. It outlines the issues encountered in the raw data, how each issue was resolved, and the assumptions made during cleaning.


## 1. Downloading and Initial File Review

All datasets were downloaded directly from **Statistics Canada** in CSV format. The raw files contained extensive metadata, including descriptive headers, footnotes, classification labels, and explanatory notes above and below the actual data tables. While this metadata is useful for context, it prevented the files from being immediately usable in Excel or Tableau.

### Issues Identified in Raw Files

* Multiple header rows (e.g., geography, NAICS labels, units of measurement)
* Blank rows separating industry categories
* Industry names listed once with blank rows beneath
* Wide-format structure (months or years spread across columns)
* Text values embedded within numeric fields (e.g., “F” or “x”)
* Commas in numeric fields causing text data types
* Hierarchical column headers (province on one row, year on another)


## 2. Cleaning and Structuring Data in Excel

Excel was used as the first stage of cleaning to remove formatting inconsistencies and restructure the data.

### Step 1: Removing Metadata

All non-data rows were deleted, including:

* Geography labels
* NAICS classification headings
* Units rows (e.g., “Number”, “Percent”)
* Footnotes and blank separator rows

Only rows containing actual numerical observations were retained.


### Step 2: Filling Down Industry and Category Labels

Industry names were often listed once, followed by blank rows for related statistics (e.g., Job vacancies, Payroll employees, Job vacancy rate). To correct this:

* Blank cells in the Industry column were filled down using Excel’s **Go To Special → Blanks** function.
* Values were pasted as static values to remove formula dependencies.

This ensured each row had a complete industry identifier.

### Step 4: Cleaning Numeric Fields

Several formatting issues existed in numeric columns:

* Commas (e.g., `16,287,130`) caused fields to be interpreted as text
* Suppressed values (e.g., “F” or “x”) appeared in some datasets
* Percentage values required decimal formatting

To resolve these:

* Non-numeric symbols were replaced with `NULL` values
* Commas were removed
* Columns were converted to appropriate numeric data types (Whole Number or Decimal)

This ensured consistency when importing into Tableau.

---

## 3. Preparing Data in Tableau Prep

After Excel cleaning, the files were imported into **Tableau Prep** for final transformation and export into `.hyper` format.

### Step 1: Verifying Data Types

Each field was reviewed to ensure:

* `Industry` and `Province` were **Dimensions (String)**
* `Date` was correctly recognized as **Date**
* `Value` fields were numeric **Measures**

Any incorrect data types were manually corrected.


### Step 2: Pivoting and Restructuring (Where Required)

For datasets with hierarchical headers (e.g., province in row 1 and year in row 3):

* Province names were filled across columns
* Province and year were combined into a single header
* Columns were pivoted to rows
* Province and Year were split into separate fields

This normalized the dataset into a flat structure suitable for visualization.


### Step 3: Removing Residual Errors

Additional cleaning steps included:

* Filtering out repeated header rows that remained within the data body
* Checking for duplicates created during pivoting
* Validating aggregation behavior in the Tableau Prep preview


## 4. Assumptions and Decisions Made

The following assumptions guided the cleaning process:

1. Suppressed values (“F”, “x”) were treated as missing values (`NULL`), not zero.
2. No data values were manually adjusted or estimated.
3. All employment and monetary values were assumed to be reported in the units specified by Statistics Canada.
4. Monthly labels such as “19-Jan” were interpreted as January 2019.
5. Wide-format tables were converted to long format following Tableau best practices.

These decisions were made to preserve data integrity while ensuring analytical usability.


## 5. Final Output

The cleaned datasets were exported from Tableau Prep as `.hyper` files. These final files:

* Contain structured, analysis-ready data
* Have consistent and verified data types
* Follow long-format design principles
* Are optimized for Tableau visualizations

The original CSV files were retained with metadata removed, while the `.hyper` files represent the finalized datasets used in dashboard development.
