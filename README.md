# CSV Converter

## Description

This Python script converts a CSV file containing radio channel information exported from `DMR Codeplug Editor v1.1.21 by G6AMU` into a CSV that can be ingested by `OpenGD77 CPS (Version R2024.12.20.01)`.

Both softwares are in the `CPS_Softwares` folder.

This helped me save a lot of time when I had to convert a large number of radio channels from one format to another.

## Usage

Run the script from the command line, specifying the input file and the output file:

```sh
python channels_converter.py input.csv output.csv
```

If exactly two arguments are not provided, the script will display an error message and terminate.

## Input Format

The input CSV file must have a header with the following fields:

```csv
"name","mode","rx freq","tx freq","bandwidth","auto scan","squelch mode",...
```

Each row represents a radio channel with its corresponding parameters.

## Output Format

The resulting CSV file will have the following header:

```csv
Channel Number,Channel Name,Channel Type,Rx Frequency,Tx Frequency,Bandwidth (kHz),...
```

Data is reformatted, and some columns have predefined or calculated values.

## Requirements

- Python 3.x

## Example

Example of converting a file:

```sh
python channels_converter.py original_channels.csv converted_channels.csv
```
