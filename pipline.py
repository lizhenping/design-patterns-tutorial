from abc import ABC, abstractmethod
from typing import Any, List, Dict, Optional
from dataclasses import dataclass, field
from enum import Enum

"""
设计模式教学示例：工作流编排系统

本示例展示了以下设计模式的应用：
1. 管道模式 (Pipeline Pattern) - WorkflowOrchestrator作为管道框架，Task作为管道阶段
2. 策略模式 (Strategy Pattern) - Task抽象类定义策略接口
3. 模板方法模式 (Template Method Pattern) - WorkflowOrchestrator定义算法骨架
4. 状态模式 (State Pattern) - TaskStatus管理状态转换
5. 依赖注入模式 (Dependency Injection) - 通过构造函数注入依赖
6. 责任链模式 (Chain of Responsibility) - 仅用于依赖检查机制
"""

# 【状态模式】：定义任务的各种状态
# State Pattern - 将状态封装为枚举，便于状态管理和转换
class TaskStatus(Enum):
    PENDING = "pending"      # 待执行状态
    RUNNING = "running"      # 执行中状态
    COMPLETED = "completed"  # 完成状态
    FAILED = "failed"        # 失败状态

# 【管道模式】：数据载体 - 在管道各阶段间传递数据
# Pipeline Pattern - WorkflowContext作为数据在管道中流动的载体
@dataclass
class WorkflowContext:
    workflow_id: str                                          # 工作流标识
    shared_data: Dict[str, Any] = field(default_factory=dict) # 管道中流动的共享数据
    task_results: Dict[str, Any] = field(default_factory=dict) # 各阶段的处理结果

# 【策略模式】：定义任务执行策略的抽象接口
# Strategy Pattern - Task抽象类定义策略接口，具体任务类实现不同策略
class Task(ABC):
    """任务抽象基类 - 策略模式的核心
    
    每个具体任务类都是一个独立的策略，实现不同的业务逻辑
    同时也是管道模式中的处理阶段
    """
    
    def __init__(self, task_id: str, name: str, dependencies: List[str] = None):
        self.task_id = task_id
        self.name = name
        self.dependencies = dependencies or []  # 【责任链模式】：任务依赖关系
        self.status = TaskStatus.PENDING        # 【状态模式】：初始状态为待执行
    
    @abstractmethod
    def execute(self, context: WorkflowContext) -> WorkflowContext:
        """【策略模式】策略接口：定义任务执行的统一接口
        【管道模式】处理阶段：接收数据，处理后传递给下一阶段
        """
        pass
    
    def can_execute(self, completed_tasks: set) -> bool:
        """【责任链模式】依赖检查：检查当前任务是否可以执行
        Chain of Responsibility - 检查依赖链是否满足
        """
        return all(dep in completed_tasks for dep in self.dependencies)

# 【策略模式】具体策略实现：展示策略模式的多态性
# 【管道模式】第一阶段：数据提取阶段
class DataExtractionTask(Task):
    """数据提取策略 - 管道的第一个处理阶段"""
    
    def __init__(self, source: str):
        super().__init__("extract_data", f"提取数据")  # 【依赖注入】：通过构造函数注入数据源
        self.source = source
    
    def execute(self, context: WorkflowContext) -> WorkflowContext:
        """【策略模式】具体策略实现 + 【管道模式】数据处理阶段"""
        print(f"执行策略: {self.name} - 从{self.source}提取数据")
        
        # 【管道模式】：生成原始数据并放入数据流
        data = [f"record_{i}" for i in range(10)]  # 简化数据生成
        context.shared_data["raw_data"] = data    # 数据流入管道
        context.task_results[self.task_id] = {"count": len(data)}
        
        return context  # 【管道模式】：返回更新后的上下文，传递给下一阶段


# 【策略模式】具体策略实现 + 【管道模式】第二阶段
class DataValidationTask(Task):
    """数据验证策略 - 管道的第二个处理阶段"""
    
    def __init__(self):
        # 【责任链模式】：设置依赖关系，必须在extract_data完成后才能执行
        super().__init__("validate_data", "验证数据", dependencies=["extract_data"])
    
    def execute(self, context: WorkflowContext) -> WorkflowContext:
        """【策略模式】具体策略实现 + 【管道模式】数据处理阶段"""
        print(f"执行策略: {self.name} - 验证数据质量")
        
        # 【管道模式】：从上一阶段获取数据，进行验证处理
        raw_data = context.shared_data.get("raw_data", [])
        valid_data = [item for item in raw_data if "record" in item]
        
        # 【管道模式】：将验证后的数据放入数据流
        context.shared_data["validated_data"] = valid_data
        context.task_results[self.task_id] = {"valid_count": len(valid_data)}
        
        return context  # 【管道模式】：传递给下一阶段


# 【策略模式】具体策略实现 + 【管道模式】第三阶段
class DataTransformationTask(Task):
    """数据转换策略 - 管道的第三个处理阶段"""
    
    def __init__(self):
        # 【责任链模式】：设置依赖关系，必须在validate_data完成后才能执行
        super().__init__("transform_data", "转换数据", dependencies=["validate_data"])
    
    def execute(self, context: WorkflowContext) -> WorkflowContext:
        """【策略模式】具体策略实现 + 【管道模式】数据处理阶段"""
        print(f"执行策略: {self.name} - 转换数据格式")
        
        # 【管道模式】：从上一阶段获取数据，进行转换处理
        validated_data = context.shared_data.get("validated_data", [])
        transformed_data = [item.upper() for item in validated_data]
        
        # 【管道模式】：将最终处理结果放入数据流
        context.shared_data["final_data"] = transformed_data
        context.task_results[self.task_id] = {"transformed_count": len(transformed_data)}
        
        return context  # 【管道模式】：管道处理完成

