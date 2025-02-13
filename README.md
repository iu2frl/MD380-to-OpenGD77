# CSV Converter

## Description

This Python script converts a CSV file containing radio channel information exported from `DMR Codeplug Editor v1.1.21 by G6AMU` into a CSV that can be ingested by `OpenGD77 CPS (Version R2024.12.20.01)`.

Both softwares are in the `CPS_Softwares` folder.

This helped me save a lot of time when I had to convert a large number of radio channels from one format to another.

## Features

This repo includes script to convert:

- Contacts list
- Channels list
  - The channels list converter needs the original contacts list to convert the contacts IDs (MD380 format) to names (OpenGD77 format)

## Known issues

- The channels converter cannot convert the TX and RX CTCSS/DCS codes, I have not figured out the MD380 encoding yet.

## Input Format

The input CSV file must have a header with the following fields:

```csv
"name","mode","rx freq","tx freq","bandwidth","auto scan","squelch mode",...
```

Each row represents a radio channel with its corresponding parameters.

The file was exported by using the `DMR Codeplug Editor v1.1.21 by G6AMU` software, browsing to the `Channels` tab, and clicking on the `Export` button.

## Output Format

The resulting CSV file will have the following header:

```csv
Channel Number,Channel Name,Channel Type,Rx Frequency,Tx Frequency,Bandwidth (kHz),...
```

Data is reformatted, and some columns have predefined or calculated values.

The file is imported into the `OpenGD77 CPS (Version R2024.12.20.01)` software by browsing to the `File` menu, selecting `CSV`, then `Open` and choosing the folder containing the converted CSV file.

> [!TIP]
> The output file should be called `Channels.csv` for the OpenGD77 CPS to recognize it.

## Requirements

- Python 3.x

## Example

### Example of converting a contacts list

```sh
python contacts_converter.py original_channels.csv converted_channels.csv
```

### Example of converting a channels list

```sh
python channels_converter.py original_channels.csv converted_channels.csv original_contacts.csv
```
