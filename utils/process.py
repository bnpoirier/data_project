

# Converts string to ordinal numbers
def categorize(column):
    column = column.astype('category')
    column = column.cat.reorder_categories(column.unique(), ordered=True)

    return column.cat.codes