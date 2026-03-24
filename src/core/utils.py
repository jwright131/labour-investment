def sorted_int_list(series):
    return sorted(series.dropna().astype(int).unique().tolist())


def sorted_text_list(series):
    return sorted(series.dropna().astype(str).unique().tolist())


def default_one(options):
    return options[:2] if options else []


def filter_in(df, column, selected_values):
    if not selected_values:
        return df.iloc[0:0].copy()
    return df[df[column].isin(selected_values)].copy()


def format_list_for_text(values, max_items=4):
    if not values:
        return "None selected"
    if len(values) <= max_items:
        return ", ".join(str(v) for v in values)
    shown = ", ".join(str(v) for v in values[:max_items])
    return f"{shown}, +{len(values) - max_items} more"
