import kagglehub

# Download latest version
path = kagglehub.dataset_download("hammadulmustafa/pakistan-stock-exchange-top-50-2021-2025")

print("Path to dataset files:", path)