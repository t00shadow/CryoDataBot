import pandas as pd
import os
from concurrent.futures import ProcessPoolExecutor, as_completed
from tqdm import tqdm
from collections import Counter


def soft_path_filter(raw_df):
    non_unique_mask = raw_df.duplicated(subset='xref_UNIPROTKB', keep=False)
    # Gives you a dataframe that has all the duplicates
    non_unique_df = raw_df[non_unique_mask].reset_index(drop=True)
    # Drops the rows that are not unique based on previous dataframe
    unique_df = raw_df.drop(non_unique_df.index).reset_index(drop=True)
    return unique_df, non_unique_df


def process_similar(uniprotkb_1, uniprotkb_2, threshold) -> bool:
    # change df to lists
    list1 = str(uniprotkb_1).split(',')
    list2 = str(uniprotkb_2).split(',')

    # Count elements in both lists
    counter1 = Counter(list1)
    counter2 = Counter(list2)

    # Find common elements and their counts
    common_elements = counter1 & counter2
    longer_list_length = max(len(list1), len(list2))
    percentage = sum(common_elements.values())/longer_list_length*100

    if percentage < threshold:
        return True
    else:
        return False


def hard_pass_filter(raw_df: pd.DataFrame, threshold):
    process_df = raw_df
    saved_df = pd.DataFrame(columns=raw_df.columns)
    dropped_df = pd.DataFrame(columns=raw_df.columns)
    pbar = tqdm(total=len(raw_df))  # Progress bar
    while True:
        # Compare the aim row with other rows
        aim = process_df['xref_UNIPROTKB'][0]
        target = process_df['xref_UNIPROTKB'][0:-1]
        # Append the first row of process_df to save_df
        first_row = process_df.head(1)
        saved_df = pd.concat([saved_df, first_row], ignore_index=True)
        # remove first row
        process_df = process_df[0:-1]
        # comparing (multiprocess to improve runtime)
        with ProcessPoolExecutor() as executor:
            futures = [executor.submit(process_similar, aim, row, threshold) for row in target]
            mask = []
            for future in as_completed(futures):
                mask.append(future.result())
        # Update dropped rows
        rows_to_append = process_df[~pd.Series(mask)]
        if not rows_to_append.empty:
            dropped_df = pd.concat([dropped_df, rows_to_append], ignore_index=True)
        # Update process_df with new indexing
        process_df = process_df[pd.Series(mask)].reset_index(drop=True)
        # progress bar
        pbar.update(mask.count(False)+1)
        if len(process_df) <= 1:
            saved_df = pd.concat([saved_df, process_df.head(1)], ignore_index=True)
            pbar.update(1)
            break
    return saved_df, dropped_df


def refine_csv(file_path, save_path, threshold):
    """
    :param file_path: path to .csv file
    :param save_path:
    :param threshold: percentage similarity
    """
    print('\n--------------------------------------------------------------------------------\nRefining .csv file...')
    file_name = os.path.basename(file_path)
    file_name = file_name.replace('.csv', '')
    raw_df = pd.read_csv(file_path)
    soft_kept, soft_filtered = soft_path_filter(raw_df)
    hard_kept, hard_filtered = hard_pass_filter(soft_kept, threshold)
    hard_kept.to_csv(save_path + file_name + '_kept.csv', index=False)
    final_path = save_path + file_name + '_filtered.csv'
    pd.concat([soft_filtered, hard_filtered]).reset_index(drop=True).\
        to_csv(final_path, index=False)
    print(f'Refinement completed, entries kept: {len(hard_kept)}. File wrote at {final_path}.')
    print('--------------------------------------------------------------------------------\n')


if __name__ == '__main__':
    csv_path = r'C:/Users/30105/PycharmProjects/pythonProject/download_file_01_review.csv'
    save_dir = r'C:/Users/30105/PycharmProjects/pythonProject/'
    refine_csv(csv_path, save_dir, threshold=50)


