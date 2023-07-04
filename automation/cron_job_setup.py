```python
import os
from crontab import CronTab

# Define the path to the script that will generate and post articles
script_path = os.path.join(os.path.dirname(__file__), '../wordpress_development/plugin_request_setup.php')

# Create a new cron job
cron = CronTab(user='root')

# Define the schedule (every hour)
job = cron.new(command='php {}'.format(script_path))
job.minute.every(60)

# Write the cron job
cron.write()
```