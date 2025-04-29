     
import json
import os
import psycopg2
from psycopg2.extras import RealDictCursor
import sys
import re
 
 
def extract_query_from_log(log_json):
    """Extract the SQL query and its parameters from the log JSON."""
    try:
        data = json.loads(log_json)
        sql = data["jsonPayload"]["sql"]
        args = data["jsonPayload"]["args"]
        return sql, args
    except (json.JSONDecodeError, KeyError) as e:
        print(f"Error parsing log JSON: {e}")
        sys.exit(1)
 
 
def run_explain_analyze(sql, args):
    """Run the query with EXPLAIN ANALYZE and return the results."""
    # Add EXPLAIN ANALYZE to the query
    explain_sql = f"EXPLAIN (ANALYZE, COSTS, VERBOSE, BUFFERS, FORMAT JSON) {sql}"
 
    try:
        # Get database URL from environment variable
        db_url = os.getenv("POSTGRES_URL")
        if not db_url:
            raise ValueError("POSTGRES_URL environment variable is not set")
 
        # Connect to the database
        with psycopg2.connect(db_url) as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                # Execute the query with EXPLAIN ANALYZE
                # Convert $1, $2, etc. to %($1)s, %($2)s, etc. in the SQL
                explain_sql = re.sub(r"\$(\d+)", r"%($\1)s", explain_sql)
 
                # Create a dictionary of parameters
                params = {f"${i+1}": arg for i, arg in enumerate(args)}
 
                cur.execute(explain_sql, params)
                result = cur.fetchone()
                return result["QUERY PLAN"]
 
    except Exception as e:
        print(f"Error executing query: {e}")
        sys.exit(1)
 
 
def main():
    # Read the log JSON from stdin
    log_json = sys.stdin.read()
 
    # Extract the query and parameters
    sql, args = extract_query_from_log(log_json)
 
    # Run EXPLAIN ANALYZE
    explain_result = run_explain_analyze(sql, args)
 
    # Print the result
    print(json.dumps(explain_result, indent=2))
 
 
if __name__ == "__main__":
    main()