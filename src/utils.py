import pandas as pd
import os

def save_to_csv(data_list, filename="quotes_final.csv"):
    """Save the list of dictionaries to the processed data folder."""
    # Define path: data/processed/filename
    output_path = os.path.join("data", "processed", filename)
    
    # Ensure the folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    df = pd.DataFrame(data_list)
    df.to_csv(output_path, index=False)
    print(f"Success: Data saved to {output_path}")