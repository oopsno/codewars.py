# codewars.py

[![Travis](https://img.shields.io/travis/oopsno/codewars.py.svg?style=flat-square)]()
[![Code Climate](https://img.shields.io/codeclimate/maintainability/oopsno/codewars.py.svg?style=flat-square)]()
[![Coveralls github](https://img.shields.io/coveralls/oopsno/codewars.py/master.svg?style=flat-square)]()

## 简介

这是一个用 [Python][Python] 刷 [CodeWars][CodeWars] 的仓库

> 反正刷了也找不到工作啊喵...

## 依赖

+ (必须) Python 3.6+
+ (可选) Coverage.py 4.0+

## 使用

要检查是不是写对了

```shell
python test/test_all.py
```

要检查覆盖率

```shell
coverage run test/test_all.py && coverage report
```

## 结构

### codewars

目前 `codewars` 模块仅实现了 [CodeWars测试框架][CWTF] 到标准库中的 [`unittest`][PyUT] 的转译器

### solutions

放答案的地方

### test

#### test_framework

测试 `codewars.Test`

#### test_all

- 加载 `test_framework` 并运行
- 加载 `solutions` 中的所有题解的单元测试，并逐一运行
- 当且仅当全部测试通过时，解释器以返回值0结束



[CodeWars]: https://www.codewars.com
[Python]: https://www.python.org
[CWTF]: https://github.com/Codewars/codewars.com/wiki/Codewars-Python-Test-Framework
[PyUT]: https://docs.python.org/3/library/unittest.html
