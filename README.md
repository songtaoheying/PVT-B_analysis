# 🧠 简明心理运动警觉性测试（PVT-B）网页版

一个轻量、开源的 [PVT-B](https://doi.org/10.1016/j.actaastro.2011.07.015) 实现，用于测量注意力、反应时间和疲劳程度。基于 Dinges 实验范式，适用于睡眠研究、认知评估和教育用途。

🌐 **在线体验**:https://songtaoheying.github.io/PVT-B_analysis/

📥 **源码开源**: [GitHub](https://github.com/songtaoheying/PVT-B_analysis) (MIT 许可)

---

## 🔍 什么是 PVT-B？

PVT-B（Brief Psychomotor Vigilance Test）是一种 **3分钟持续注意力测试**，广泛用于：
- 睡眠剥夺研究
- 疲劳监测（如司机、医生、飞行员）
- 航天员认知表现评估（NASA 使用）
- 心理学教学实验

参与者需在黄色数字出现时**尽快按下空格键**，避免提前按键或反应过慢。

---

## 📊 测试结束后输出数据：

| 指标 | 说明 |
|------|------|
| Test End Time | 完成时间 |
| Average RT (ms) | 正确反应的平均反应时间 |
| Total Trials | 总试验次数 |
| Lapses (>500ms) | 反应超过 500ms 的次数 |
| Commissions (too early) | 提前按键（<100ms）次数 |

点击“Copy Data”可复制为 CSV，粘贴到 Excel 或 SPSS 分析。

---

## 📚 参考文献

- Basner, M., Mollicone, D., & Dinges, D. F. (2011). [Validity and sensitivity of a brief PVT-B](https://doi.org/10.1016/j.actaastro.2011.07.015)
- Dinges, D. F., & Powell, J. W. (1985). Microcomputer analyses of performance...
- Wilkinson, R. T., & Houghton, D. (1982). [Field test of arousal](https://doi.org/10.1177/001872088202400409)

灵感来自 [PsyToolkit PVT-B demo](https://www.psytoolkit.org/experiment-library/pvtb.html)

---

## 🛠️ 如何使用？

1. 直接打开 [在线链接](https://你的用户名.github.io/pvtb-web)
2. 或下载 `index.html` 本地运行（双击即可）
3. 用于研究时请添加知情同意流程

> ⚠️ 数据仅在浏览器中处理，不会上传服务器。

---

## 📄 许可证：MIT

你可以自由使用、修改、分发本项目，用于科研或教学。  
请引用原始研究作者和本项目链接。
