import pandas as pd

def update_csv(correct, false, mode='standard'):
    print(correct, false, mode)
    # try: 
    if mode == 'standard':
        file_path = '/Users/matthew/Documents/College/Projects/Mental-Math/data/standard.csv'
    elif mode == 'large_multi':
        file_path = '/Users/matthew/Documents/College/Projects/Mental-Math/data/large_multi.csv'
    elif mode == 'complex':
        file_path = '/Users/matthew/Documents/College/Projects/Mental-Math/data/complex.csv'

    df = pd.read_csv(file_path)

    if len(df) > 0:
        idx = df.iloc[:, 0].max()
    else:
        idx = 0

    new_record = [idx + 1, correct, correct/(correct+false)]
    new_df = pd.DataFrame([new_record], columns=df.columns)
    updated_df = pd.concat([df, new_df], ignore_index=True)
    updated_df.to_csv(file_path, index=False)
    # except:
    #     return False
    return True

if __name__ == '__main__':
    update_csv(10, 5, 'complex')

