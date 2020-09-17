## Hellinger transformation:

def hellinger_transformation(id_rows, df):
    ''' id_rows --> this is the first column or columns and is a separate df.
        df --> these columns are the counts (with the column headers) of the data matrix.'''
    margin_total = df.sum(axis=1)
    transform = df.apply(lambda x: np.sqrt(x / margin_total))
    new_df = pd.concat([id_rows, transform], axis=1)
    return new_df
