from datasets import load_dataset
try:
    ds = load_dataset("MIAMAI/TMMLUplus", "medical_license", split="test")
    for i in range(3):
        print(ds[i])
except Exception as e:
    print(e)
