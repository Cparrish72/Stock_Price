from stock_data import fetch_stock_data
from database import create_connection, create_table, insert_stock_data
from visualization import plot_stock_price

def main():
    database = "stock_data.db"

    sql_create_stocks_table = """ CREATE TABLE IF NOT EXISTS stocks (
                                        id integer PRIMARY KEY,
                                        date text NOT NULL,
                                        ticker text NOT NULL,
                                        open real,
                                        high real,
                                        low real,
                                        close real,
                                        volume integer
                                    ); """

    conn = create_connection(database)


    if conn is not None:
        create_table(conn, sql_create_stocks_table)
    else:
        print("Error! Cannot create the database connection.")

    ticker = input("Enter stock ticker: ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    data = fetch_stock_data(ticker, start_date, end_date)


    plot_stock_price(data, ticker)

    for index, row in data.iterrows():
        stock_data = (str(index.date()), ticker, row['Open'], row['High'], row['Low'], row['Close'], row['Volume'])
        insert_stock_data(conn, stock_data)

    conn.close()
    print(f"Data for {ticker} has been saved to the database.")

if __name__ == "__main__":
    main()

