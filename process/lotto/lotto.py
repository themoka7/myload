import json
import os
from datetime import date, datetime
from process.common.dbCon import dbConn

current_dir = os.path.dirname(os.path.abspath(__file__))


# Custom encoder to handle date objects
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.strftime('%Y-%m-%d')  # Convert date/datetime to string
        return super().default(obj)


def get_lotto_data():
    try:
        conn = dbConn()
        cursor = conn.cursor()
        print(conn.ping())  # Check if the connection is alive

        # SQL query to fetch the latest lotto results
        query = """
        SELECT * 
        FROM LottoResults
        WHERE drwNo = (SELECT max(drwNo) FROM LottoResults)
        """

        # Execute the query
        cursor.execute(query)

        # Fetch columns from cursor description
        columns = [col[0] for col in cursor.description]  # Get column names
        results = cursor.fetchall()  # Fetch all results

        # Convert the results into JSON format
        json_results = []
        for row in results:
            row_dict = dict(zip(columns, row))  # Map columns to row values
            json_results.append(row_dict)

        # Print the formatted JSON output with custom encoder
        print(json.dumps(json_results, indent=4, cls=CustomJSONEncoder))

    finally:
        cursor.close()
        conn.close()

    # Return the results as JSON
    return json_results  # Return the JSON results


# Call the function to test
lotto_data = get_lotto_data()
