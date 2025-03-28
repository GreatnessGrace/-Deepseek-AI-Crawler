import csv

def save_iocs_to_csv(iocs, filename):
    # Expected columns in CSV
    expected_fields = ["url", "ioc_type", "ioc_value"]

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=expected_fields)

        # Write headers
        writer.writeheader()

        for ioc in iocs:
            # Filter out unexpected fields
            filtered_ioc = {key: ioc[key] for key in expected_fields if key in ioc}
            writer.writerow(filtered_ioc)