# 【管道模式 + 模板方法模式】：定义工作流执行的算法骨架
class WorkflowOrchestrator:
    """工作流编排器 - 多种设计模式的综合应用
    
    【管道模式】：将多个Task连接成数据处理管道，数据通过WorkflowContext在各阶段间流动
    【模板方法模式】：定义工作流执行的算法骨架：
    1. 构建执行计划
    2. 按计划执行任务
    3. 生成执行报告
    【依赖注入模式】：通过add_task方法注入具体的任务策略
    """
    
    def __init__(self, workflow_id: str):
        self.workflow_id = workflow_id
        # 【依赖注入模式】：任务策略容器，用于存储注入的具体策略
        self.tasks: Dict[str, Task] = {}
        
    def add_task(self, task: Task) -> 'WorkflowOrchestrator':
        """【依赖注入模式】：注入具体的任务策略到管道中
        【管道模式】：将任务作为管道阶段添加到处理流程中
        """
        self.tasks[task.task_id] = task
        return self  # 流式接口，支持链式调用
    
    def build_execution_plan(self) -> List[str]:
        """【模板方法模式】步骤1：构建执行计划（拓扑排序）
        【责任链模式】：通过依赖检查确定任务执行顺序
        【管道模式】：确定数据在管道中的流动顺序
        """
        completed = set()
        execution_plan = []
        
        while len(completed) < len(self.tasks):
            # 【责任链模式】：找到所有可执行的任务（依赖已满足）
            ready_tasks = [
                task_id for task_id, task in self.tasks.items()
                if task_id not in completed and task.can_execute(completed)
            ]
            
            if not ready_tasks:
                raise Exception("检测到循环依赖")
            
            # 选择第一个可执行的任务
            next_task = ready_tasks[0]
            execution_plan.append(next_task)
            completed.add(next_task)
        
        return execution_plan
    
    def execute(self, input_data: Dict[str, Any] = None) -> WorkflowContext:
        """【模板方法模式】：定义工作流执行的算法骨架
        【管道模式】：启动数据在管道中的流动处理
        """
        print(f"\n=== 开始执行工作流: {self.workflow_id} ===")
        
        # 【模板方法模式】步骤1：创建执行上下文
        # 【管道模式】：初始化数据载体
        context = WorkflowContext(workflow_id=self.workflow_id)
        if input_data:
            context.shared_data.update(input_data)
        
        # 【模板方法模式】步骤2：构建执行计划
        execution_plan = self.build_execution_plan()
        print(f"执行计划: {' -> '.join(execution_plan)}")
        
        # 【模板方法模式】步骤3：按计划执行任务
        # 【管道模式】：数据在各阶段间流动处理
        completed_tasks = set()
        for task_id in execution_plan:
            task = self.tasks[task_id]
            
            try:
                # 【状态模式】：更新任务状态
                task.status = TaskStatus.RUNNING
                # 【策略模式】：多态调用具体策略
                # 【管道模式】：数据流经当前处理阶段
                context = task.execute(context)
                task.status = TaskStatus.COMPLETED
                completed_tasks.add(task_id)
                
            except Exception as e:
                task.status = TaskStatus.FAILED
                print(f"任务失败: {task.name} - {str(e)}")
                break
        
        # 【模板方法模式】步骤4：生成执行报告
        self._generate_report(context)
        
        print(f"=== 工作流执行完成 ===\n")
        return context
    
    def _generate_report(self, context: WorkflowContext):
        """【模板方法模式】步骤4：生成执行报告
        【状态模式】：统计各任务的最终状态
        """
        # 【状态模式】：统计完成状态的任务数量
        completed = sum(1 for task in self.tasks.values() if task.status == TaskStatus.COMPLETED)
        total = len(self.tasks)
        
        print(f"执行报告: {completed}/{total} 任务完成")
        print(f"成功率: {completed/total:.1%}")

# 【综合应用示例】：多种设计模式的协同工作
if __name__ == "__main__":
    print("设计模式教学示例：工作流编排系统")
    print("展示6种设计模式的综合应用\n")
    
    # 【管道模式 + 模板方法模式】：创建工作流编排器
    orchestrator = WorkflowOrchestrator("数据处理工作流")
    
    # 【依赖注入模式 + 策略模式】：注入具体的任务策略到管道中
    # 【管道模式】：构建数据处理管道 extract -> validate -> transform
    orchestrator.add_task(DataExtractionTask("数据库")) \
               .add_task(DataValidationTask()) \
               .add_task(DataTransformationTask())
    
    # 【模板方法模式】：执行预定义的算法骨架
    # 【管道模式】：启动数据在管道中的流动
    result = orchestrator.execute({"batch_id": "batch_001"})
    
    # 查看最终结果
    print("\n=== 最终结果 ===")
    print(f"工作流ID: {result.workflow_id}")
    print(f"共享数据: {result.shared_data}")
    print(f"任务结果: {result.task_results}")
    
    print("\n=== 设计模式总结 ===")
    print("1. 【管道模式】：数据通过WorkflowContext在Task管道阶段间流动转换")
    print("2. 【策略模式】：Task抽象类定义策略接口，具体任务类实现不同策略")
    print("3. 【模板方法模式】：WorkflowOrchestrator定义执行算法骨架")
    print("4. 【依赖注入模式】：通过add_task方法注入具体策略")
    print("5. 【状态模式】：TaskStatus管理任务状态转换")
    print("6. 【责任链模式】：仅用于can_execute方法的依赖检查机制")