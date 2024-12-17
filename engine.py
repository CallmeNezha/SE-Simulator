#
import typing

class Data:
    ID = ''
    FORM = ''


class Document(Data):
    ...


class UpperLevelRequirementsAndExpectations(Data):
    ID = 'Upper Level Requirements And Expectations'
    FORM = 'informal'


class Process:
    ID = ''
    def __init__(self, parent=None):
        self._parent = parent
        self._children = []
        parent._children.append(self)

    @property
    def parent(self) -> typing.Optional['Process']:
        return self._parent

    @property
    def children(self) -> typing.List['Process']:
        return self._children


class SystemDesign(Process):
    ID = 'System Design'
    def __init__(self):
        Process.__init__(self)
        self.proc_requirement_definition = RequirementDefinition(self)
        self.proc_technical_solution_definition = TechnicalSolutionDefinition(self)


class RequirementDefinition(Process):
    ID = 'Requirement Definition'
    def __init__(self, parent=None):
        Process.__init__(self, parent)
        self.proc_stakeholder_expectations_definition = StakeholderExpectationsDefinition(self)
        self.proc_technical_requirements_definition = TechnicalRequirementsDefinition(self)


class TechnicalSolutionDefinition(Process):
    ID = 'Technical Solution Definition'
    def __init__(self, parent=None):
        Process.__init__(self, parent)
        self.proc_logical_decomposition = LogicalDecomposition(self)
        self.proc_design_solution_definition = DesignSolutionDefinition(self)


class StakeholderExpectationsDefinition(Process):
    ID = 'Stakeholder Expectations Definition'


class TechnicalRequirementsDefinition(Process):
    ID = 'Technical Requirements Definition'


class LogicalDecomposition(Process):
    ID = 'Logical Decomposition'


class DesignSolutionDefinition(Process):
    ID = 'Design Solution Definition'


class TechnicalManagement(Process):
    ID = 'Technical Management'
    def __init__(self):
        Process.__init__(self)


class TechnicalPlanning(Process):
    ID = 'Technical Planning'
    def __init__(self, parent=None):
        Process.__init__(self, parent)
        self.proc_technical_planning = TechnicalPlanning(self)
        self.proc_technical_control = TechnicalControl(self)
        self.proc_technical_assessment = TechnicalAssessment(self)
        self.proc_technical_decision_analysis = TechnicalDecisionAnalysis(self)


class TechnicalControl(Process):
    ID = 'Technical Control'
    def __init__(self, parent=None):
        Process.__init__(self, parent)
        self.proc_requirements_management = RequirementsManagement(self)
        self.proc_interface_management = InterfaceManagement(self)
        self.proc_technical_risk_management = TechnicalRiskManagement(self)
        self.proc_configuration_management = ConfigurationManagement(self)
        self.proc_technical_data_management = TechnicalDataManagement(self)


class RequirementsManagement(Process):
    ID = 'Requirements Management'


class InterfaceManagement(Process):
    ID = 'Interface Management'


class TechnicalRiskManagement(Process):
    ID = 'Technical Risk Management'


class ConfigurationManagement(Process):
    ID = 'Configuration Management'


class TechnicalDataManagement(Process):
    ID = 'Technical Data Management'


class TechnicalAssessment(Process):
    ID = 'Technical Assessment'


class TechnicalDecisionAnalysis(Process):
    ID = 'Technical Decision Analysis'

