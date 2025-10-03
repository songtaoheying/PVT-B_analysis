

# 简明心理运动警觉性测试（PVT-B）及数据简单分析

> 一个轻量、开源的 3 分钟注意力测试，基于 NASA 航天员研究范式。

 **在线体验**: https://songtaoheying.github.io/PVT-B_analysis/  
 **源码开源**: [GitHub](https://github.com/songtaoheying/PVT-B_analysis) (MIT License)

---

## 什么是 PVT-B？

PVT-B 是一种测量**持续注意力和警觉性**的标准化测试，用于：

*   睡眠与疲劳研究
*   高风险职业监测（如司机、医生）
*   心理学教学与认知评估

参与者需在黄色数字出现时**尽快按下空格键**。


---
## 测试后生成的数据

测试结束后，系统会生成以下数据，可用于分析：

| 指标 | 说明 |
| :--- | :--- |
| **Test End Time** | 测试完成的日期和时间 |
| **Average RT (ms)** | 正确反应的平均时间（毫秒），反映处理速度 |
| **Total Trials** | 总试验次数（通常 ~60 次） |
| **Lapses (>500ms)** | 反应过慢 (>500ms) 的次数，反映注意力涣散 |
| **Commissions (too early)** | 抢答 (<100ms) 的次数，反映冲动性 |

点击“Copy Data”按钮，可将以上数据复制为 CSV 格式，方便粘贴到 Excel、SPSS 或 Python 中进行进一步分析。

---

## 数据分析核心指标：OPS

> **反应时间 (RT)** 也是一个重要参数，综合 OPS 与 RT 能更全面地评估认知状态。

本项目的核心指标是 **OPS (Overall Performance Score, 整体表现得分)**。

**为什么是 OPS？**
根据 NASA 对航天员的研究 (Tu et al., 2022)，**测试前的平均 OPS 是预测未来疲劳和表现衰退的最重要指标之一**。**OPS 越高，代表基础警觉性越好，越能抵抗疲劳影响**。

### OPS 公式

$$
\text{OPS} = 1 - \frac{\text{Lapses (>500ms)} + \text{Commissions (too early)}}{\text{Total Trials}}
$$

*   **Lapses**: 反应过慢 (>500ms) 的次数
*   **Commissions**: 抢答 (<100ms) 的次数
*   **Total Trials**: 总试验次数

**解读**：值越接近 **1** 表现越好。

---
## 如何本地体验测试


- 下载文件：
在本项目的 GitHub 页面，找到右边Releases,下载zip文件
- 找到主文件：
打开解压后的文件夹，找到名为 PVT-B.html 的文件。
- 直接运行：
双击 PVT-B.html 文件。
它会自动在您的默认浏览器（如 Chrome, Edge, Safari）中打开。
无需安装任何软件，无需联网，即可开始测试！
## 如何本地分析数据
测试完成后点击历史数据,可以查看历史数据和通过图表查看趋势


---

## 灵感来源


本项目设计灵感来源于 [PsyToolkit ](https://www.psytoolkit.org/experiment-library/pvtb.html)的 PVT-B 演示
为了方便本地运行和数据分析,开发为html单文件测试
所有代码均为原创


---

## 参考文献

*   **Tu, D. et al. (2022)**. Dynamic ensemble prediction of cognitive performance in spaceflight. *Scientific Reports*.
*   Basner, M. et al. (2011). Validity and sensitivity of a brief Psychomotor Vigilance Test (PVT-B). *Acta Astronautica*.

---

## 隐私说明

所有数据**仅在您的浏览器中处理,不会上传**

---

## 许可证：MIT

欢迎用于科研、教学、自由使用与修改。
请引用本项目链接。
