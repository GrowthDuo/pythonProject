'''
好的，你可以在 Python 中通过以下代码导入 `random` 模块：

```python
import random
```

这样，你就可以在代码中使用 `random` 模块中的所有方法了。例如，你可以使用 `random.randint(a, b)` 方法生成 `[a, b]` 范围内的随机整数。


Python 中标准库 `random` 模块除了 `randint` 方法外，还提供了其他常用的生成随机数的方法。

一些常用的方法包括：
- `random.random()`：生成一个 [0, 1) 范围内的随机浮点数。
- `random.uniform(a, b)`：生成一个 [a, b] 范围内的随机浮点数。
- `random.choice(seq)`：从序列 `seq` 中随机选择一个元素返回。
- `random.sample(population, k)`：从总体 `population` 中随机选择 `k` 个元素形成一个新的序列返回。
- `random.shuffle(lst)`：将序列 `lst` 中的元素随机打乱顺序。

需要注意的是，与 `randint` 方法类似，这些方法都需要事先导入 `random` 模块。
'''