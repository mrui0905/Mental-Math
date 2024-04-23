import pandas as pd

def update_csv(correct, false, mode='standard'):
    try: 
        if mode == 'standard':
            file_path = 'data/standard.csv'

        df = pd.read_csv(file_path)

        if len(df) > 0:
            idx = df.iloc[:, 0].max()
        else:
            idx = 0

        new_record = [idx + 1, correct, correct/(correct+false)]
        new_df = pd.DataFrame([new_record], columns=df.columns)
        updated_df = pd.concat([df, new_df], ignore_index=True)
        updated_df.to_csv(file_path, index=False)
    except:
        return False
    return True

