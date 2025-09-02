import pandas as pd

# 1. 读取 CSV 文件
df = pd.read_csv('cleaned_data.csv')

# 2. 转换时间列并按 'Test End Time' 排序
df['Test End Time'] = pd.to_datetime(df['Test End Time'])
df = df.sort_values('Test End Time').reset_index(drop=True)

# 3. 分配 id（从 1 开始）
df['id'] = range(1, len(df) + 1)

# 4. 提取 Average RT (ms)
df['Average RT (ms)'] = df['Average RT (ms)']  # 直接保留

# 5. 安全计算 OPS：防止 Total Trials 为 0
df['OPS'] = df.apply(
    lambda row: 1 - (row['Lapses (>500ms)'] + row['Commissions (too early)']) / row['Total Trials']
    if row['Total Trials'] > 0 else 0,
    axis=1
)

# 6. 计算 Standardized OPS
ops_mean = df['OPS'].mean()
ops_std = df['OPS'].std()

if ops_std == 0:
    df['Standardized OPS'] = 0.0
else:
    df['Standardized OPS'] = (df['OPS'] - ops_mean) / ops_std

# 7. 选择需要的列输出
result = df[['id', 'Test End Time', 'Average RT (ms)', 'OPS', 'Standardized OPS']]

# 8. 保存为 result.csv，保留合适的浮点精度
result.to_csv('result.csv', index=False, float_format='%.6f')

print("✅ 数据处理完成，已保存为 result.csv")
print(result)