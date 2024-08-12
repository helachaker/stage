import pandas as pd
from sqlalchemy import create_engine
import django
import os
from django.conf import settings

# Configure Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projet_rh.settings")
django.setup()

def export_data_to_csv():
    # Create SQLAlchemy engine for MySQL using mysql-connector
    db_url = (
        f"mysql+mysqlconnector://{settings.DATABASES['default']['USER']}:"
        f"{settings.DATABASES['default']['PASSWORD']}@"
        f"{settings.DATABASES['default']['HOST']}:"
        f"{settings.DATABASES['default']['PORT']}/"
        f"{settings.DATABASES['default']['NAME']}"
    )
    engine = create_engine(db_url)

    # SQL Query to retrieve data
    query = '''
        SELECT
            e.first_name, e.last_name, e.date_of_birth, e.gender, e.position, e.department, e.hire_date, e.salary,
            p.performance_rating, p.salary_increase, b.absenteeism_days, b.overtime_hours,      
            s.satisfaction_score, f.feedback_text 
        FROM
            gestion_employee e
        JOIN
            gestion_performance p ON e.employee_id = p.employee_id
        JOIN
            gestion_behavior b ON e.employee_id = b.employee_id
        LEFT JOIN
            gestion_satisfactionsurvey s ON e.employee_id = s.employee_id
        LEFT JOIN
            gestion_feedback f ON e.employee_id = f.employee_id
    '''

    # Use pandas to execute query and export data
    df = pd.read_sql(query, engine)
    df.to_csv('exported_data.csv', index=False)

if __name__ == "__main__":
    export_data_to_csv()
