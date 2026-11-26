# pairwise-shadow-removal-illum

## 领域

游戏、图形与多媒体

## 主题

图像阴影去除与光照一致性

## 说明

软阴影半影保留、结构引导纹理填充、光源方向时域对齐。

初始状态下 `imaging/shadow_removal.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
