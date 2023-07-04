```python
import pandas as pd

contract_dates = []

def generate_report(contract_dates):
    df = pd.DataFrame(contract_dates, columns=['Contract', 'Date'])
    
    # Basic statistics
    report = df.describe(include='all')
    
    # Additional insights
    report['Earliest Contract Date'] = df['Date'].min()
    report['Latest Contract Date'] = df['Date'].max()
    report['Total Contracts'] = df['Contract'].count()
    
    return report
```