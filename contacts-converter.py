#!/usr/bin/env python3
import csv
import sys
import argparse

def convert_row(input_row):
    """Convert a single input row to output format"""
    # Extract data from input row
    id_num, name, call_type, *_ = input_row
    
    # Create output row
    # Using the TG number from the name (e.g., "TG2" -> "2") as part of conversion
    tg_num = ''.join(filter(str.isdigit, name))
    
    return {
        'Contact Name': name.strip(),
        'ID': id_num,
        'ID Type': 'Group' if 'Group' in call_type else 'Private',
        'TS Override': 'Disabled'
    }

def convert_csv(input_file, output_file):
    try:
        # Read input CSV
        with open(input_file, 'r', newline='') as infile:
            reader = csv.reader(infile)
            input_data = list(reader)
        
        # Convert data
        output_data = [convert_row(row) for row in input_data]
        
        # Write output CSV with header
        fieldnames = ['Contact Name', 'ID', 'ID Type', 'TS Override']
        with open(output_file, 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(output_data)
            
        return True
    except Exception as e:
        print(f"Error processing CSV: {e}", file=sys.stderr)
        return False

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Convert CSV file format')
    parser.add_argument('input_file', help='Input CSV file path')
    parser.add_argument('output_file', help='Output CSV file path')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Convert the file
    if convert_csv(args.input_file, args.output_file):
        print(f"Successfully converted {args.input_file} to {args.output_file}")
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()