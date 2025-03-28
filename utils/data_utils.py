import csv


def save_iocs_to_csv(iocs: list, filename: str):
    """
    Saves extracted IOCs to a CSV file.

    Args:
        iocs (list): List of extracted IOC data.
        filename (str): Name of the CSV file.
    """
    if not iocs:
        print("No IOCs to save.")
        return

    fieldnames = ["type", "value", "source", "raw_text"]

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for ioc in iocs:
            writer.writerow(ioc)

    print(f"Saved {len(iocs)} IOCs to '{filename}'.")
