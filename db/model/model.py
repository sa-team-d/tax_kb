from typing import List, Optional

class KPIFormula:
    def __init__(self, formula: str, unit_measure: str, aggregation_type: str):
        self.formula = formula
        self.unit_measure = unit_measure
        self.aggregation_type = aggregation_type


class KPIObjective:
    def __init__(self, objective: str, subobjectives: Optional[List['KPIObjective']] = None):
        self.objective = objective
        self.subobjectives = subobjectives or []


class KPI:
    def __init__(
        self,
        id: str,
        name: str,
        description: str,
        taxonomy_type: str,
        formula: KPIFormula,
        objective: KPIObjective,
        children: Optional[List[str]] = None,
    ):
        self.id = id
        self.name = name
        self.description = description
        self.taxonomy_type = taxonomy_type
        self.formula = formula
        self.objective = objective
        self.children = children or []

    def to_dict(self):
        """Convert the object into a dictionary for MongoDB storage."""
        return {
            "_id": self.id,
            "name": self.name,
            "description": self.description,
            "taxonomy_type": self.taxonomy_type,
            "formula": {
                "formula": self.formula.formula,
                "unit_measure": self.formula.unit_measure,
                "aggregation_type": self.formula.aggregation_type,
            },
            "objective": {
                "business_objective": self.objective.objective,
                "subobjectives": [
                    {"business_objective": subobjective.objective}
                    for subobjective in self.objective.subobjectives
                ],
            },
            "children": self.children,
        }

 