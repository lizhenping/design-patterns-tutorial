# Design Patterns Tutorial

## 📚 Project Overview

This project is a comprehensive design patterns tutorial that helps developers understand and master classic design patterns through Python code examples. Each pattern includes detailed code implementation, explanatory comments, and real-world application scenarios.

## 🎯 Learning Objectives

- Understand the core concepts of 23 classic design patterns
- Master the application of design patterns in real projects
- Improve code maintainability, extensibility, and reusability
- Develop best practices for object-oriented design

## 📁 Directory Structure

```
design-patterns-tutorial/
├── README.md                    # Chinese documentation
├── README_EN.md                 # English documentation
├── 01-creational-patterns/      # Creational Patterns
│   ├── singleton/               # Singleton Pattern
│   ├── factory/                 # Factory Method Pattern
│   ├── abstract-factory/        # Abstract Factory Pattern
│   ├── builder/                 # Builder Pattern
│   └── prototype/               # Prototype Pattern
├── 02-structural-patterns/      # Structural Patterns
│   ├── adapter/                 # Adapter Pattern
│   ├── bridge/                  # Bridge Pattern
│   ├── composite/               # Composite Pattern
│   ├── decorator/               # Decorator Pattern
│   ├── facade/                  # Facade Pattern
│   ├── flyweight/               # Flyweight Pattern
│   └── proxy/                   # Proxy Pattern
├── 03-behavioral-patterns/      # Behavioral Patterns
│   ├── chain-of-responsibility/ # Chain of Responsibility Pattern
│   ├── command/                 # Command Pattern
│   ├── interpreter/             # Interpreter Pattern
│   ├── iterator/                # Iterator Pattern
│   ├── mediator/                # Mediator Pattern
│   ├── memento/                 # Memento Pattern
│   ├── observer/                # Observer Pattern
│   ├── state/                   # State Pattern
│   ├── strategy/                # Strategy Pattern
│   ├── template-method/         # Template Method Pattern
│   └── visitor/                 # Visitor Pattern
├── 04-compound-patterns/        # Compound Patterns
│   ├── mvc/                     # MVC Pattern
│   ├── mvp/                     # MVP Pattern
│   ├── mvvm/                    # MVVM Pattern
│   └── pipeline/                # Pipeline Pattern
│       └── workflow_orchestrator.py  # Workflow Orchestration Example
├── examples/                    # Comprehensive Examples
├── assets/                      # Resource Files
└── docs/                        # Documentation
```

## 🚀 Quick Start

### Requirements

- Python 3.8+
- Virtual environment recommended

### Installation

```bash
# Activate conda environment
source activate alphasql

# Navigate to project directory
cd /root/autodl-tmp/nl2sql/NL2SQL/design-patterns-tutorial

# Install dependencies (if needed)
pip install -r requirements.txt
```

### Running Examples

```bash
# Run workflow orchestration example (demonstrates 6 design patterns working together)
python 04-compound-patterns/pipeline/workflow_orchestrator.py
```

## 📖 Learning Path

### Beginner Path
1. **Creational Patterns** - Start with Singleton to understand object creation control
2. **Structural Patterns** - Learn Adapter and Decorator patterns to understand object composition
3. **Behavioral Patterns** - Master Observer and Strategy patterns to understand object interaction
4. **Compound Patterns** - Learn how to combine multiple patterns for complex problems

### Advanced Path
1. Deep understanding of each pattern's use cases and trade-offs
2. Learning pattern combinations and interactions
3. Applying design patterns in real projects
4. Understanding anti-patterns and over-engineering issues

## 🎨 Design Pattern Categories

### Creational Patterns
Deal with object creation mechanisms, separating object creation from usage.

- **Singleton** - Ensure a class has only one instance
- **Factory Method** - Create objects through an interface, subclasses decide which class to instantiate
- **Abstract Factory** - Interface for creating families of related objects
- **Builder** - Construct complex objects step by step
- **Prototype** - Create new objects by copying existing instances

### Structural Patterns
Deal with object composition to form larger structures.

- **Adapter** - Allow incompatible interfaces to work together
- **Bridge** - Separate abstraction from implementation
- **Composite** - Compose objects into tree structures
- **Decorator** - Dynamically add new functionality to objects
- **Facade** - Provide a simple interface to a complex subsystem
- **Flyweight** - Reduce memory usage through sharing
- **Proxy** - Provide a proxy for an object to control access

### Behavioral Patterns
Focus on communication between objects and responsibility assignment.

- **Chain of Responsibility** - Pass requests along a chain of handlers
- **Command** - Encapsulate requests as objects
- **Interpreter** - Define a representation for a language's grammar
- **Iterator** - Sequentially access elements of a collection
- **Mediator** - Define how objects interact with each other
- **Memento** - Save and restore object state
- **Observer** - Define one-to-many dependencies between objects
- **State** - Change object behavior based on internal state
- **Strategy** - Define a family of algorithms and make them interchangeable
- **Template Method** - Define algorithm skeleton, subclasses implement specific steps
- **Visitor** - Define new operations without modifying classes

### Compound Patterns
Combinations of multiple patterns to solve complex design problems.

- **MVC Pattern** - Model-View-Controller architecture
- **MVP Pattern** - Model-View-Presenter architecture
- **MVVM Pattern** - Model-View-ViewModel architecture
- **Pipeline Pattern** - Data processing pipeline (implemented example)

## 🌟 Featured Example

### Workflow Orchestration System
Located at `04-compound-patterns/pipeline/workflow_orchestrator.py`, this comprehensive example demonstrates 6 design patterns working together:

1. **Pipeline Pattern** - WorkflowOrchestrator as pipeline framework
2. **Strategy Pattern** - Task abstract class defines strategy interface
3. **Template Method Pattern** - Defines workflow execution algorithm skeleton
4. **State Pattern** - TaskStatus manages state transitions
5. **Dependency Injection Pattern** - Inject dependencies through constructors
6. **Chain of Responsibility Pattern** - Used for dependency checking mechanism

## 📝 Code Standards

- Each pattern includes detailed comments
- Type hints for improved code readability
- Follows PEP 8 code style guidelines
- Includes real-world application examples
- Unit tests provided (planned)

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

For questions or suggestions, please contact us through:

- Submit an Issue
- Email: lizhenping18@mails.ucas.ac.cn
- Join the discussion

---

**Happy Coding! 🎉**