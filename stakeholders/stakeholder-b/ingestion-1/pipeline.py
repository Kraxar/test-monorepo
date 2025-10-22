"""
Stakeholder B - Ingestion Pipeline 1
"""

def run_ingestion():
    print("Running Stakeholder B ingestion")
    from shared.common_functions.utils import validate_data
    
    data = {"source": "stakeholder-b", "type": "ingestion-1"}
    if validate_data(data):
        print("Data validated successfully")
    return data

if __name__ == "__main__":
    run_ingestion()
