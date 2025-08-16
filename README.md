# 设计模式教学指南

## 📚 项目简介

本项目是一个全面的设计模式教学指南，通过Python代码示例帮助开发者深入理解和掌握经典的设计模式。每个模式都包含详细的代码实现、注释说明和实际应用场景。

## 🎯 学习目标

- 理解23种经典设计模式的核心思想
- 掌握设计模式在实际项目中的应用
- 提升代码的可维护性、可扩展性和可复用性
- 培养面向对象设计的最佳实践

## 📁 目录结构

```
design-patterns-tutorial/
├── README.md                    # 中文说明文档
├── README_EN.md                 # 英文说明文档
├── 01-creational-patterns/      # 创建型模式
│   ├── singleton/               # 单例模式
│   ├── factory/                 # 工厂方法模式
│   ├── abstract-factory/        # 抽象工厂模式
│   ├── builder/                 # 建造者模式
│   └── prototype/               # 原型模式
├── 02-structural-patterns/      # 结构型模式
│   ├── adapter/                 # 适配器模式
│   ├── bridge/                  # 桥接模式
│   ├── composite/               # 组合模式
│   ├── decorator/               # 装饰器模式
│   ├── facade/                  # 外观模式
│   ├── flyweight/               # 享元模式
│   └── proxy/                   # 代理模式
├── 03-behavioral-patterns/      # 行为型模式
│   ├── chain-of-responsibility/ # 责任链模式
│   ├── command/                 # 命令模式
│   ├── interpreter/             # 解释器模式
│   ├── iterator/                # 迭代器模式
│   ├── mediator/                # 中介者模式
│   ├── memento/                 # 备忘录模式
│   ├── observer/                # 观察者模式
│   ├── state/                   # 状态模式
│   ├── strategy/                # 策略模式
│   ├── template-method/         # 模板方法模式
│   └── visitor/                 # 访问者模式
├── 04-compound-patterns/        # 复合模式
│   ├── mvc/                     # MVC模式
│   ├── mvp/                     # MVP模式
│   ├── mvvm/                    # MVVM模式
│   └── pipeline/                # 管道模式
│       └── workflow_orchestrator.py  # 工作流编排示例
├── examples/                    # 综合示例
├── assets/                      # 资源文件
└── docs/                        # 文档资料
```

## 🚀 快速开始

### 环境要求

- Python 3.8+
- 推荐使用虚拟环境

### 安装依赖

```bash
# 激活conda环境
source activate alphasql

# 进入项目目录
cd /root/autodl-tmp/nl2sql/NL2SQL/design-patterns-tutorial

# 安装依赖（如有需要）
pip install -r requirements.txt
```

### 运行示例

```bash
# 运行工作流编排示例（展示6种设计模式的综合应用）
python 04-compound-patterns/pipeline/workflow_orchestrator.py
```

## 📖 学习路径

### 初学者路径
1. **创建型模式** - 从单例模式开始，理解对象创建的控制
2. **结构型模式** - 学习适配器和装饰器模式，理解对象组合
3. **行为型模式** - 掌握观察者和策略模式，理解对象交互
4. **复合模式** - 学习如何组合多种模式解决复杂问题

### 进阶路径
1. 深入理解每种模式的适用场景和权衡
2. 学习模式之间的组合使用
3. 在实际项目中应用设计模式
4. 理解反模式和过度设计的问题

## 🎨 设计模式分类

### 创建型模式 (Creational Patterns)
负责对象的创建过程，将对象的创建与使用分离。

- **单例模式 (Singleton)** - 确保类只有一个实例
- **工厂方法模式 (Factory Method)** - 创建对象的接口，子类决定实例化哪个类
- **抽象工厂模式 (Abstract Factory)** - 创建相关对象家族的接口
- **建造者模式 (Builder)** - 分步骤构建复杂对象
- **原型模式 (Prototype)** - 通过复制现有实例创建新对象

### 结构型模式 (Structural Patterns)
处理类和对象的组合，形成更大的结构。

- **适配器模式 (Adapter)** - 使不兼容的接口能够协同工作
- **桥接模式 (Bridge)** - 将抽象与实现分离
- **组合模式 (Composite)** - 将对象组合成树形结构
- **装饰器模式 (Decorator)** - 动态地给对象添加新功能
- **外观模式 (Facade)** - 为复杂子系统提供简单接口
- **享元模式 (Flyweight)** - 通过共享减少内存使用
- **代理模式 (Proxy)** - 为对象提供代理以控制访问

### 行为型模式 (Behavioral Patterns)
关注对象之间的通信和职责分配。

- **责任链模式 (Chain of Responsibility)** - 将请求沿着处理链传递
- **命令模式 (Command)** - 将请求封装为对象
- **解释器模式 (Interpreter)** - 定义语言的语法表示
- **迭代器模式 (Iterator)** - 顺序访问集合元素
- **中介者模式 (Mediator)** - 定义对象间的交互方式
- **备忘录模式 (Memento)** - 保存和恢复对象状态
- **观察者模式 (Observer)** - 定义对象间的一对多依赖
- **状态模式 (State)** - 根据内部状态改变对象行为
- **策略模式 (Strategy)** - 定义算法家族并使其可互换
- **模板方法模式 (Template Method)** - 定义算法骨架，子类实现具体步骤
- **访问者模式 (Visitor)** - 在不修改类的前提下定义新操作

### 复合模式 (Compound Patterns)
多种模式的组合应用，解决复杂的设计问题。

- **MVC模式** - 模型-视图-控制器架构
- **MVP模式** - 模型-视图-展示器架构
- **MVVM模式** - 模型-视图-视图模型架构
- **管道模式** - 数据流处理管道（已实现示例）

## 🌟 特色示例

### 工作流编排系统
位于 `04-compound-patterns/pipeline/workflow_orchestrator.py`，这是一个综合示例，展示了6种设计模式的协同应用：

1. **管道模式** - WorkflowOrchestrator作为管道框架
2. **策略模式** - Task抽象类定义策略接口
3. **模板方法模式** - 定义工作流执行算法骨架
4. **状态模式** - TaskStatus管理状态转换
5. **依赖注入模式** - 通过构造函数注入依赖
6. **责任链模式** - 用于依赖检查机制

## 📝 代码规范

- 每个模式都包含详细的中文注释
- 使用类型提示提高代码可读性
- 遵循PEP 8代码风格规范
- 包含实际应用场景的示例
- 提供单元测试（计划中）

## 🤝 贡献指南

欢迎贡献代码、文档或建议！请遵循以下步骤：

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 📞 联系方式

如有问题或建议，请通过以下方式联系：

- 提交 Issue
- 邮箱：lizhenping18@mails.ucas.ac.cn
- 参与讨论

---

**Happy Coding! 🎉**