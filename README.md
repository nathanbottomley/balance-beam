# Balance Beam

"Balance Beam" is a Python-based application that provides visualizations for tracking the amount of money in user accounts over time. It efficiently processes transaction data from spreadsheets and offers insights into net values, facilitating improved financial decision-making.

## Features
- Import transaction data from CSV files.
- Handle transactions from joint accounts, splitting their value for accurate calculations.
- Track transactions intended for savings and maintain a running total.
- Offer a sorted view of transactions based on dates for better temporal analysis.

## Setup and Installation

1. **Clone the repository**:
    ```
    git clone https://github.com/your_username/balance-beam.git
    cd balance-beam
    ```

2. **Set up a virtual environment**:
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install required packages**:
    ```
    pip install -r requirements.txt
    ```

4. **Usage**:
   To process your transaction data, place your CSV file in the project directory and modify the script accordingly to read from your file. Then:
    ```
    python main.py
    ```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
