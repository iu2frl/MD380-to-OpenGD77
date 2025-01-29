import csv
import sys

contacts_dict = dict()

def load_contacts(input_file):
    with open(input_file, newline='', encoding='utf-8') as infile:
        contact_id = 1
        for line in infile:
            line = line.replace('"', '').strip()
            split_line = line.split(',')
            if not split_line:
                continue
            contact_name = split_line[1].strip()
            contacts_dict[contact_id] = contact_name
            print(f"Loaded contact {contact_id}: {contact_name}")
            contact_id += 1

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
                contacts_dict.get(int(row["contact"].strip(), 0)),
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
            print(f"Converted channel {channel_number}: {row['name']}")
            print(f"  Rx Freq: {int(row['rx freq']) / 1e5:.5f}")
            print(f"  Tx Freq: {int(row['tx freq']) / 1e5:.5f}")
            print(f"  Colour Code: {row['colour code']}")
            print(f"  Repeater Slot: {row['repeater slot']}")
            print(f"  Contact: {contacts_dict.get(int(row["contact"].strip()), 0)}")
            print(f"  TX Time Out: {row['tx time out']}")
            print(f"  Squelch Mode: {row['squelch mode']}")
            print(f"  RX Only: {row['rx only']}")
            print(f"  VOX: {row['vox']}")
            channel_number += 1

if __name__ == "__main__":
    if 3 < len(sys.argv) < 4:
        print("Usage: python script.py input.csv output.csv [contacts.csv]")
        sys.exit(1)

    if len(sys.argv) == 4:
        load_contacts(sys.argv[3])
    else:
        print("Contacts file not provided, contacts for DMR channels will be empty")

    convert_csv(sys.argv[1], sys.argv[2])
