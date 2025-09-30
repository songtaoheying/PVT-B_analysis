# data_process.py
import pandas as pd
import csv
from datetime import datetime

def append_raw_data(file_path, raw_text):
    """
    追加新数据到原始数据文件

    Args:
        file_path (str): 原始数据文件路径
        raw_text (str): 原始文本数据
    """
    # 直接追加文本数据，无需解析
    with open(file_path, 'a', newline='', encoding='utf-8') as f:
        f.write(raw_text)
        # 添加个空行
        f.write('\n\n\n')

def clean_and_save(input_file, output_file):
    """
    清理原始数据文件并保存为标准CSV格式

    Args:
        input_file (str): 原始数据文件路径
        output_file (str): 清理后数据保存路径

    Returns:
        pandas.DataFrame: 清理后的数据框
    """
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

def process_data(input_file, output_file):
    """
    处理清理后的数据，计算指标并保存结果

    Args:
        input_file (str): 清理后数据文件路径
        output_file (str): 最终结果保存路径
    """
    # 1. 读取 CSV 文件
    df = pd.read_csv(input_file)

    # 2. 转换时间列并按 'Test End Time' 排序
    df['Test End Time'] = pd.to_datetime(df['Test End Time'])
    df = df.sort_values('Test End Time').reset_index(drop=True)

    # 3. 分配 id（从 1 开始）
    df['id'] = range(1, len(df) + 1)

    # 4. 提取 Average RT (ms)
    df['Average RT (ms)'] = df['Average RT (ms)']  # 直接保留

    # 5. 新增列: 1/RT (注意处理 RT 为 0 的情况)
    # 使用 .loc 避免除零错误
    df['Mean 1/RT'] = 0.0  # 先初始化
    mask = df['Average RT (ms)'] > 0  # 创建布尔掩码
    df.loc[mask, 'Mean 1/RT'] = 1 / (df.loc[mask, 'Average RT (ms)'] / 1000)

    # 6. 安全计算 OPS：防止 Total Trials 为 0
    df['OPS'] = 0.0  # 先初始化
    mask = df['Total Trials'] > 0  # 创建布尔掩码
    df.loc[mask, 'OPS'] = 1 - (df.loc[mask, 'Lapses (>500ms)'] + df.loc[mask, 'Commissions (too early)']) / df.loc[mask, 'Total Trials']

    # 7. 选择需要的列输出（加入 '1/RT'）
    result = df[['id', 'Test End Time', 'Average RT (ms)', 'Mean 1/RT', 'OPS']]

    # 8. 保存为 result.csv，保留合适的浮点精度
    result.to_csv(output_file, index=False, float_format='%.6f')
    print(f"✅ 数据处理完成，已保存为 {output_file}")

def get_user_input():
    """
    获取用户输入的数据

    Returns:
        tuple: 包含测试数据的元组
    """
    print("请输入测试数据:")
    test_end_time = input("测试结束时间 (格式: YYYY/MM/DD HH:MM:SS，回车使用当前时间): ").strip()
    if not test_end_time:
        test_end_time = datetime.now().strftime('%Y/%m/%d %H:%M:%S')

    avg_rt = float(input("平均反应时间 (ms): "))
    total_trials = int(input("总试验次数: "))
    lapses = int(input("超时次数 (>500ms): "))
    commissions = int(input("过早反应次数: "))

    return test_end_time, avg_rt, total_trials, lapses, commissions

def main():
    """
    主函数：执行完整的数据输入、清理和处理流程
    """
    # 获取用户输入的原始文本
    print("请输入测试数据（完整的CSV文本）:")
    raw_text = ""
    try:
        while True:
            line = input()
            if line == "":  # 空行表示输入结束
                break
            raw_text += line + "\n"
    except KeyboardInterrupt:
        pass

    # 追加数据到原始文件
    raw_data_file = 'raw_data.txt'
    append_raw_data(raw_data_file, raw_text)
    print(f"✅ 数据已追加到 {raw_data_file}")

    # 处理步骤1: 清理数据
    cleaned_data_file = 'cleaned_data.csv'
    clean_and_save(raw_data_file, cleaned_data_file)

    # 处理步骤2: 计算指标
    result_file = 'result.csv'
    process_data(cleaned_data_file, result_file)

    print("\n✅ 所有处理已完成!")
    print(f"原始数据文件: {raw_data_file}")
    print(f"清理后数据文件: {cleaned_data_file}")
    print(f"结果文件: {result_file}")


if __name__ == "__main__":
    main()
