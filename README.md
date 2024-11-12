
# Finance App

A simple Python application to fetch the latest market price of a specified stock using `yfinance`.

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

Ensure you have Python 3.6 or later installed. You can verify your Python version with:
```bash
python3 --version
```

### Clone the Repository

1. Open your terminal.
2. Clone the repository:
   ```bash
   git clone https://github.com/Felix-kerich/finance-app.git
   ```
3. Navigate into the project directory:
   ```bash
   cd finance-app
   ```

### Set Up a Virtual Environment

1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
2. Activate the virtual environment:
   - **For Linux/macOS:**
     ```bash
     source venv/bin/activate
     ```
   - **For Windows:**
     ```cmd
     venv\Scripts\activate
     ```

### Install Dependencies

Once the virtual environment is activated, install the dependencies listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

### Run the Application

Run the application with the following command:
```bash
python3 main.py
```

### Expected Output

When prompted, enter the stock ticker symbol, like `AAPL`. The expected output should look like this:

```plaintext
Hello user
Enter the share name: AAPL
Last market price: 224.0800018310547
```

> **Note:** The last market price will vary depending on the latest available data.

## Deactivating the Virtual Environment

After running the application, you can deactivate the virtual environment by typing:
```bash
deactivate
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
