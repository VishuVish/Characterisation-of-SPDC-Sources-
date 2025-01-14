import os

def process_file(file_path, is_coincidence):
    with open(file_path, 'r') as file:
        lines = file.readlines()[5:]

        valid_counts = []
        idler_counts = []
        signal_counts = []

        for line in lines:
            parts = line.strip().split(';')
            channel = float(parts[0])
            count = float(parts[1])

            if count == 0:
                continue

            if is_coincidence:
                valid_counts.append(count)
            else:
                if channel == 2.0000:
                    idler_counts.append(count)
                elif channel == 3.0000:
                    signal_counts.append(count)

    if is_coincidence:
        return sum(valid_counts) / len(valid_counts) if valid_counts else 0
    else:
        avg_idler = sum(idler_counts) / len(idler_counts) if idler_counts else 0
        avg_signal = sum(signal_counts) / len(signal_counts) if signal_counts else 0
        return avg_idler, avg_signal

def main(folder_path):
    coincidence_files = [f for f in os.listdir(folder_path) if 'Coincidence' in f]
    single_count_files = [f for f in os.listdir(folder_path) if 'SingleCount' in f]

    total_coincidence = 0
    total_idler = 0
    total_signal = 0

    for file in coincidence_files:
        avg_coincidence = process_file(os.path.join(folder_path, file), True)
        total_coincidence += avg_coincidence

    avg_total_coincidence = total_coincidence / len(coincidence_files) if coincidence_files else 0

    for file in single_count_files:
        avg_idler, avg_signal = process_file(os.path.join(folder_path, file), False)
        total_idler += avg_idler
        total_signal += avg_signal

    avg_idler_counts = total_idler / len(single_count_files) if single_count_files else 0
    avg_signal_counts = total_signal / len(single_count_files) if single_count_files else 0

    print(f"Averaged Total Coincidence Counts: {avg_total_coincidence}")
    print(f"Averaged Idler Counts: {avg_idler_counts}")
    print(f"Averaged Signal Counts: {avg_signal_counts}")

if __name__ == "__main__":
    folder_path = ("C:/Users/vishn/OneDrive/Desktop/FSU Jena/University of Jena/1st Sem/Quantum Laboratory/Reports/Lab 06 SPDC/EQT WS24/EXP 03 25/32first dip")
    main(folder_path)