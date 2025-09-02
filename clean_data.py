import pandas as pd
import csv

def clean_and_save(input_file, output_file):
    data = []
    header = None

    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if not row or all(cell.strip() == '' for cell in row):  # 跳过空行
                continue
            # 判断是否是表头（根据第一列是否是 "Test End Time"）
            if row[0] == 'Test End Time' or 'End Time' in row[0]:
                if header is None:  # 只保留第一次的表头
                    header = [col.strip() for col in row]
                continue  # 跳过所有表头行
            # 正常数据行
            if len(row) == len(header):
                data.append([cell.strip() for cell in row])

    if not header:
        raise ValueError("未找到表头！")

    # 创建 DataFrame
    df = pd.DataFrame(data, columns=header)

    # 类型转换
    df['Average RT (ms)'] = pd.to_numeric(df['Average RT (ms)'])
    df['Total Trials'] = pd.to_numeric(df['Total Trials'])
    df['Lapses (>500ms)'] = pd.to_numeric(df['Lapses (>500ms)'])
    df['Commissions (too early)'] = pd.to_numeric(df['Commissions (too early)'])
    df['Test End Time'] = pd.to_datetime(df['Test End Time'], format='%Y/%m/%d %H:%M:%S')

    # 保存为新的标准 CSV 文件
    df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"✅ 已保存处理后的数据到: {output_file}")
    return df

# === 使用示例 ===
input_path = 'raw_data.txt'        # 你的原始文件（包含多个表头块）
output_path = 'cleaned_data.csv'   # 输出的新文件（标准格式）

df = clean_and_save(input_path, output_path)