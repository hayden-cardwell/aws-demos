import pandas as pd
import plotly.express as px

# Sample data for AG Grid (AWS EC2 Instances)
df_grid = pd.DataFrame(
    {
        "Instance ID": [
            "i-0123456789abcdef0",
            "i-0fedcba9876543210",
            "i-0abcdef0123456789",
        ],
        "Instance Type": ["t2.micro", "m5.large", "c6g.medium"],
        "Region": ["us-east-1", "us-west-2", "eu-central-1"],
        "State": ["running", "stopped", "running"],
    }
)

# Sample data for Plotly chart (AWS S3 Buckets)
df_chart = pd.DataFrame(
    {
        "Bucket Name": ["my-logs-bucket", "my-data-lake", "my-website-assets"],
        "Number of Objects": [15000, 500000, 2500],
        "Total Size (GB)": [50, 800, 10],
    }
)
