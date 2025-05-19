import pandas as pd

def parse_cif_to_csv(file_path, output_csv):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    atom_data = []
    capture = False
    headers = []

    for line in lines:
        if 'loop_' in line:
            capture = False  # Reset capture
            continue
        if line.strip().startswith('_atom_site_'):
            headers.append(line.strip().split('_atom_site_')[-1])
            capture = True
        elif capture:
            if line.strip() == '' or line.startswith('_'):
                break  # End of loop
            atom_data.append(line.strip().split())

    df = pd.DataFrame(atom_data, columns=headers)
    df.to_csv(output_csv, index=False)
    print(f"CSV saved to: {output_csv}")

# Example usage:
parse_cif_to_csv("S0026461X18000889sup001.cif", "atom_sites.csv")
