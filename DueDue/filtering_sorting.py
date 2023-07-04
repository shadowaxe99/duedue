```python
def filter_sort(contract_dates, user_config):
    """
    Function to filter and sort contract dates based on user configuration.
    """
    # Extract filter and sort options from user configuration
    filter_option = user_config.get('filter_option', None)
    sort_option = user_config.get('sort_option', None)

    # Apply filter if specified
    if filter_option:
        contract_dates = [date for date in contract_dates if filter_option in date]

    # Apply sort if specified
    if sort_option:
        if sort_option == 'ascending':
            contract_dates.sort()
        elif sort_option == 'descending':
            contract_dates.sort(reverse=True)

    return contract_dates
```