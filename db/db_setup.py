import sqlite3

def create_tables():
    conn = sqlite3.connect('data/scraped_data.db')
    c = conn.cursor()

    # Generic jobs table
    c.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            keyword TEXT,
            location TEXT,
            dts TEXT,
            job_id TEXT PRIMARY KEY,
            job_url TEXT,
            job_title TEXT,
            job_location TEXT,
            post_date TEXT,
            end_date TEXT,
            company TEXT,
            contract_type TEXT,
            salary TEXT,
            job_description TEXT,
            insights TEXT,
            apply_url TEXT
        )
    ''')

    # You can add more table creation statements here for other types of data
    # For example:
    # c.execute('''
    #     CREATE TABLE IF NOT EXISTS reviews (
    #         product_id TEXT PRIMARY KEY,
    #         review_text TEXT,
    #         user TEXT,
    #         star_rating INTEGER,
    #         review_date TEXT
    #     )
    # ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
