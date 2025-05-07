import pandas as pd
import ast

def extract(filepath):
    return pd.read_csv(filepath)

def transform(df):
    # Drop rows missing essential fields
    df = df.dropna(subset=['Title', 'Instructions'])

    # Clean whitespace in Title and Instructions
    df['Title'] = df['Title'].str.strip()
    df['Instructions'] = df['Instructions'].str.strip()

    # Try parsing ingredients from Cleaned_Ingredients column
    def parse_ingredients(ing_str):
        try:
            return ast.literal_eval(ing_str)
        except:
            return []

    df['Parsed_Ingredients'] = df['Cleaned_Ingredients'].apply(parse_ingredients)

    return df[['Title', 'Parsed_Ingredients', 'Instructions']]

def load(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to: {output_path}")

# Run the ETL pipeline
if __name__ == "__main__":
    raw_path = "13k-recipes.csv"
    cleaned_path = "cleaned_recipes.csv"

    df_raw = extract(raw_path)
    df_clean = transform(df_raw)
    load(df_clean, cleaned_path)
