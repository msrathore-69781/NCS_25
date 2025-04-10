import os
import pandas as pd

# Path to the folder containing all your Excel files
folder_path = "excel_files"

# Get all Excel files in the folder
excel_files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

# List to store data from second sheets
all_dataframes = []

for file in excel_files:
    file_path = os.path.join(folder_path, file)
    
    try:
        # Load the Excel file
        xlsx = pd.ExcelFile(file_path)

        # Ensure there is a second sheet
        if len(xlsx.sheet_names) >= 2:
            second_sheet_name = xlsx.sheet_names[1]
            df = xlsx.parse(second_sheet_name)

            # Optionally add the file name as a column to trace back
            df['Source File'] = file

            all_dataframes.append(df)
        else:
            print(f"⚠️ Skipped {file} — it doesn't have a second sheet.")
    
    except Exception as e:
        print(f"❌ Error reading {file}: {e}")

# Combine all into a single DataFrame
combined_df = pd.concat(all_dataframes, ignore_index=True)

# Export to Excel
combined_df.to_excel("Combined_Second_Sheets.xlsx", index=False)

print("✅ Combined data from second sheets into Combined_Second_Sheets.xlsx")
