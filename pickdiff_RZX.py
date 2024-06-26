import sys
import numpy as np
from ase.io import read, write
from dscribe.descriptors import ACSF
from multiprocessing import Pool, cpu_count
from scipy.optimize import linear_sum_assignment

def calculate_acsf_fingerprints(atoms_list, acsf_params):
    acsf = ACSF(**acsf_params)
    fingerprints = [acsf.create(atoms) for atoms in atoms_list]
    return fingerprints

def fingerprint_distance(fp1, fp2):
    cost_matrix = np.linalg.norm(fp1[:, np.newaxis] - fp2[np.newaxis, :], axis=2)
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    distance = cost_matrix[row_ind, col_ind].sum()
    return distance

def find_unique_structures(fingerprints, threshold):
    n = len(fingerprints)
    selected_indices = set(range(n))
    for i in range(n):
        if i not in selected_indices:
            continue
        for j in range(i + 1, n):
            if j not in selected_indices:
                continue
            distance = fingerprint_distance(fingerprints[i], fingerprints[j])
            if distance < threshold:
                selected_indices.remove(j)
    return list(selected_indices)


def process_chunk(args):
    chunk, acsf_params, distance_threshold = args
    fingerprints = calculate_acsf_fingerprints(chunk, acsf_params)
    unique_indices = find_unique_structures(fingerprints, distance_threshold)
    selected_structures = [chunk[i] for i in unique_indices]
    return selected_structures

def main(input_file, output_file, acsf_params, distance_threshold):
    structures = read(input_file, index=':')
    num_structures = len(structures)
    while num_structures > 2000 :
        print(f"Read {num_structures} structures from {input_file}")

        num_cores = cpu_count()
        chunk_size = max(1, num_structures // num_cores)
        chunks = [(structures[i:i + chunk_size], acsf_params, distance_threshold) 
                  for i in range(0, num_structures, chunk_size)]

        print(f"Divided structures into {len(chunks)} chunks of up to {chunk_size} structures each")

        # Use multiprocessing to process chunks in parallel
        with Pool(cpu_count()) as pool:
            results = pool.map(process_chunk, chunks)

        # Flatten the list of selected structures
        all_selected_structures = [structure for sublist in results for structure in sublist]
        print(f"Total selected structures after chunk processing: {len(all_selected_structures)}")
        structures=all_selected_structures
        num_structures_old = num_structures
        num_structures = len(structures)
        if abs(num_structures_old-num_structures) < 10:
            break
    
    # Calculate fingerprints for all selected structures from all chunks
    merged_fingerprints = calculate_acsf_fingerprints(all_selected_structures, acsf_params)
    final_unique_indices = find_unique_structures(merged_fingerprints, distance_threshold)
    final_selected_structures = [all_selected_structures[i] for i in final_unique_indices]

    write(output_file, final_selected_structures)
    print(f"Wrote {len(final_selected_structures)} unique structures to {output_file}")


#def main(input_file, output_file, acsf_params, distance_threshold):
#    structures = read(input_file, index=':')
#    print(f"Read {len(structures)} structures from {input_file}")
#    fingerprints = calculate_acsf_fingerprints(structures, acsf_params)
#    print("Fingerprints calculated:")
#    #for i, fp in enumerate(fingerprints):
#    #    print(f"Structure {i}: Fingerprint shape {fp.shape}, dtype {fp.dtype}")
#
#    unique_indices = find_unique_structures(fingerprints, distance_threshold)
#    selected_structures = [structures[i] for i in unique_indices]
#    write(output_file, selected_structures)
#    print(f"Wrote {len(selected_structures)} selected structures to {output_file}")

if __name__ == "__main__":
    acsf_params = {
        "species": ["Mg", "Ti", "O"],  # Example species, adjust as needed
        "r_cut": 6.0,
        "g2_params":[[0.0001, 0.1000],[0.001, 0.1000],[0.01, 0.1000],[0.1, 0.1000],[0.2, 0.1000],[0.4, 0.1000],[0.5, 0.1000],[1.0, 0.1000],
                   [0.0001, 1.0000],[0.001, 1.0000],[0.01, 1.0000],[0.1, 1.0000],[0.2, 1.0000],[0.4, 1.0000],[0.5, 1.0000],[1.0, 1.0000]],
        "g4_params": [[0.0001, 0.10, 1.0],[0.001, 0.10, 1.0],[0.01, 0.10, 1.0],[0.05, 0.10, 1.0],[0.1, 0.10, 1.0],[0.2, 0.10, 1.0],[0.5, 0.10, 1.0],
                   [0.0001, 0.50, 1.0],[0.001, 0.50, 1.0],[0.01, 0.50, 1.0],[0.05, 0.50, 1.0],[0.1, 0.50, 1.0],[0.2, 0.50, 1.0],[0.5, 0.50, 1.0],
                   [0.0001, 2.00, 1.0],[0.001, 2.00, 1.0],[0.01, 2.00, 1.0],[0.05, 2.00, 1.0],[0.1, 2.00, 1.0],[0.2, 2.00, 1.0],[0.5, 2.00, 1.0],
                   [0.0001, 4.00, 1.0],[0.001, 4.00, 1.0],[0.01, 4.00, 1.0],[0.05, 4.00, 1.0],[0.1, 4.00, 1.0],[0.2, 4.00, 1.0],[0.5, 4.00, 1.0],
                   [0.0001, 7.50, 1.0],[0.001, 7.50, 1.0],[0.01, 7.50, 1.0],[0.05, 7.50, 1.0],[0.1, 7.50, 1.0],[0.2, 7.50, 1.0],[0.5, 7.50, 1.0],
                   [0.0001, 10.0, 1.0],[0.001, 10.0, 1.0],[0.01, 10.0, 1.0],[0.05, 10.0, 1.0],[0.1, 10.0, 1.0],[0.2, 10.0, 1.0],[0.5, 10.0, 1.0]]
                   
    }
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    distance_threshold = float(sys.argv[3])
    
    main(input_file, output_file, acsf_params, distance_threshold)

