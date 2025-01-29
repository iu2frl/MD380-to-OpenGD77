import csv
import sys

def convert_csv(input_file, output_file):
    with open(input_file, newline='', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.writer(outfile)
        
        # Scrittura intestazione del nuovo formato
        writer.writerow([
            "Channel Number", "Channel Name", "Channel Type", "Rx Frequency", "Tx Frequency",
            "Bandwidth (kHz)", "Colour Code", "Timeslot", "Contact", "TG List", "DMR ID",
            "TS1_TA_Tx", "TS2_TA_Tx ID", "RX Tone", "TX Tone", "Squelch", "Power", "Rx Only",
            "Zone Skip", "All Skip", "TOT", "VOX", "No Beep", "No Eco", "APRS",
            "Latitude", "Longitude", "Use Location"
        ])
        
        channel_number = 1
        for row in reader:
            writer.writerow([
                channel_number,
                row["name"].strip(),
                "Digital" if row["mode"] == "2" else "Analogue",
                f"{int(row['rx freq']) / 1e5:.5f}",
                f"{int(row['tx freq']) / 1e5:.5f}",
                "12.5",  # Valore fisso della banda
                row["colour code"].strip(),
                row["repeater slot"].strip(),
                row["contact"].strip(),
                "",  # TG List non presente nel file originale
                "",  # DMR ID non presente nel file originale
                "",  # TS1_TA_Tx non presente nel file originale
                "",  # TS2_TA_Tx ID non presente nel file originale
                "None",  # RX Tone non specificato
                "None",  # TX Tone non specificato
                "Disabled" if row["squelch mode"] == "0" else "Enabled",
                "P7",  # Mappatura della potenza non specificata, valore di default
                "No" if row["rx only"] == "0" else "Yes",
                "No",  # Zone Skip non presente
                "No",  # All Skip non presente
                row["tx time out"].strip(),
                "Off" if row["vox"] == "0" else "On",
                "No",  # No Beep non presente
                "No",  # No Eco non presente
                "None",  # APRS non presente
                "0.128",  # Latitudine di default
                "0.008",  # Longitudine di default
                "No"  # Use Location
            ])
            channel_number += 1

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input.csv output.csv")
        sys.exit(1)
    convert_csv(sys.argv[1], sys.argv[2])